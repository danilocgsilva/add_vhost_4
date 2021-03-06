from install_assets.files_folder import files, folders
from install_assets.Nt_Paths import Nt_Paths
from install_assets.Posix_Paths import Posix_Paths
import os
import shutil
import stat

class Installer:

    def __init__(self):

        if os.name == 'nt':
            paths = Nt_Paths()
        elif os.name == 'posix':
            paths = Posix_Paths()
        else:
            raise Exception("The os name is not known...")

        self.base_physical_app_folder = paths.get_base_physical_app_folders()
        self.os_entry = paths.get_os_entry()
        self.error_messages = []


    def check_write_permission(self) -> bool:
        try:
            open(self.os_entry, "w")
            os.remove(self.os_entry)
        except PermissionError:
            self.error_messages.append("Can't write in the entry execution path.")

        if len(self.error_messages) == 0:
            return True
        return False


    def write_os_entry(self):
        file_resource = open(self.os_entry, "w")
        file_resource.write("#!/bin/bash\n")
        file_resource.write("\n")
        file_resource.write("python3 " + self.base_physical_app_folder + " $1\n")


    def __forge_destiny__(self, relative_file_path):
        return os.path.join(self.base_physical_app_folder, relative_file_path)


    def copy_files(self):

        self.__custom_makedirs__(self.base_physical_app_folder)

        for folder in folders:
            self.__custom_makedirs__(os.path.join(self.base_physical_app_folder, folder))

        for file in files:
            if not os.path.exists(os.path.join(self.base_physical_app_folder, file)):
                shutil.copy(
                    file,
                    os.path.join(self.base_physical_app_folder, file)
                )
                print("The file " + file + " has been copied to the destiny.")
            else:
                os.remove(os.path.join(self.base_physical_app_folder, file))
                shutil.copy(
                    file,
                    os.path.join(self.base_physical_app_folder, file)
                )
                print('The file ' + file + ' has been replaced.')


    def get_error_messages(self) -> str:
        error_message = ""
        for message in self.error_messages:
            error_message += "\n" + message
        return error_message


    def __custom_makedirs__(self, folder: str):
        if os.path.exists(folder):
            print("The folder " + folder + " already exists!")
        else:
            os.makedirs(folder)
            print("The folder " + folder + " has been created.")


    def set_execution_permission(self):
        if os.name == 'posix':
            os.chmod(self.os_entry, stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
            print("The entry point for adding vhost has setted the execution permission.")
