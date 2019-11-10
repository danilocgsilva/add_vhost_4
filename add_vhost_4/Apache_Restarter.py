import os
import subprocess

class Apache_Restarter:

    def restart(self) -> bool:
        restarted = self.__debian_like_restart__()
        if restarted:
            print("Success in the debian like restart")
            return True
        if not restarted:
            restarted = self.__centos_like_restart__()
        if restarted:
            return True
        return False


    def __debian_like_restart__(self) -> bool:
        FNULL = open(os.devnull, 'w')
        result_from_trial = subprocess.call(
            ['service', 'apache2', 'restart'], 
            stdout=FNULL, 
            stderr=FNULL
        )
        if result_from_trial == 0:
            return True
        return False


    def __centos_like_restart__(self) -> bool:
        FNULL = open(os.devnull, 'w')
        result_from_trial = subprocess.call(['service', 'httpd', 'restart'], stdout=FNULL, stderr=FNULL)
        if result_from_trial == 0:
            return True
        return False
