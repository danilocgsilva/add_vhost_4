import os

class Hosts:

    def __init__(self):
        self.hosts_file = self.__get_hosts_file_path__()

    def write_hosts(self, vhost_desired):
        file_resource = open(self.hosts_file, 'a')
        file_resource.write("\n\n127.0.0.1 " + vhost_desired)
        file_resource.write("\n::1 " + vhost_desired)
        file_resource.close()


    def can_write(self) -> bool:
        try:
            open_file_append = open(self.hosts_file, "a")
            open_file_append.close()
            return True
        except:
            return False


    def __get_hosts_file_path__(self) -> str:
        if os.name == 'posix':
            return '/etc/hosts'
        elif os.name == 'nt':
            return 'C:\\Windows\\System32\\drivers\\etc\\hosts'
        else:
            raise Exception("Sorry! I don't know which system I am running on... I am so dumb!!!!")
