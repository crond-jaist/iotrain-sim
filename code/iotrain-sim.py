#! /usr/bin/env python

#############################################################################
# Main program file for the IoTrain-Sim training system
#############################################################################

# Standard library imports
import os
import time

# Local imports
from menu import MenuDisplay
from files import FileManager
from storyboard import Storyboard

# Print banner
print(Storyboard.SEPARATOR3)
print(Storyboard.STARTUP_BANNER.format(Storyboard.IOTRAIN_SIM_VERSION))
print(Storyboard.SEPARATOR3)

# Prepare the Contiki environment
print(Storyboard.STARTUP_COPY.format(Storyboard.CONTIKI_PATH))
FileManager().copy_dir_struct(Storyboard.IOTRAIN_CONTIKI_PATH, Storyboard.CONTIKI_PATH)

# Show prompt before displaying the training menu
#raw_input(Storyboard.READY_PROMPT)
print(Storyboard.READY_MESSAGE)
time.sleep(2)

# Display the top training menu
MenuDisplay().display_top_menu()

# Cleanup the Contiki environment
print(Storyboard.SHUTDOWN_CLEANUP)
FileManager().delete_dir_struct(Storyboard.IOTRAIN_CONTIKI_PATH, Storyboard.CONTIKI_PATH)
