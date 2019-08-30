#! /usr/bin/env python

#############################################################################
# Main program file for the IoTrain-Sim training system
#############################################################################

# Standard library imports
import os

# Local imports
from menu import MenuDisplay
from folders import FolderManager
from storyboard import Storyboard

# Print banner
print(Storyboard.SEPARATOR3)
print('IoTrain-Sim v{}: IoT Training System Using the Cooja Network Simulator'.format(Storyboard.IOTRAIN_SIM_VERSION))
print(Storyboard.SEPARATOR3)

# Configure the environment
#print('* Configure the simulation environment...')
#folder_manager = FolderManager()
#folder_manager.backup_rpl_collect()
#folder_manager.copy_rpl_collect()

# Display the menus 
#print('* IoTrain-Sim is ready to start the training')
#print(Storyboard.SEPARATOR2)
MenuDisplay().display_menu_first()

#print('* Restore the default environment...')
#folder_manager.restore_rpl_collect()
