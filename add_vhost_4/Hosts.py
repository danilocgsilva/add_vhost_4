class Hosts:

    def write_hosts(self):
        file_to_write = self.__get_hosts_file_path__()
        file_resource = open(file_to_write, 'a')
        file_resource.write("\nteste")
        file_resource.close()


    def __get_hosts_file_path__(self) -> str:
        return '/etc/hosts'