import shlex
import cmd
from cowsay import list_cows, cowsay
from itertools import batched

class Cow(cmd.Cmd):
    prompt = "<<^_^>> "
    d_params_cowsay = {
        '-e': 'eyes',
        '-t': 'tongue',
        '-f': 'cow',
    }

    def __cowsay_params(self, args):
        params = {}
        for arg, val in batched(args, 2):
            params[self.d_params_cowsay[arg]] = val
        return params
    

    def do_list_cows(self, args=None):
        """Get all available cows"""
        print(*list_cows())

    def do_cowsay(self, args):
        """Cow say your message"""
        args = shlex.split(args)
        params=self.__cowsay_params(args[1:])
        print(cowsay(args[0], **params))
        
    def do_EOF(self, args=None):
        return 1

if __name__ == '__main__':
    Cow().cmdloop() 
    