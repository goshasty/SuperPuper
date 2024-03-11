import shlex
import cmd
from cowsay import list_cows


class Cow(cmd.Cmd):
    prompt = "<<^_^>> "

    def do_list_cows(self, args=None):
        """Get all available cows"""
        print(*list_cows())

if __name__ == '__main__':
    Cow().cmdloop() 
    