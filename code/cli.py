
#############################################################################
# Display the CLI of IoTrain-Sim
#############################################################################

# Standard library imports
import os
import webbrowser
from collections import OrderedDict

# Local imports
from content import Content
from cooja import CoojaManager
from storyboard import Storyboard

# Class that displays CLI training menus
class CLI(object):

    # Enable debug messages
    debug = False

    # Find the full path for the file identified by the file name argument
    def find_file(self, database_path, file_name):

        if not file_name:
            return None

        file_list = []

        # Traverse database_path to find all the files and add them to the list
        for home, _, files in os.walk(database_path):
            for full_name in files:
                file_list.append(os.path.join(home, full_name))

        for file_path in file_list:
            if file_name in file_path:
                return file_path

        return None

    # Check whether a choice is in the menu range
    def is_in_menu_range(self, choice, menu):
        if choice > 0 and choice <= len(menu):
            return True
        else:
            return False

    # Clear the screen when displaying CLI menu
    def clear_screen(self):
        os.system("clear")

    # Display the top training menu
    def display_top_menu(self):

        # Clear initialization information
        self.clear_screen()

        # Display the top-level menu
        try:
            self.show_menu(Content().training_content)

        # Catch the quit exception, which indicates that the user wants to quit
        except QuitException:
            return

    # Show the current training menu; this function works recursively to enable back and forth menu navigation
    def show_menu(self, menu):

        # Loop forever
        while True:

            # Build list with menu data
            current_menu = list(menu)

            # Display the training menu header
            print(Storyboard.MENU_HEADER)

            # Print each menu item
            for menu_key in current_menu:

                # Prepare suffix to denote sub-menus by checking
                # whether the menu value is a dictionary
                menu_value = menu[menu_key]
                if isinstance(menu_value, dict) or isinstance(menu_value, OrderedDict):
                    submenu_suffix = Storyboard.SUBMENU_SUFFIX
                else:
                    submenu_suffix = ""

                # Determine maximum menu item length
                max_len = len(max(current_menu, key=len))

                # Print item index (starting from 1) and menu text
                print((" ({}) {:" + str(max_len+1) + "}{}").format(current_menu.index(menu_key) + 1, menu_key, submenu_suffix))

            # Display the training menu footer
            print(Storyboard.MENU_FOOTER)

            # Get the menu selection
            choice = raw_input(Storyboard.MENU_PROMPT)

            # Back menu choice (go up one level)
            if choice == Storyboard.BACK_CHOICE:
                self.clear_screen()

                # Check whether we are at the top level
                if current_menu == list(Content().training_content):
                    print(Storyboard.ERROR_TOP_LEVEL)
                else:
                    # Otherwise just return from the recursive call
                    return

            # Start Cooja choice
            elif choice == Storyboard.COOJA_CHOICE:
                self.clear_screen()
                print(Storyboard.INFO_START_COOJA)

                # Use helper class to start Cooja
                exit_status = CoojaManager().start_cooja()

                # In case of error print a message, otherwise clear the screen
                if exit_status != 0:
                    print(Storyboard.ERROR_COOJA_FAILED)
                else:
                    self.clear_screen()

            # Quit training choice
            elif choice == Storyboard.QUIT_CHOICE:
                raise QuitException("Quit")

            # Some actual training choice
            else:

                # Check whether the input is a number
                if choice.isdigit():
                    choice = int(choice)

                    # Check whether the choice is a valid menu item index
                    if self.is_in_menu_range(choice, current_menu):
                        self.clear_screen()

                        # Get the current menu value
                        menu_value = menu[current_menu[choice-1]]
                        if self.debug: print("DEBUG: Value of selected menu: '{}'".format(menu_value))

                        # Check whether the menu value is NOT a dictionary
                        if not isinstance(menu_value, dict) and not isinstance(menu_value, OrderedDict):

                            # Check whether the database directory exists
                            if not os.path.isdir(Storyboard.IOTRAIN_DATABASE_PATH):
                                print(Storyboard.ERROR_DATABASE_NOT_FOUND.format(Storyboard.IOTRAIN_DATABASE_PATH))
                                continue

                            # Retrieve the full path for the file specified in "menu_value"
                            if self.debug: print("DEBUG: Find full path for database file: '{}'...".format(menu_value))
                            file_path = self.find_file(Storyboard.IOTRAIN_DATABASE_PATH, menu_value)

                            # Check whether a corresponding file was actually found
                            if not file_path:
                                print(Storyboard.ERROR_FILE_NOT_LOCATED.format(menu_value))

                            # PDF files are opened via the webbrowser library
                            elif os.path.splitext(file_path)[1] == ".pdf":
                                if self.debug: print("DEBUG: Open PDF file: '{}'...".format(file_path))
                                # Make sure to add the "file://" prefix, or it will not work on macOS
                                # NOTE: There seems to be no way to catch errors in webbrowser.open()
                                webbrowser.open("file://" + file_path)

                            # CSC files are opened via a helper function
                            elif os.path.splitext(file_path)[1] == ".csc":
                                if self.debug: print("DEBUG: Open CSC file: '{}'...".format(file_path))
                                # Use helper class to open CSC file
                                exit_status = CoojaManager().open_csc_file(file_path)
                                # In case of error print a message, otherwise clear the screen
                                if exit_status != 0:
                                    print(Storyboard.ERROR_CSC_FAILED)
                                else:
                                    self.clear_screen()

                            # Otherwise display an error
                            else:
                                print(Storyboard.ERROR_UNKNOWN_FILE_TYPE.format(file_path))

                        else:
                            self.clear_screen()
                            self.show_menu(menu_value)
                    else:
                        self.clear_screen()
                        print(Storyboard.ERROR_INVALID_CHOICE.format(choice))

                # Otherwise just print an error
                else:
                    self.clear_screen()
                    print(Storyboard.ERROR_INVALID_INPUT.format(choice))

 # Class that defines a custom quit exception which indicates that the user wants to quit
 # This makes possible to exit from the nested recursive calls needed for menu navigation
class QuitException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
