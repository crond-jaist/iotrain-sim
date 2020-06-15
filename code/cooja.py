
#############################################################################
# Helper class for managing Cooja
#############################################################################

# Standard library imports
import os
import subprocess
import time

# Local imports
from storyboard import Storyboard

# Cooja manager class
class CoojaManager():

    # Run a process and detect error status immediately after launch
    def run_process(self, command_list, working_dir):
        try:
            process = subprocess.Popen(command_list, cwd=working_dir)
            # Wait to capture (some) execution errors, but without guarantees
            for _ in range(5):
                time.sleep(1)
                poll_result = process.poll()
                if poll_result: # Process ended => return exit code
                    return poll_result
            # Process is still running => assume no error
            return 0
        except OSError as error:
            print("ERROR: " + str(error))
            return 255

    # Use the command 'ant run' to start Cooja
    def start_cooja(self):
        # Run command "ant run" after changing to CONTIKI_COOJA_PATH directory
        return self.run_process(["ant", "run"], Storyboard.CONTIKI_COOJA_PATH)

    # Open CSC files via Cooja
    def open_csc_file(self, file_path):

        # Get the directory where the file is located
        dir_path = os.path.dirname(file_path)

        # Get the actual file name
        file_name=os.path.basename(file_path)

        # Run command "make TARGET=cooja FILE_NAME" after changing to DIR_PATH directory
        return self.run_process(["make", "TARGET=cooja", file_name], dir_path)
