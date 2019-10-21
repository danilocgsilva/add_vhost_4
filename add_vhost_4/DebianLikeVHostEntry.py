from add_vhost_4.Guessers.Posix_Guesser import Posix_Guesser
import os
import subprocess

class DebianLikeVHostEntry:

    def __init__(self, vhost_desired):
        self.vhost_desired = vhost_desired
        self.guesser = Posix_Guesser()
        self.vhost_file_entry = self.guesser.guess_debian_like_vhost_file(self.vhost_desired)
        self.physical_vhost_path = self.guesser.get_base_physical_path()


    def add(self, vhost_desired: str):
        template_file_resource = open(self.__get_template_config_file__(), "r")
        template_lines = template_file_resource.readlines()
        self.__write_entry__(template_lines)
        self.__link__()


    def write_folder(self):
        print("-----" + self.physical_vhost_path)
        if not os.path.isdir(self.physical_vhost_path):
            os.makedirs(self.physical_vhost_path)
            self.__make_stub_php__()


    def can_write(self) -> bool:
        try:
            resource_test = open(self.vhost_file_entry, "a")
            resource_test.close()
            return True
        except:
            return False


    def __get_template_config_file__(self) -> str:
        current_file_full_path = os.path.realpath(__file__)
        current_folder = os.path.dirname(current_file_full_path)
        return os.path.join(current_folder, 'vhost_config.template')


    def __write_entry__(self, template_lines: list):
        vhost_file_resource = open(self.vhost_file_entry, 'a')

        line_loop = 0

        for template_line in template_lines:
            if line_loop == 1:
                line_string = template_line.format(self.vhost_desired)
            elif line_loop == 2:
                line_string = template_line.format(self.vhost_desired)
            else:
                line_string = template_line
            vhost_file_resource.write(line_string)
            line_loop += 1


    def __make_stub_php__(self):
        file_name = os.path.join(self.physical_vhost_path, 'index.html')
        file_resource = open(file_name, "w")
        file_resource.write('Hello world! This VirtualHost name is ' + self.vhost_desired)


    def __link__(self):
        subprocess.call(['a2ensite', self.vhost_desired])
