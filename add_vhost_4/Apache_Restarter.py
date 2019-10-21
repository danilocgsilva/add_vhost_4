import subprocess

class Apache_Restarter:

    def restart(self) -> bool:
        try:
            subprocess.call(['service', 'apache2', 'restart'])
            return True
        except:
            return False
