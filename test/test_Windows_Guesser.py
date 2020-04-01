import unittest
import sys
sys.path.append("..")
from add_vhost_4.Guessers.Windows_Guesser import Windows_Guesser

class test_Windows_Guesser(unittest.TestCase):

    def test_can_search_apache_folder_without_provided_version(self):
        windows_guesser = Windows_Guesser()
        possibility_whithout_version = "C:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"

if __name__ == '__main__':
    unittest.main()
