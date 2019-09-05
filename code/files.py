
#############################################################################
# Helper class for managing files
#############################################################################

# Standard library imports
import os
import distutils.dir_util

# Local imports
from storyboard import Storyboard

# File manager class
class FileManager():

    debug = False

    # Copy the file and subdirectory structure in the directory 'src_dir'
    # to 'dst_dir' (new subdirectories are created if needed)
    def copy_dir_struct(self, src_dir, dst_dir):

        if self.debug: print("DEBUG: Copying all files in '{}' to '{}'...".format(src_dir, dst_dir))
        distutils.dir_util.copy_tree(src_dir, dst_dir)

    # Build recursively a list with all the files in a directory and its
    # subdirectories
    def build_file_list(self, dir_name):

        # Check if the argument is a directory
        if not os.path.isdir(dir_name):
            print("ERROR: Argument is not a directory name: '{}'".format(dir_name))
            return None

        # Get list of files and subdirectory names
        file_list = os.listdir(dir_name)
        file_list_all = []

        # Iterate over all the elements
        for item in file_list:

            # Build item path
            item_path = os.path.join(dir_name, item)

            # If item is a subdirectory, get the list of files in it
            if os.path.isdir(item_path):
                file_list_all = file_list_all + self.build_file_list(item_path)
            # Otherwise, add the item to the result list
            else:
                file_list_all.append(item_path)

        return file_list_all

    # Delete the files structure present in the directory 'src_dir' from
    # 'dst_dir' (other files in 'dst_dir' and any directories that became
    # empty are not deleted)
    def delete_dir_struct(self, src_dir, dst_dir):

        if self.debug: print("DEBUG: Deleting all files in '{}' from '{}'...".format(src_dir, dst_dir))

        # Build a list of files in the source directory
        file_list = self.build_file_list(src_dir)
        if self.debug: print("DEBUG: Files in source directory: {}".format(file_list))

        # Iterate over the files in the source directory
        for file_name in file_list:

            # Build the name of the corresponding file in the destination
            # directory
            dst_file_name = file_name.replace(src_dir, dst_dir)

            # Actually delete the file
            if self.debug: print("DEBUG: File to be deleted: {}".format(dst_file_name))
            os.remove(dst_file_name)
