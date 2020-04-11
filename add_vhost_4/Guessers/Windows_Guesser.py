import os
import re

class Windows_Guesser:

    def __init__(self):
        self.possibles = [
            "C:\\wamp64\\bin\\apache\\apache2.4.37\\conf\\extra\\httpd-vhosts.conf",
            "D:\\wamp64\\bin\\apache\\apache2.4.37\\conf\\extra\\httpd-vhosts.conf"
        ]
        self.httpd_entries_address = None
        self.file_list = []
        self.generic_apache_path = ""


    def guess_vhost_entries(self):

        if not self.generic_apache_path == "":
            return self.search_version(self.generic_apache_path)

        return self.possibles[0]


    def get_base_physical_path(self):
        return os.path.join(self.httpd_entries_address[0:9], "www")


    def add_possibles(self, possible: str):
        self.possibles.append(possible)


    def add_file_list(self, file_list: list):
        self.file_list = self.file_list + file_list


    def search_version(self, candidate):

        if re.search("\*", candidate):
            candidate = self.search_version_asterisk(candidate)

        return candidate


    def search_version_asterisk(self, candidate):

        path_parts = candidate.split("\\")
        count_loop = 0

        prefix_parts = []
        for part in path_parts:
            if re.search("\*", part):
                break
            prefix_parts.append(part)
            count_loop = count_loop + 1

        suffix_parts = []
        suffix_count_loop = 0
        for part in path_parts:
            suffix_count_loop = suffix_count_loop + 1
            if suffix_count_loop <= count_loop + 1:
                continue
            suffix_parts.append(part)
            count_loop = count_loop + 1

        found_dir = self.file_list[0]

        return os.path.join( 
            self.generate_path_string_from_list(prefix_parts),
            found_dir,
            self.generate_path_string_from_list(suffix_parts)
        )


    def generate_path_string_from_list(self, parts_list: list):
        path_string = ""
        loop_pass = 0
        for part in parts_list:
            path_string = path_string + part
            if len(parts_list) != loop_pass + 1:
                path_string = path_string + os.sep
            loop_pass = loop_pass + 1
        return path_string


    def set_generic_apache_path(self, generic_apache_path: str):
        self.generic_apache_path = generic_apache_path
