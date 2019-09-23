import os

class Installer:

    def __init__(self):
        self.base_physical_app_folder = "/opt/danilocgsilva_add_vhost"


    def write_os_entry(self):
        os_entry_name = os.path.join('usr', 'local', 'bin')
        file_resource = open(os_entry_name)
        file_resource.write("#!/bin/bash")
        file_resource.write("")
        file_resource.write("python3 " + self.base_physical_app_folder)
