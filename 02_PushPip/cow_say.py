import argparse
import cowsay

def main(args):
    message = ' '.join(args.message)
    cow_said = cowsay.cowsay(
        message=message,
        eyes=args.eyes,
        tongue=args.tongue,
        cowfile=args.cowfile,
        wrap_text=args.wrap_text
    )
    print(cow_said)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('message', nargs='*', default='')
    parser.add_argument('-e', dest='eyes', type=str, default='oo')
    parser.add_argument('-T', dest='tongue', type=str, default='__')
    parser.add_argument('-f', dest='cowfile', type=str, default=None)
    parser.add_argument(
        '-n', dest='wrap_text', type=bool, default=True, 
        help="To use -n arg: python3 cow_say.py -n '' <other args>/<message>"
    )
   
    args = parser.parse_args()
    
    main(args)