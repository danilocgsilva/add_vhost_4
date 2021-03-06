from add_vhost_4.Hosts import Hosts
from add_vhost_4.VHost_Entry import VHost_Entry
from add_vhost_4.Guessers.DebianLike_Guesser import DebianLike_Guesser
from add_vhost_4.CLI import CLI
from add_vhost_4.DebianLikeVHostEntry import DebianLikeVHostEntry
from add_vhost_4.Apache_Restarter import Apache_Restarter
from add_vhost_4.App import App

hosts = Hosts()
cli = CLI()
vhost_desired = cli.get_user_param()
apache_restarter = Apache_Restarter()
app = App()

debian_like_guesser = DebianLike_Guesser()

if debian_like_guesser.is_debian_like():
    vhost_entry = DebianLikeVHostEntry(vhost_desired)
else:
    vhost_entry = VHost_Entry()

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


hosts.write_hosts(vhost_desired)
vhost_entry.add(vhost_desired)
vhost_entry.write_folder()
app.assignPermissions(vhost_entry.get_physical_vhost_path())
trial_apache_restart = apache_restarter.restart()

if trial_apache_restart:
    print("Virtualhost added locally successfully. Access http://" + vhost_desired)
else:
    print("Virtualhost added locally successfully. Restart your webserver application and access http://" + vhost_desired)

print("You can find your application in: " + vhost_entry.get_physical_vhost_path())