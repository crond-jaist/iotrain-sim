
#############################################################################
# Helper class for managing folders
#############################################################################

# Standard library imports
import shutil

# Local imports
from storyboard import Storyboard

# Folder manager class
class FolderManager():

    # Backup IoTrain-Sim and Contiki 'rpl-collect' folders
    def backup_rpl_collect(self):
        #shutil.copytree(self._iotrain_path, self._iotrain_backup_path)
        shutil.copytree(Storyboard.CONTIKI_RPL_COLLECT_PATH, Storyboard.CONTIKI_RPL_COLLECT_BACKUP)

    # Use IoTrain-Sim 'rpl-collect' folder to overwrite the Contiki one
    def copy_rpl_collect(self):
        shutil.rmtree(Storyboard.CONTIKI_RPL_COLLECT_PATH)
        shutil.copytree(Storyboard.IOTRAIN_RPL_COLLECT_PATH, Storyboard.CONTIKI_RPL_COLLECT_PATH)

    # Restore all changed folders from backup
    def restore_rpl_collect(self):
        shutil.rmtree(Storyboard.CONTIKI_RPL_COLLECT_PATH)
        #shutil.rmtree(self._iotrain_backup_path)
        shutil.copytree(Storyboard.CONTIKI_RPL_COLLECT_BACKUP, Storyboard.CONTIKI_RPL_COLLECT_PATH)
        shutil.rmtree(Storyboard.CONTIKI_RPL_COLLECT_BACKUP)
