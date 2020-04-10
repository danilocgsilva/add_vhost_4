import unittest
import sys
import os
sys.path.append("..")
from add_vhost_4.Guessers.Windows_Guesser import Windows_Guesser

class test_Windows_Guesser(unittest.TestCase):

    def __init__(self, *args, **kwargs):

        super(test_Windows_Guesser, self).__init__(*args, **kwargs)
        self.windows_guesser = Windows_Guesser()

    def test_can_search_no_asterisk_apache_version(self):
        file_candidate_no_asterisk = "C:\\wamp64\\bin\\apache\\apache2.4.37\\conf\\extra\\httpd-vhosts.conf"
        candidate_version = self.windows_guesser.search_version(file_candidate_no_asterisk)
        self.assertEqual(file_candidate_no_asterisk, candidate_version)

    
    def test_can_search_correct_apache_version_with_asterisk(self):
        file_candidate_asterisk = "C:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"
        file_list = ["apache2.4.39"]
        self.windows_guesser.add_file_list(file_list)
        correct_path = "C:\\wamp64\\bin\\apache\\apache2.4.39\\conf\\extra\\httpd-vhosts.conf"
        guessed_path = self.windows_guesser.search_version(file_candidate_asterisk)
        self.assertEqual(correct_path, guessed_path)


    def test_can_search_correct_apache_version_with_asterisk_different_string(self):
        file_candidate_asterisk = "C:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"
        file_list = ["apache2.4.41"]
        self.windows_guesser.add_file_list(file_list)
        correct_path = "C:\\wamp64\\bin\\apache\\apache2.4.41\\conf\\extra\\httpd-vhosts.conf"
        guessed_path = self.windows_guesser.search_version(file_candidate_asterisk)
        self.assertEqual(correct_path, guessed_path)


    def test_generate_path_string(self):
        members = ["c", "Wamp", "bin", "apache2"]
        expected_path = os.path.join(members[0], members[1], members[2], members[3])
        generated_path = self.windows_guesser.generate_path_string_from_list(members)
        self.assertEqual(expected_path, generated_path)


if __name__ == '__main__':
    unittest.main()
