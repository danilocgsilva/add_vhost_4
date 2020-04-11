import os
from add_vhost_4.Guessers.Windows_Guesser import Windows_Guesser
from add_vhost_4.Guessers.Posix_Guesser import Posix_Guesser

class VHost_Entry:

    def __init__(self):

        self.guesser = None

        if os.name == 'nt':
            self.guesser = Windows_Guesser()
        else:
            self.guesser = Posix_Guesser()

        self.vhost_file = self.guesser.guess_vhost_entries()

        if not os.path.isfile(self.vhost_file):
            raise FileNotFoundError("There were not possible to guess the path for the virtual hosts entry.")

        self.desired_name = None


    def can_write(self) -> bool:
        try:
            resource_test = open(self.vhost_file, "a")
            resource_test.close()
            return True
        except:
            return False


    def add(self, desired_name):
        self.desired_name = desired_name
        vhost_file_resource = open(self.vhost_file, "a")
        template_file_resource = open(self.__get_template_config_file__(), "r")
        vhost_file_resource.write("\n\n")
        template_lines = template_file_resource.readlines()
        self.__write_to_template__(template_lines, vhost_file_resource)


    def __get_template_config_file__(self) -> str:
        current_file_full_path = os.path.realpath(__file__)
        current_folder = os.path.dirname(current_file_full_path)
        return os.path.join(current_folder, 'vhost_config.template')


    def __write_to_template__(self, template_lines: list, vhost_file_resource):
        line_loop = 0

        self.physical_vhost_path = os.path.join(self.guesser.get_base_physical_path(), self.desired_name)

        for template_line in template_lines:
            if line_loop == 1:
                line_string = template_line.format(self.desired_name)
            elif line_loop == 2:
                line_string = template_line.format(self.physical_vhost_path)
            else:
                line_string = template_line
            vhost_file_resource.write(line_string)
            line_loop += 1


    def write_folder(self):
        if not os.path.isdir(self.physical_vhost_path):
            os.makedirs(self.physical_vhost_path)
            self.__make_stub_php__()


    def get_physical_vhost_path(self):
        return self.physical_vhost_path


    def __make_stub_php__(self):
        file_name = os.path.join(self.physical_vhost_path, 'index.html')
        file_resource = open(file_name, "w")
        file_resource.write('Hello world! This VirtualHost name is ' + self.desired_name)
