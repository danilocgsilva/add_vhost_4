import os
import subprocess

class Apache_Restarter:

    def restart(self) -> bool:
        restarted = self.__debian_like_restart__()
        if restarted:
            return True
        if not restarted:
            restarted = self.__centos_like_restart__()
            if restarted:
                return True
        return False


    def __debian_like_restart__(self) -> bool:
        try:
            FNULL = open(os.devnull, 'w')
            subprocess.call(['service', 'apache2', 'restart'], stdout=FNULL, stderr=FNULL)
            return True
        except:
            return False


    def __centos_like_restart__(self) -> bool:
        try:
            FNULL = open(os.devnull, 'w')
            subprocess.call(['service', 'httpd', 'restart'], stdout=FNULL, stderr=FNULL)
            return True
        except:
            return False