def write_hosts():
    file_to_write = get_hosts_file_path()
    file_resource = open(file_to_write, 'a')
    file_resource.write("\nteste")
    file_resource.close()


def get_hosts_file_path():
    return '/etc/hosts'
