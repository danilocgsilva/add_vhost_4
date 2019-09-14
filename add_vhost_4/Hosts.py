import os

class Hosts:

    def write_hosts(self):
        file_to_write = self.__get_hosts_file_path__()
        file_resource = open(file_to_write, 'a')
        file_resource.write("\nteste")
        file_resource.close()


    def __get_hosts_file_path__(self) -> str:
        if os.name == 'posix':
            return '/etc/hosts'
        elif os.name == 'nt':
            return 'C:\Windows\System32\drivers\etc\hosts'
        else:
            raise Exception("Sorry! I don't know which system I am running on... I am so dumb!!!!")
