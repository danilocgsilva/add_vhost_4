import os

class Posix_Guesser:
    def __init__(self):
        self.possibles = [
            '/Applications/XAMPP/xamppfiles/etc/extra/httpd-vhosts.conf',
            '/etc/httpd/conf/httpd.conf',
        ]
        self.httpd_entries_address = None


    def guess_vhost_entries(self):

        for candidate in self.possibles:
            if os.path.isfile(candidate):
                self.httpd_entries_address = candidate
                return candidate

        raise FileNotFoundError("There were not possible to guess the path for the virtual hosts entry.")


    def get_base_physical_path(self):
        return '/var/www/html'


    def guess_debian_like_vhost_file(self, desired_name: str) -> str:
        return os.sep + os.path.join('etc', 'apache2', 'sites-available', desired_name)

