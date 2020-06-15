
#############################################################################
# Helper class for the IoTrain-Sim storyboard
#############################################################################

class Storyboard:

    #############################################################################
    # Generic constants

    # Program version
    IOTRAIN_SIM_VERSION = "1.0"

    # Separator constants
    SEPARATOR1 = "-------------------------------------------------------------------------"
    SEPARATOR2 = "========================================================================="
    SEPARATOR3 = "#########################################################################"

    #############################################################################
    # Path constants for IoTrain-Sim folders

    # Global paths
    IOTRAIN_PATH = "/home/user/iotrain-sim/"
    CONTIKI_PATH = "/home/user/contiki/"

    # Relative paths
    IOTRAIN_DATABASE_PATH = IOTRAIN_PATH + "database/"
    IOTRAIN_FIGURES_PATH = IOTRAIN_PATH + "figures/"
    IOTRAIN_CONTIKI_PATH = IOTRAIN_DATABASE_PATH + "contiki/"
    CONTIKI_COOJA_PATH = CONTIKI_PATH + "tools/cooja/"

    #############################################################################
    # CLI constants

    # Menu choices
    BACK_CHOICE = "b"
    COOJA_CHOICE = "c"
    QUIT_CHOICE = "q"

    # Menu details
    MENU_HEADER = SEPARATOR2 + "\nTRAINING MENU\n" + SEPARATOR1
    MENU_FOOTER = SEPARATOR1
    MENU_PROMPT = "Enter your choice (or '{}' to go back, '{}' to start Cooja, '{}' to quit): ".format(BACK_CHOICE, COOJA_CHOICE, QUIT_CHOICE)
    SUBMENU_SUFFIX = "[>]"

   #############################################################################
    # GUI constants

    # Button labels
    BUTTON_EXPAND_ALL = "Expand All"
    BUTTON_COLLAPSE_ALL = "Colapse All"
    BUTTON_START_COOJA = "Start Cooja"
    BUTTON_QUIT = "Quit"

    # Treeview items
    TAG_CATEGORY = "category"
    HEADING_NAME = "Training Content"

    #############################################################################
    # Mesage constants

    # General messages
    STARTUP_BANNER = "IoTrain-Sim v{}: IoT Training System Using the Cooja Network Simulator"
    INFO_COPY_BIN = "INFO: Copy precompiled IoTrain-Sim training binaries to Contiki..."
    INFO_START_CLI = "INFO: Start CLI interface..."
    INFO_START_GUI = "INFO: Start GUI interface..."
    INFO_REMOVE_BIN = "INFO: Remove precompiled IoTrain-Sim training binaries from Contiki..."
    INFO_START_COOJA = "INFO: Start Cooja..."

    # Error messages
    # (a GUI suffix means the message is intended for use in GUI)
    ERROR_CMD_LINE_ARGS = "ERROR: Command-line argument error: '{}' => abort execution\n"
    ERROR_TRAILING_ARGS = "ERROR: Unrecognized trailing arguments: '{}' => abort execution\n"
    ERROR_FAILED_COPY_BIN = "ERROR: Failed to copy precompiled training binaries => abort execution\n "
    ERROR_COOJA_FAILED = "ERROR: Cooja execution failed\n"
    ERROR_COOJA_FAILED_GUI = "Cooja execution failed"
    ERROR_CSC_FAILED = "ERROR: CSC file execution failed\n"
    ERROR_CSC_FAILED_GUI = "CSC file execution failed"
    ERROR_COOJA_DIALOG_TITLE_GUI = "Cooja Error"

    ERROR_TOP_LEVEL = "ERROR: Already at top level\n"
    ERROR_INVALID_CHOICE = "ERROR: Invalid choice: '{}'\n"
    ERROR_INVALID_INPUT = "ERROR: Invalid input: '{}'\n"

    ERROR_DATABASE_NOT_FOUND = ("ERROR: Database directory does not exist: '{}'\n" +
                                "       Check 'code/storyboard.py' for errors: is IOTRAIN_PATH correct?\n")
    ERROR_DATABASE_NOT_FOUND_GUI = ("Database directory does not exist:\n\t{}\n" +
                                "Check 'code/storyboard.py' for errors: is IOTRAIN_PATH correct?\n")
    ERROR_FILE_NOT_LOCATED = ("ERROR: File could not be located in database: '{}'\n" +
                              "       Check 'code/contents.py' for errors\n")
    ERROR_FILE_NOT_LOCATED_GUI = ("File could not be located in database:\n\t{}\n" +
                              "Check 'code/contents.py' for errors.")
    ERROR_UNKNOWN_FILE_TYPE = ("ERROR: Unknown type for file: '{}'\n"+
                              "       Check 'code/contents.py' for errors\n")
    ERROR_UNKNOWN_FILE_TYPE_GUI = ("Unknown type for file:\n\t{}\n" +
                              "Check 'code/contents.py' for errors.")
    ERROR_MAIN_DIALOG_TITLE_GUI = "IoTrain-Sim Error"
