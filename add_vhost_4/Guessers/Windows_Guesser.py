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
        self.path_parts = []
        self.count_loop = 0
        self.prefix_path = ""
        self.suffix_path = ""


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
            self.set_path_parts(candidate)
            candidate = self.search_version_asterisk()

        return candidate


    def search_version_asterisk(self):
        
        generated_prefix_and_suffix = self.sepparate_preffix_suffix_from_generic_path()

        found_dir = self.file_list[0]

        return os.path.join( 
            generated_prefix_and_suffix[0],
            found_dir,
            generated_prefix_and_suffix[1]
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


    def config_prefix_path_from_generic_path(self):
        
        prefix_parts = []

        for part in self.path_parts:
            if re.search("\*", part):
                break
            prefix_parts.append(part)
            self.count_loop = self.count_loop + 1

        self.prefix_path = self.generate_path_string_from_list(prefix_parts)



    def set_path_parts(self, path: str):
        self.path_parts = path.split("\\")


    def config_suffix_path_from_generic_path(self):
        suffix_parts = []
        suffix_count_loop = 0
        for part in self.path_parts:
            suffix_count_loop = suffix_count_loop + 1
            if suffix_count_loop <= self.count_loop + 1:
                continue
            suffix_parts.append(part)
            self.count_loop = self.count_loop + 1

        self.suffix_path = self.generate_path_string_from_list(suffix_parts)


    def get_prefix_path_from_generic_path(self):
        return self.prefix_path


    def sepparate_preffix_suffix_from_generic_path(self) -> list: 

        self.config_prefix_path_from_generic_path()

        self.config_suffix_path_from_generic_path()

        return [
            self.prefix_path,
            self.suffix_path
        ]
        