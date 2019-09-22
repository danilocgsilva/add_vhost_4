import os

class Windows_Guesser:

    def __init__(self):
        self.possibles = [
            "C:\\wamp64\\bin\\apache\\apache2.4.37\\conf\\extra\\httpd-vhosts.conf",
            "D:\\wamp64\\bin\\apache\\apache2.4.37\\conf\\extra\\httpd-vhosts.conf"
        ]


    def guess(self):

        for candidate in self.possibles:
            if os.path.isfile(candidate):
                return candidate

        raise FileNotFoundError("There were not possible to guess the path for the virtual hosts entry.")
