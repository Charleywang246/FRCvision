import argparse

from train import train
from detection import detect
from resources import capture

def get_arguments ():
    parser = argparse.ArgumentParser()
    parser.add_argument('--default', action='store_true', help='use default setting')
    parser.add_argument('--capture', action='store_true', help='get images for training')
    parser.add_argument('--slice', action='store_true', help='slice images to positive and nagetive images')
    parser.add_argument('--train', action='store_true', help='train xml model')
    parser.add_argument('--detect', action='store_true', help='detect objects with webcam')
    parser.add_argument('-xml','--xmlpath', default='cascade.xml', type=str, dest='xmlpath', help='port of webcam (default 0)')
    parser.add_argument('-w', '--webcam', default=0, type=int, dest='port', help='name of xmlfile (default cascade.xml)')
    args = vars(parser.parse_args())
    return args

def main ():
    args = get_arguments()
    camport = args['port']
    xmlpath = args['xmlpath']
    if args['default']:
        capture.start(camport)
        train.start(xmlpath)
        detect.start(camport, xmlpath)

    if args['capture']:
        capture.start(camport)

    if args['slice']:
        train.slice()

    if args['train']:
        train.train(xmlpath)
    
    if args['detect']:
        detect.start(camport, xmlpath)

if __name__ == '__main__':
    main()
