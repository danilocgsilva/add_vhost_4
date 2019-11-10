import os
import subprocess

class Apache_Restarter:

    def __init__(self):
        self.fnull = open(os.devnull, 'w')


    def restart(self) -> bool:
        restarted = self.__try_restart__('debian')
        if restarted:
            return True
        if not restarted:
            restarted = self.__try_restart__('centos')
        if restarted:
            return True
        return False


    def __try_restart__(self, mode: str) -> bool:

        if mode == 'debian':
            service = 'apache2'
        elif mode == 'centos':
            service = 'httpd'
        else:
            raise Exception("The pattern for restart still not implemented.")

        try:
            result_from_trial = subprocess.call(
                ['service', service, 'restart'], 
                stdout = self.fnull, 
                stderr = self.fnull
            )
            if result_from_trial == 0:
                return True
            return False
        except FileNotFoundError:
            return False


