from add_vhost_4.Hosts import Hosts
from add_vhost_4.VHost_Entry import VHost_Entry



hosts = Hosts()
vhost_entry = VHost_Entry()

hosts.write_hosts()
vhost_entry.add()