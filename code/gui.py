
#############################################################################
# Display the GUI of IoTrain-Sim
#############################################################################

# Standard library imports
import os
import webbrowser
from collections import OrderedDict
import re
import Tkinter as tk
import ttk
import tkMessageBox

# Local imports
from content import Content
from cooja import CoojaManager
from storyboard import Storyboard

# Tree structure constants
TREE_ROOT = ""
ITEM_OPEN = True
KEY_PREFIX = " "

# Visual aspect constants (adjusted for the Instant Contiki VM)
FONT_SIZE = 11 # 15
WINDOW_SIZE = "420x500"

# Class that displays GUI training menus
class GUI(object):

    # Insert the dictionary content into the menu tree structure
    def process_dict(self, dict, tree, parent, is_open):
        for key, value in dict.items():
            if type(value) is str:
                if ".pdf" in value:
                    tree.insert(parent, "end", text=KEY_PREFIX+key, values=value, image=self.icon_pdf)
                elif ".csc" in value:
                    tree.insert(parent, "end", text=KEY_PREFIX+key, values=value, image=self.icon_csc)
                else:
                    # We insert unknown files without icon and print an error message
                    tree.insert(parent, "end", text=KEY_PREFIX+key, values=value)
                    print(Storyboard.ERROR_UNKNOWN_FILE_TYPE.format(value))
            else:
                child = tree.insert(parent, "end", text=key, open=is_open, tag=Storyboard.TAG_CATEGORY)
                self.process_dict(value, tree, child, is_open)

    # Do the appropriate action on the file identified by the file name argument
    def do_file_action(self, database_path, file_name):

        if not file_name:
            return

        file_list = []

        # Traverse database_path to find all the files and add them to the list
        for home, _, files in os.walk(database_path):
            for full_name in files:
                file_list.append(os.path.join(home, full_name))

        # Try to find the file name and apply the appropriate action
        file_found = False
        for file_path in file_list:
            if file_name in file_path:
                file_found = True

                # PDF files are opened via the webbrowser library
                if os.path.splitext(file_name)[1] == ".pdf":
                    # Make sure to add the "file://" prefix, or it will not work on macOS
                    # NOTE: There seems to be no way to catch errors in webbrowser.open()
                    webbrowser.open("file://" + os.path.abspath(file_path))

                # CSC files are opened via a helper function
                elif os.path.splitext(file_name)[1] == ".csc":
                    # Use helper class to open CSC file
                    exit_status = CoojaManager().open_csc_file(file_path)
                    if exit_status != 0:
                        tkMessageBox.showerror(title=Storyboard.ERROR_COOJA_DIALOG_TITLE_GUI,
                            message=Storyboard.ERROR_CSC_FAILED_GUI)

                # Handle unknown file types
                else:
                    tkMessageBox.showerror(title=Storyboard.ERROR_MAIN_DIALOG_TITLE_GUI,
                            message=Storyboard.ERROR_UNKNOWN_FILE_TYPE_GUI.format(file_name))

        # Deal with the case that the target file was not found
        if not file_found:
            tkMessageBox.showerror(title=Storyboard.ERROR_MAIN_DIALOG_TITLE_GUI,
                            message=Storyboard.ERROR_FILE_NOT_LOCATED_GUI.format(file_name))

    # Start GUI menu
    def start(self):

        # Setup window
        window = tk.Tk()

        # Prepare resources
        self.icon_csc = tk.PhotoImage(file=Storyboard.IOTRAIN_FIGURES_PATH + "icon_csc.gif")
        self.icon_pdf = tk.PhotoImage(file=Storyboard.IOTRAIN_FIGURES_PATH + "icon_pdf.gif")

        ############################################
        # Create a tree view panel
        tree = ttk.Treeview(window, height=10, show="tree headings", selectmode="browse")
        style = ttk.Style()
        style.configure("Treeview", font=("", FONT_SIZE), rowheight=21)
        tree.tag_configure(Storyboard.TAG_CATEGORY, font=("", FONT_SIZE, "bold"))
        # Color reference: https://www.rapidtables.com/web/color/gray-color.html
        style.configure("Treeview.Heading", foreground="#696969", font=("", FONT_SIZE, "bold"))
        #style.configure('Treeview', relief = 'flat', borderwidth = 0)
        #style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) # Remove borders
        tree.heading("#0", text=Storyboard.HEADING_NAME)

        # Setup vertical and horizontal scrollbars for tree
        y_scrollbar = tk.Scrollbar(tree, orient=tk.VERTICAL, command=tree.yview)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        x_scrollbar = tk.Scrollbar(tree, orient=tk.HORIZONTAL, command=tree.xview)
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        tree.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)

        # Default scrollbar width is supposed to be 16, but padding looks better with 13
        # Reference: https://effbot.org/tkinterbook/scrollbar.htm
        PADDING_X=13
        PADDING_Y=PADDING_X
        tree.pack(side=tk.TOP, expand=True, fill=tk.BOTH, padx=(PADDING_X,0))

        # Import training content into tree
        content = Content().training_content
        self.process_dict(content, tree, TREE_ROOT, not ITEM_OPEN)

        ############################################
        # Set up buttons

        ## Callback functions
        def delete_tree(tree):
            items = tree.get_children()
            for item in items:
                tree.delete(item)
        def expand_callback():
            delete_tree(tree)
            self.process_dict(content, tree, TREE_ROOT, ITEM_OPEN)
        def collapse_callback():
            delete_tree(tree)
            self.process_dict(content, tree, TREE_ROOT, not ITEM_OPEN)
        def cooja_callback():
            print(Storyboard.INFO_START_COOJA)
            # Use helper class to start Cooja
            # (set cursor before, and reset cursor after the operation)
            # NOTE: The "wait" cursor maps to native cursors on macOS & Windows,
            # but it is not portable, so we use "watch" instead
            # Reference: https://www.tcl.tk/man/tcl8.6/TkCmd/cursors.htm
            window.config(cursor="watch")
            cooja_button.config(cursor="watch")
            exit_status = CoojaManager().start_cooja()
            window.config(cursor="")
            cooja_button.config(cursor="")
            if exit_status != 0:
                tkMessageBox.showerror(title=Storyboard.ERROR_COOJA_DIALOG_TITLE_GUI,
                    message=Storyboard.ERROR_COOJA_FAILED_GUI)

        ## Actual button setup
        expand_button = ttk.Button(window, text=Storyboard.BUTTON_EXPAND_ALL,
            command=expand_callback)
        collapse_button = ttk.Button(window, text=Storyboard.BUTTON_COLLAPSE_ALL,
            command=collapse_callback)
        cooja_button = ttk.Button(window, text=Storyboard.BUTTON_START_COOJA,
            command=cooja_callback)
        quit_button = ttk.Button(window, text=Storyboard.BUTTON_QUIT,
            command=window.destroy)
        expand_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(PADDING_X,0), pady=(0,PADDING_Y))
        collapse_button.pack(side=tk.LEFT, expand=True, fill=tk.X, pady=(0,PADDING_Y))
        cooja_button.pack(side=tk.LEFT, expand=True, fill=tk.X, pady=(0,PADDING_Y))
        quit_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0,PADDING_X), pady=(0,PADDING_Y))

        # Set up an action for when a file is clicked
        def on_click(event):
            if tree.selection():
                file_name_list = tree.item(tree.selection()[0], "values")
                if file_name_list:
                    if not os.path.isdir(Storyboard.IOTRAIN_DATABASE_PATH):
                        tkMessageBox.showerror(title=Storyboard.ERROR_MAIN_DIALOG_TITLE_GUI,
                            message=Storyboard.ERROR_DATABASE_NOT_FOUND_GUI.format(Storyboard.IOTRAIN_DATABASE_PATH))
                    else:
                        # Perform action on file
                        # (set cursor before, and reset cursor after the operation)
                        window.config(cursor="watch")
                        tree.config(cursor="watch")
                        self.do_file_action(Storyboard.IOTRAIN_DATABASE_PATH, file_name_list[0])
                        window.config(cursor="")
                        tree.config(cursor="")
        #tree.bind("<ButtonRelease-1>", on_click) # Single click
        tree.bind("<Double-1>", on_click) # Double click

        ############################################
        # Set up window for GUI
        window.geometry(WINDOW_SIZE)
        window.title("IoTrain-Sim")
        menubar = tk.Menu(window)
        iotrain_sim_menu = tk.Menu(menubar, tearoff=0) # Disable tearoff (detachable menu) feature
        iotrain_sim_menu.add_command(label=Storyboard.BUTTON_START_COOJA, command=cooja_callback)
        iotrain_sim_menu.add_separator()
        iotrain_sim_menu.add_command(label=Storyboard.BUTTON_QUIT, command=window.quit)
        menubar.add_cascade(label="IoTrain-Sim", menu=iotrain_sim_menu)
        window.config(menu=menubar)

        # Start the window loop
        window.mainloop()
