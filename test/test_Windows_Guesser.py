import unittest
import sys
sys.path.append("..")
from add_vhost_4.Guessers.Windows_Guesser import Windows_Guesser

class test_Windows_Guesser(unittest.TestCase):

    def test_can_search_no_asterisk_apache_version(self):
        windows_guesser = Windows_Guesser()
        file_candidate_no_asterisk = "C:\\wamp64\\bin\\apache\\apache2.4.37\\conf\\extra\\httpd-vhosts.conf"
        candidate_version = windows_guesser.search_version(file_candidate_no_asterisk)
        self.assertEqual(file_candidate_no_asterisk, candidate_version)

    
    def test_can_search_correct_apache_version_with_asterisk(self):
        windows_guesser = Windows_Guesser()
        file_candidate_asterisk = "C:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"
        file_list = ["apache2.4.39"]
        windows_guesser.add_file_list(file_list)
        correct_path = "C:\\wamp64\\bin\\apache\\apache2.4.39\\conf\\extra\\httpd-vhosts.conf"
        guessed_path = windows_guesser.search_version(file_candidate_asterisk)
        self.assertEqual(correct_path, guessed_path)


if __name__ == '__main__':
    unittest.main()
