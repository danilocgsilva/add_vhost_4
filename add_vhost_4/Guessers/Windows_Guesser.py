import os

class Windows_Guesser:

    def __init__(self):
        self.possibles = [
            "C:\\wamp64\\bin\\apache\\apache2.4.37\\conf\\extra\\httpd-vhosts.conf",
            "D:\\wamp64\\bin\\apache\\apache2.4.37\\conf\\extra\\httpd-vhosts.conf"
        ]
        self.httpd_entries_address = None


    def guess(self):

        for candidate in self.possibles:
            if os.path.isfile(candidate):
                self.httpd_entries_address = candidate
                return self.httpd_entries_address

        raise FileNotFoundError("There were not possible to guess the path for the virtual hosts entry.")


    def get_base_physical_path(self):
        return os.path.join(self.httpd_entries_address[0:9], "www")
