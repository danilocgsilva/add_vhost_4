import os

class VHost_Entry:

    def add(self):
        vhosts_file = self.__get_vhost_file__()
        vhost_file_resource = open(vhosts_file, "a")

        template_file = os.path.join('add_vhost_4', 'vhost_config.template')
        template_file_resource = open(template_file, "r")

        vhost_file_resource.write("")

        template_lines = template_file_resource.readlines()
        for template_line in template_lines:
            vhost_file_resource.write(template_line)


    def __get_vhost_file__(self):
        return '/Applications/XAMPP/xamppfiles/etc/extra/httpd-vhosts.conf'
