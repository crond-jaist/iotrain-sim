
#############################################################################
# Helper class for managing files
#############################################################################

# Standard library imports
import os
import distutils.dir_util
from distutils.errors import DistutilsFileError

# Local imports
from storyboard import Storyboard

# File manager class
class FileManager():

    debug = False

    # Copy the file and subdirectory structure in the directory 'src_dir'
    # to 'dst_dir' (new subdirectories are created if needed)
    def copy_hierarchy(self, src_dir, dst_dir):

        if self.debug: print("DEBUG: Copying all files in '{}' to '{}'...".format(src_dir, dst_dir))
        try:
            distutils.dir_util.copy_tree(src_dir, dst_dir)
            return True
        except DistutilsFileError as error:
            print("ERROR: " + str(error))
            return False

    # Delete the files structure present in the directory 'src_dir' from
    # 'dst_dir' (other files in 'dst_dir' and any directories that became
    # empty are not deleted)
    def delete_hierarchy(self, src_dir, dst_dir):

        if self.debug: print("DEBUG: Deleting all files in '{}' from '{}'...".format(src_dir, dst_dir))

        # Build a list of files in the source directory
        file_list = []
        for home, _, files in os.walk(src_dir):
            for full_name in files:
                file_list.append(os.path.join(home, full_name))
        if self.debug: print("DEBUG: Files in source directory: {}".format(file_list))

        no_error_encountered = True
        # Iterate over the files in the source directory
        for file_name in file_list:

            # Build the name of the corresponding file in the destination
            # directory
            dst_file_name = file_name.replace(src_dir, dst_dir)

            # Actually delete the file
            if self.debug: print("DEBUG: File to be deleted: {}".format(dst_file_name))
            try:
                os.remove(dst_file_name)
            except OSError as error:
                print("ERROR: " + str(error))
                no_error_encountered = False

        return no_error_encountered
