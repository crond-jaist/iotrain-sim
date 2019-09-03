
#############################################################################
# Helper class for the IoTrain-Sim storyboard
#############################################################################

class Storyboard:

    #############################################################################
    # Generic constants

    # Program version
    IOTRAIN_SIM_VERSION = '0.1'

    # Separator constants
    SEPARATOR1 = '-------------------------------------------------------------------------'
    SEPARATOR2 = '========================================================================='
    SEPARATOR3 = '#########################################################################'


    #############################################################################
    # Path constants for 'rpl-collect' folder

    # IoTrain-Sim paths
    IOTRAIN_PATH = '/home/user/iotrain-sim/'
    IOTRAIN_DATABASE_PATH = IOTRAIN_PATH + 'database/'
    IOTRAIN_RPL_COLLECT_PATH = IOTRAIN_DATABASE_PATH + 'security_training/rpl-collect'
    IOTRAIN_RPL_COLLECT_BACKUP = IOTRAIN_RPL_COLLECT_PATH + '-iotrain_backup'

    # Contiki paths
    CONTIKI_RPL_COLLECT_PATH = '/home/user/contiki/examples/ipv6/rpl-collect'
    CONTIKI_RPL_COLLECT_BACKUP = CONTIKI_RPL_COLLECT_PATH + '-iotrain_backup'

    #############################################################################
    # Menu constants

    # Menu choices
    BACK_CHOICE = 'b'
    COOJA_CHOICE = 'c'
    QUIT_CHOICE = 'q'

    # Menu details
    MENU_HEADER = SEPARATOR2 + '\nTRAINING MENU\n' + SEPARATOR1
    MENU_FOOTER = SEPARATOR1
    MENU_PROMPT = "Enter your choice (or '{}' to go back, '{}' to start Cooja, '{}' to quit): ".format(BACK_CHOICE, COOJA_CHOICE, QUIT_CHOICE)
    SUBMENU_SUFFIX = "[>]"

    # Information messages
    INFO_START_COOJA = 'INFO: Starting Cooja...\n'
    INFO_QUIT_TRAINING = '\nINFO: Quit training...\n'

    # Error messages
    ERROR_COOJA_FAILED = 'ERROR: Cooja execution failed\n' 
    ERROR_CSC_FAILED = 'ERROR: CSC file execution failed\n' 
    ERROR_TOP_LEVEL = 'ERROR: Already at top level\n'
    ERROR_INVALID_CHOICE = "ERROR: Invalid choice: '{}'\n"
    ERROR_INVALID_INPUT = "ERROR: Invalid input: '{}'\n"
    ERROR_DATABASE_NOT_FOUND = ("ERROR: Database directory does not exist: '{}'\n" +
                                "       Check the file 'code/storyboard.py' for configuration errors (e.g., is IOTRAIN_PATH correct?)\n")
    ERROR_FILE_NOT_LOCATED = ("ERROR: File corresponding to menu choice could not be located: '{}'\n" +
                              "       Check the file 'code/contents.py' for specification errors\n")
    ERROR_UNKNOWN_FILE_TYPE = "ERROR: Unknown type for file: '{}'\n"
