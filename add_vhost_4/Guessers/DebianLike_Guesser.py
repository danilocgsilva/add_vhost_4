import re
import os
from add_vhost_4.Guessers.Posix_Guesser import Posix_Guesser

class DebianLike_Guesser:

    def __init__(self):
        self.os_release_file = os.sep + os.path.join('etc', 'os-release')


    def is_debian_like(self) -> bool:

        if os.name == 'nt':
            return False

        os_name = self.__get_os_release_name__()


        if os_name == None:
            return False

        if os_name == 'Ubuntu' or os_name == 'Debian' or os_name == 'Mint':
            return True

        return False


    def __get_os_release_name__(self) -> str:
        fr = open(self.os_release_file, "r")
        line = fr.readline()
        while line:
            line = re.sub(r'"', r'', line)
            line = re.sub(r"\n", r"", line)
            if re.search('NAME', line):
                name_strings = line.split('=')
                return name_strings[1]
            line = fr.readline()


    def write_folder(self):
        if not os.path.isdir(self.physical_vhost_path):
            os.makedirs(self.physical_vhost_path)
            self.__make_stub_php__()


    def __make_stub_php__(self):
        file_name = os.path.join(self.physical_vhost_path, 'index.html')
        file_resource = open(file_name, "w")
        file_resource.write('Hello world! This VirtualHost name is ' + self.desired_name)


    def get_base_physical_path(self) -> str:
        posix_guesser = Posix_Guesser()
        return posix_guesser.get_base_physical_path()

        