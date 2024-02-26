import argparse
import cowsay

def main(args):
    message = ' '.join(args.message)
    cow_said = cowsay.cowsay(
        message=message,
        eyes=args.eyes
    )
    print(cow_said)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('message', nargs='*', default='')
    parser.add_argument('-e', '--eyes', type = str, default = 'oo')
   
    args = parser.parse_args()
    
    main(args)