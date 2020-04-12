import os
import re

class Windows_Guesser:

    def __init__(self):
        self.drive = "C"
        self.wamp_base = "wamp64"
        self.vhost_configuration_path = "bin\\apache\\apache2.4.41\\conf\\extra\\httpd-vhosts.conf"
        self.physical_www_path = "www"


    def guess_vhost_entries(self):
        return self.drive + ":" + os.sep + self.wamp_base + os.sep + self.vhost_configuration_path


    def get_base_physical_path(self):
        return self.drive + ":" + os.sep + self.wamp_base + os.sep + self.physical_www_path


    def get_full_base_wamp_path(self):
        return self.drive + ":" + os.sep + self.wamp_base
