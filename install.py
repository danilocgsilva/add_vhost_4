from install_assets.Installer import Installer

installer = Installer()

can_write = installer.check_write_permission()

if not can_write:
    print(installer.get_error_messages())
    exit()

installer.write_os_entry()
installer.copy_files()

print("Run in the terminal: add_vhost")
