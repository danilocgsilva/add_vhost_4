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


    def guess_vhost_entries(self):

        for candidate in self.possibles:

            processed_candidate = self.search_version(candidate)

            if os.path.isfile(processed_candidate):
                self.httpd_entries_address = candidate
                return self.httpd_entries_address

        raise FileNotFoundError("There were not possible to guess the path for the virtual hosts entry.")


    def get_base_physical_path(self):
        return os.path.join(self.httpd_entries_address[0:9], "www")


    def add_possibles(self, possible: str):
        self.possibles.append(possible)


    def add_file_list(self, file_list: list):
        self.file_list = self.file_list + file_list


    def search_version(self, candidate):
        if re.search("\*", candidate):
            path_parts = candidate.split("\\")
            count_loop = 0

            prefix_parts = []
            for part in path_parts:
                if re.search("\*", part):
                    break
                prefix_parts.append(part)
                count_loop = count_loop + 1
            list_dir = os.listdir(
                self.generate_path_string_from_list(prefix_parts)
            )
            found_dir = list_dir[0]
            return self.generate_path_string_from_list(prefix_parts)
            # return found_dir

            # return "C:\\wamp64\\bin\\apache\\apache2.4.39\\conf\\extra\\httpd-vhosts.conf"
        return candidate


    def generate_path_string_from_list(self, parts_list: list):
        path_string = ""
        loop_pass = 0
        for part in parts_list:
            path_string = path_string + part
            if len(parts_list) != loop_pass + 1:
                path_string = path_string + os.sep
            loop_pass = loop_pass + 1
        return path_string
        


