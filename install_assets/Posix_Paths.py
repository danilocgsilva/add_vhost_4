import os

class Posix_Paths:

    def get_base_physical_app_folders(self):
        return "/opt/danilocgsilva_add_vhost"

    def get_os_entry(self):
        return os.sep + os.path.join('usr', 'local', 'bin', 'add_vhost')
