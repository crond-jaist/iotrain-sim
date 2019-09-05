
#############################################################################
# Display the training menus of IoTrain-Sim
#############################################################################

# Standard library imports
import os
import webbrowser
from collections import OrderedDict

# Local imports
from content import Content
from cooja import CoojaManager
from storyboard import Storyboard

# Class that displays training menus
class MenuDisplay(object):

    # Enable debug messages
    debug = False

    # Class variable needed to return a value from 'find_file'
    file_path = None

    # Find a file's full path based on the file name
    # NOTE: Only the last matching path can be retrieved from 'self.file_path'
    def find_file(self, database_path, filename):

        # Try to find item in the database directory structure
        for item in os.listdir(database_path):
            item_path = os.path.join(database_path, item)

            # For directories, we do recursive search
            if os.path.isdir(item_path):
                self.find_file(item_path, filename)

            # For files, we check whether the item matches
            elif os.path.isfile(item_path):
                if filename == item:
                    # On match, assign the found value to class variable
                    self.file_path = item_path

    # Verify whether a file has a certain extension (argument must include the separating dot)
    def check_extension(self, filename, extension):
        if os.path.splitext(filename)[1] == extension:
            return True
        else:
            return False

    # Check whether a choice is in the menu range
    def is_in_menu_range(self, choice, menu):
        if choice > 0 and choice <= len(menu):
            return True
        else:
            return False

    # Clear the screen when displaying CLI menu
    def clear_screen(self):
        os.system('clear')

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

                            # Retrieve the full path for the file specified in 'menu_value' and 
                            # store it in the class variable 'self.file_path'
                            if self.debug: print("DEBUG: Find full path for database file: '{}'...".format(menu_value))
                            self.find_file(Storyboard.IOTRAIN_DATABASE_PATH, menu_value)

                            # Check whether a corresponding file was actually found
                            if not self.file_path:
                                print(Storyboard.ERROR_FILE_NOT_LOCATED.format(menu_value))

                            # PDF files are opened via the webbrowser library
                            elif self.check_extension(self.file_path, '.pdf'):
                                if self.debug: print("DEBUG: Open PDF file: '{}'...".format(self.file_path))
                                # Make sure to add the 'file://' prefix, or it will not work on macOS
                                # TODO: Is there any way to check if the command was successful or not?
                                webbrowser.open('file://' + self.file_path)

                            # CSC files are opened via a helper function
                            elif self.check_extension(self.file_path, '.csc'):

                                # Use helper class to start Cooja
                                if self.debug: print("DEBUG: Open CSC file: '{}'...".format(self.file_path))
                                exit_status = CoojaManager().open_csc_file(self.file_path)
                                # In case of error print a message, otherwise clear the screen
                                if exit_status != 0:
                                    print(Storyboard.ERROR_CSC_FAILED)
                                else:
                                    self.clear_screen()

                            # Otherwise display an error
                            else:
                                print(Storyboard.ERROR_UNKNOWN_FILE_TYPE.format(self.file_path))

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
 # This makes possible to exit from the nested recursive calls needed foe menu navigation
class QuitException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
