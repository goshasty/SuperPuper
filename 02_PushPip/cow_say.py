import argparse
import cowsay

def handle_preset(args) -> str:
    # -bgpstwy
    preset_list = []
    if args.b:
        preset_list.append('b')
    if args.g:
        preset_list.append('g')
    if args.p:
        preset_list.append('p')
    if args.s:
        preset_list.append('s')
    if args.t:
        preset_list.append('t')
    if args.w:
        preset_list.append('w')
    if args.y:
        preset_list.append('y')
        
    return ''.join(preset_list)
        

def main(args):
    message = ' '.join(args.message)
    preset = handle_preset(args)
    if args.list:
        print(cowsay.list_cows())
        return
    
    cow_said = cowsay.cowsay(
        message=message,
        eyes=args.eyes,
        tongue=args.tongue,
        cowfile=args.cowfile,
        wrap_text=args.wrap_text,
        width=args.width,
        preset=preset
    )
    
    print(cow_said)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('message', nargs='*', default=' ')
    parser.add_argument('-e', dest='eyes', type=str, default='oo')
    parser.add_argument('-T', dest='tongue', type=str, default='__')
    parser.add_argument('-f', dest='cowfile', type=str, default=None)
    parser.add_argument('-n', dest='wrap_text', action='store_false')
    parser.add_argument('-W', dest='width', type=int, default=40)
    parser.add_argument('-l', dest='list', action = 'store_true')
    
    modes = 'bgpstwy'
    for mode in modes:
        parser.add_argument(f'-{mode}', dest=f'{mode}', action='store_true')
   
    args = parser.parse_args()
    main(args)