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


    def test_get_prefix_path_with_path_parts_and_generic_apache(self):
        generic_apache_path = "C:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"
        self.windows_guesser.set_path_parts(generic_apache_path)
        self.windows_guesser.set_generic_apache_path(generic_apache_path)
        self.windows_guesser.sepparate_preffix_suffix_from_generic_path()

        expected_string = "C:\\wamp64\\bin\\apache"
        guessed_prefix = self.windows_guesser.get_prefix_path_from_generic_path()

        self.assertEqual(expected_string, guessed_prefix)


    def test_guess_vhost_entries_with_path_parts_and_generic_apache(self):
        generic_apache_path = "C:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"
        self.windows_guesser.set_path_parts(generic_apache_path)
        self.windows_guesser.set_generic_apache_path(generic_apache_path)
        self.windows_guesser.sepparate_preffix_suffix_from_generic_path()

        apache_version_list = [ "apache2.4.29" ]
        self.windows_guesser.add_file_list(apache_version_list)

        expected_result = "C:\\wamp64\\bin\\apache\\apache2.4.29\\conf\\extra\\httpd-vhosts.conf"
        guessed_string = self.windows_guesser.guess_vhost_entries()

        self.assertEqual(expected_result, guessed_string)


    def test_search_version_with_path_parts_and_generic_apache(self):
        generic_apache_path = "D:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"
        self.windows_guesser.set_path_parts(generic_apache_path)
        self.windows_guesser.set_generic_apache_path(generic_apache_path)
        self.windows_guesser.sepparate_preffix_suffix_from_generic_path()

        apache_version_list = [ "apache2.4.28" ]
        self.windows_guesser.add_file_list(apache_version_list)

        expected = "D:\\wamp64\\bin\\apache\\apache2.4.28\\conf\\extra\\httpd-vhosts.conf"
        guessed_path = self.windows_guesser.search_version(generic_apache_path)

        self.assertEqual(expected, guessed_path)


    def test_search_version_asterisk_with_path_parts_and_generic_apache(self):
        generic_apache_path = "D:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"
        self.windows_guesser.set_path_parts(generic_apache_path)
        self.windows_guesser.set_generic_apache_path(generic_apache_path)
        self.windows_guesser.sepparate_preffix_suffix_from_generic_path()

        apache_version_list = [ "apache2.4.34" ]
        self.windows_guesser.add_file_list(apache_version_list)

        expected = "D:\\wamp64\\bin\\apache\\apache2.4.28\\conf\\extra\\httpd-vhosts.conf"
        guessed_path = self.windows_guesser.search_version_asterisk()

        self.assertEqual(expected, guessed_path)


    def test_get_prefix_path_with_path_parts_and_generic_apache_d_drive(self):
        generic_apache_path = "D:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"
        self.windows_guesser.set_path_parts(generic_apache_path)
        self.windows_guesser.set_generic_apache_path(generic_apache_path)
        self.windows_guesser.sepparate_preffix_suffix_from_generic_path()

        expected_string = "D:\\wamp64\\bin\\apache"
        guessed_prefix = self.windows_guesser.get_prefix_path_from_generic_path()

        self.assertEqual(expected_string, guessed_prefix)


    def test_generate_path_string(self):
        members = ["c", "Wamp", "bin", "apache2"]
        expected_path = os.path.join(members[0], members[1], members[2], members[3])
        generated_path = self.windows_guesser.generate_path_string_from_list(members)
        self.assertEqual(expected_path, generated_path)


    def test_guess_vhost_entries(self):

        generic_apache_path = "C:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"
        self.windows_guesser.set_generic_apache_path(generic_apache_path)

        apache_version_list_results = [ "apache2.4.33" ]
        self.windows_guesser.add_file_list(apache_version_list_results)

        guessed_vhost_path = self.windows_guesser.guess_vhost_entries()
        correct_file_path = "C:\\wamp64\\bin\\apache\\apache2.4.33\\conf\\extra\\httpd-vhosts.conf"

        self.assertEqual(correct_file_path, guessed_vhost_path)


    def test_guess_vhost_entries_2(self):

        generic_apache_path = "C:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"
        self.windows_guesser.set_generic_apache_path(generic_apache_path)

        apache_version_list_results = [ "apache2.4.21" ]
        self.windows_guesser.add_file_list(apache_version_list_results)

        guessed_vhost_path = self.windows_guesser.guess_vhost_entries()
        correct_file_path = "C:\\wamp64\\bin\\apache\\apache2.4.21\\conf\\extra\\httpd-vhosts.conf"

        self.assertEqual(correct_file_path, guessed_vhost_path)


    def test_get_prefix_path_from_generic_path(self):

        generic_apache_path = "C:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"
        self.windows_guesser.set_path_parts(generic_apache_path)
        self.windows_guesser.sepparate_preffix_suffix_from_generic_path()

        expected_result = "C:\\wamp64\\bin\\apache"
        prefix_result = self.windows_guesser.get_prefix_path_from_generic_path()

        self.assertEqual(expected_result, prefix_result)


    def test_get_prefix_path_from_generic_path_d_drive(self):

        generic_apache_path = "D:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"
        self.windows_guesser.set_path_parts(generic_apache_path)
        self.windows_guesser.sepparate_preffix_suffix_from_generic_path()

        expected_result = "D:\\wamp64\\bin\\apache"
        prefix_result = self.windows_guesser.get_prefix_path_from_generic_path()

        self.assertEqual(expected_result, prefix_result)


    def test_get_prefix_path_from_generic_path_with_set_generic_apache_path(self):

        generic_apache_path = "D:\\wamp64\\bin\\apache\\apache2.4.*\\conf\\extra\\httpd-vhosts.conf"
        self.windows_guesser.set_path_parts(generic_apache_path)
        self.windows_guesser.set_generic_apache_path(generic_apache_path)
        self.windows_guesser.sepparate_preffix_suffix_from_generic_path()

        expected_result = "D:\\wamp64\\bin\\apache"
        prefix_result = self.windows_guesser.get_prefix_path_from_generic_path()

        self.assertEqual(expected_result, prefix_result)


if __name__ == '__main__':
    unittest.main()
