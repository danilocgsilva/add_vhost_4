import subprocess
import os
import time

class App:

    def __init__(self):
        self.dev_local_user_var = 'DEV_LOCAL_USER'


    def assignPermissions(self, physical_vhost_path) -> bool:

        if os.name == 'nt':
            return False

        current_user = self.__get_dev_user__()
        if current_user == None:
            self.__cannot_get_dev_user_message__()
            return False
            
        self.__assing_group__(current_user, physical_vhost_path)
        subprocess.call(['chmod', '-Rv', '775', physical_vhost_path])
        return True

    
    def __assing_group__(self, current_user, physical_vhost_path) -> bool:

        result = subprocess.call(['chown', '-Rv', current_user + ':' + 'apache', physical_vhost_path])
        if result == 0:
            return True

        result = subprocess.call(['chown', '-Rv', current_user + ':' + 'www-data', physical_vhost_path])
        if result == 0:
            return True

        result = subprocess.call(['chown', '-Rv', current_user + ':' + 'daemon', physical_vhost_path])
        if result == 0:
            return True

        return False


    def __get_dev_user__(self) -> str:
        return os.environ.get(self.dev_local_user_var)


    def __cannot_get_dev_user_message__(self):
        print("...await 15 seconds to let you read the message...")
        print("Cannot see the dev user. We suppose that the in the host system there are a variable called " + self.dev_local_user_var + ", which is the current development user. If the system indeed does not have this variable, pelase, set and assign to your normal user.")
        print("The script will proceed, but no properly permission may be assigned to the virtual host local files.")
        time.sleep(10)
