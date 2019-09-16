import os

class VHost_Entry:

    def __init__(self):
        self.vhost_file = self.__get_vhost_file__()
        self.desired_name = ""


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


    def __get_vhost_file__(self) -> str:
        
        if os.name == 'nt':
            candidate_path = 'D:\\wamp64\\bin\\apache\\apache2.4.37\\conf\\extra\\httpd-vhosts.conf'
        else:
            candidate_path = '/Applications/XAMPP/xamppfiles/etc/extra/httpd-vhosts.conf'

        if not os.path.isfile(candidate_path):
            raise FileNotFoundError("No configuration file found.")

        return candidate_path


    def __get_template_config_file__(self) -> str:
        return os.path.join('add_vhost_4', 'vhost_config.template')


    def __write_to_template__(self, template_lines: list, vhost_file_resource):
        line_loop = 0
        for template_line in template_lines:
            if line_loop == 1:
                line_string = template_line.format(self.desired_name)
            elif line_loop == 2:
                line_string = template_line.format(os.path.join("D:\\wamp64\\www", self.desired_name))
            else:
                line_string = template_line
            vhost_file_resource.write(line_string)
            line_loop += 1
