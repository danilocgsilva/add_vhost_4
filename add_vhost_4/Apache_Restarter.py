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
        try:
            if mode == 'debian':
                return self.__debian_like_restart__()
            elif mode == 'centos':
                return self.__debian_like_restart__()
        except FileNotFoundError:
            return False


    def __debian_like_restart__(self) -> bool:
        result_from_trial = subprocess.call(
            ['service', 'apache2', 'restart'], 
            stdout = self.fnull, 
            stderr = self.fnull
        )
        if result_from_trial == 0:
            return True
        return False



    def __centos_like_restart__(self) -> bool:
        result_from_trial = subprocess.call(
            ['service', 'httpd', 'restart'], 
            stdout = self.fnull, 
            stderr = self.fnull
        )
        if result_from_trial == 0:
            return True
        return False
