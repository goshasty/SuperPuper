import shlex
import cmd
from cowsay import list_cows, cowsay, Option, make_bubble, THOUGHT_OPTIONS
#from itertools import batched

def batched(args, n):
    if n==2:
        return [(args[i*2], args[i*2+1]) for i in range(0, (len(args)+1)//2)]
    
class Cow(cmd.Cmd):
    prompt = "<<^_^>> "
    
    
    
    d_params_cowsay = {
        '-e': 'eyes',
        '-t': 'tongue',
        '-f': 'cow',
    }
    
    d_params_bubble = {
        '-w': 'width',
        '-b': 'brackets'
    }
    
    d_default_cowsay = {
        '-e': ['oo', '$$'],
        '-t': ['=', '[['],
        '-f': list_cows()[:4],
    }
    
    d_params = {
        'cowsay': d_params_cowsay,
        'make_bubble': d_params_bubble
    }
    
    def __params(self, args, function: str):
        params_dict = self.d_params[function]   
        params = {}
        print(batched(args, 2))
        for arg, val in batched(args, 2):
            params[params_dict[arg]] = val
        return params
    

    def do_list_cows(self, args=None):
        """Get all available cows"""
        print(*list_cows())

    def do_make_bubble(self, args):
        """Make bubbles"""
        args = shlex.split(args)
        
        params=self.__params(args[1:], 'make_bubble')
        if 'brackets' in params:
            params['brackets'] = THOUGHT_OPTIONS[params['brackets']]
        print(make_bubble(args[0], **params))

    def do_cowsay(self, args):
        """Cow say your message"""
        args = shlex.split(args)
        params=self.__params(args[1:], 'cowsay')
        print(cowsay(args[0], **params))
    
    def complete_cowsay(self, text, line, begidx, endidx) -> list[str] | None:
        words = (line[:endidx] + " ").split()
        return self.d_default_cowsay.get(words[-1], None)
        
    def do_EOF(self, args=None):
        return 1

if __name__ == '__main__':
    Cow().cmdloop() 
    