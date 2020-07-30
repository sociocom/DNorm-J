import argparse

print(__name__)

from .d_norm import DNorm


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file", help="train path")
parser.add_argument("-n", "--normal", default="default", help="normal set path")
parser.add_argument("-d", "--dict", default="default", help="normal set path")
parser.add_argument("-o", "--output_file", help="output model path (pkl)")
args = parser.parse_args()

with open(args.input_file, 'r') as f:
    test_x = [line for line in f.read().split('\n') if line != '']

model = DNorm.from_pretrained(args.normal, args.dict)
res = [model.normalize(x) for x in test_x]

with open(args.output_file, 'w') as f:
    f.write('\n'.join(res))


