from install_assets.files_folder import files, folders
import os
import shutil

class Installer:

    def __init__(self):
        self.base_physical_app_folder = "/opt/danilocgsilva_add_vhost"
        self.os_entry = os.sep + os.path.join('usr', 'local', 'bin', 'add_vhost')
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
        file_resource.write("python3 " + self.base_physical_app_folder + "\n")


    def __forge_destiny__(self, relative_file_path):
        return os.path.join(self.base_physical_app_folder, relative_file_path)


    def copy_files(self):

        self.__custom_makedirs__(self.base_physical_app_folder)

        for folder in folders:

            #if not os.path.isdir(os.path.join(self.base_physical_app_folder, folder)):
            #    os.makedirs(
            #        os.path.join(self.base_physical_app_folder, folder)
            #    )
            #    print('The folder ' + folder + ' has been created.')
            #else:
            #    print('The folder ' + folder + ' already existed in the destiny.')

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


    def get_error_messages(self):
        return self.error_messages


    def __custom_makedirs__(self, folder: str):
        if os.path.exists(folder):
            print("The folder " + folder + " already exists!")
        else:
            os.makedirs(folder)
            print("The folder " + folder + " has been created.")
