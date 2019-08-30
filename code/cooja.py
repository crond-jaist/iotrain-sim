
#############################################################################
# Helper class for managing Cooja
#############################################################################

# Standard library imports
import os

# Local imports
from storyboard import Storyboard

# Cooja manager class
class CoojaManager():

    # Use the command 'ant run' to start Cooja
    def start_cooja(self):
        # TODO: Change to subprocess.call() or Popen() with cwd option to avoid a
        # potential security vulnerability
        exit_status = os.system('cd /home/user/contiki/tools/cooja/ && ant run')
        return exit_status

    # Open CSC files via Cooja
    def open_csc_file(self, file_path):

        # Get the directory where the file is located
        dir_path = os.path.dirname(file_path)

        # Get the actual file name
        file_name=os.path.basename(file_path)

        # Prepare and execute command
        command = 'make TARGET=cooja ' + file_name
        os.chdir(dir_path)
        # TODO: Change to subprocess.call() or Popen() with cwd option to avoid a
        # potential security vulnerability
        exit_status = os.system(command)
        return exit_status
