import sys

class CLI:

    def __init__(self):
        try:
            self.user_argument = sys.argv[1]
        except IndexError:
            print("Please, provide as the first argument the virtual host name.")
            exit()

    def get_user_param(self) -> str:
        return self.user_argument
