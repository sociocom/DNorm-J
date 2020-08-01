import argparse
import sys

from .d_norm import DNorm


parser = argparse.ArgumentParser()
parser.add_argument("-i", '--input_file', nargs='?', type=argparse.FileType("r"),
        default=sys.stdin, help="input file path")
parser.add_argument("-o", '--output_file', nargs='?', type=argparse.FileType("w"),
        default=sys.stdout, help="output file path")
parser.add_argument("-n", "--normal", default="default", help="normal set path")
parser.add_argument("-d", "--dict", default="default", help="normal set path")
args = parser.parse_args()

#with open(args.input_file, 'r') as f:
with args.input_file as f:
    test_x = [line for line in f.read().split('\n') if line != '']

model = DNorm.from_pretrained(args.normal, args.dict)
res = [model.normalize(x) for x in test_x]

#with open(args.output_file, 'w') as f:
with args.output_file as f:
    f.write('\n'.join(res) + '\n')


