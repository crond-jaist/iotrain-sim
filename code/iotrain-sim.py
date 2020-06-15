#! /usr/bin/env python

#############################################################################
# Main program file for the IoTrain-Sim training system
#############################################################################

# Standard library imports
import os
import time
import sys
import getopt

# Local imports
from cli import CLI
from gui import GUI
from files import FileManager
from storyboard import Storyboard

#############################################################################
# Functions
#############################################################################

# Print usage information
def usage():
    print "\nUSAGE: iotrain-sim.py [options]\n"
    print "OPTIONS:"
    print "-h, --help       Display this help message and exit"
    print "-c, --cli        Use command-line user interface"
    print "-g, --gui        Use graphical user interface (default)\n"

#############################################################################
# Main program
#############################################################################
def main(args):

    # Program parameters and their default values
    use_cli = False

    # Print banner
    print(Storyboard.SEPARATOR3)
    print(Storyboard.STARTUP_BANNER.format(Storyboard.IOTRAIN_SIM_VERSION))
    print(Storyboard.SEPARATOR3)

    # Parse command line arguments
    try:
        # Make sure to add ':' for short-form and '=' for long-form options that require an argument
        opts, trailing_args = getopt.getopt(args, "hcg", ["help", "cli", "gui"])
    except getopt.GetoptError as err:
        print(Storyboard.ERROR_CMD_LINE_ARGS.format(str(err)))
        usage()
        sys.exit(1)

    for opt, _ in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif opt in ("-c", "--cli"):
            use_cli = True
        elif opt in ("-g", "--gui"):
            use_cli = False
        else:
            # Nothing to be done on else, since unrecognized options are caught by
            # the getopt.GetoptError exception above
            pass

    if trailing_args:
        print(Storyboard.ERROR_TRAILING_ARGS.format(trailing_args))
        usage()
        sys.exit(2)

    # Make sure the database directory exists
    if not os.path.isdir(Storyboard.IOTRAIN_DATABASE_PATH):
        print(Storyboard.ERROR_DATABASE_NOT_FOUND.format(Storyboard.IOTRAIN_DATABASE_PATH))
        sys.exit(3)

    # Prepare the Contiki environment
    print(Storyboard.INFO_COPY_BIN)
    if not FileManager().copy_hierarchy(Storyboard.IOTRAIN_CONTIKI_PATH, Storyboard.CONTIKI_PATH):
        print(Storyboard.ERROR_FAILED_COPY_BIN)
        sys.exit(4)

    # Display the appropriate interface
    if use_cli:
        # Display the top CLI training menu
        print(Storyboard.INFO_START_CLI)
        time.sleep(1) # Used for debugging purposes, to make sure messages are displayed
        CLI().display_top_menu()
    else:
        # Display the top GUI training
        print(Storyboard.INFO_START_GUI)
        GUI().start()

    # Cleanup the Contiki environment
    print(Storyboard.INFO_REMOVE_BIN)
    if not FileManager().delete_hierarchy(Storyboard.IOTRAIN_CONTIKI_PATH, Storyboard.CONTIKI_PATH):
        sys.exit(5)

#############################################################################
# Run program
if __name__ == "__main__":
    main(sys.argv[1:])
