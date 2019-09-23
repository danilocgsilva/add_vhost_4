from add_vhost_4.Hosts import Hosts
from add_vhost_4.VHost_Entry import VHost_Entry
from add_vhost_4.CLI import CLI

hosts = Hosts()

try:
    vhost_entry = VHost_Entry()
except FileNotFoundError as fnfe:
    print("The virutalhost file entry has not been found in the system. Sorry!")
    exit()

cli = CLI()
errors = []

if not hosts.can_write():
    errors.append("Can't write in the hosts file. Check permission.")

if not vhost_entry.can_write():
    errors.append("Can't write to the virtualhosts file. Check permission.")

if len(errors) > 0:
    print("There are permission issues that won't allow you to install the virtual host in the computer:")
    for error in errors:
        print(error)
    exit()

vhost_desired = cli.get_user_param()

hosts.write_hosts(vhost_desired)
vhost_entry.add(vhost_desired)
vhost_entry.write_folder()

print("Virtualhost added locally successfully. Restart your webserver application and access http://" + vhost_desired)
