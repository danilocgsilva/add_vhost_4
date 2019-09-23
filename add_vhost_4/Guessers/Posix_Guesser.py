import os

class Posix_Guesser:
    def __init__(self):
        self.possibles = [
            '/Applications/XAMPP/xamppfiles/etc/extra/httpd-vhosts.conf',
            '/etc/httpd/conf/httpd.conf',
        ]

    def guess(self):

        for candidate in self.possibles:
            if os.path.isfile(candidate):
                print(candidate)
                return candidate

        raise FileNotFoundError("There were not possible to guess the path for the virtual hosts entry.")

