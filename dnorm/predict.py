import MeCab
import sys
import pickle
import argparse

sys.path.append('../')
from dnorm import Tokenizer, DNorm, tokenize

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_path", help="train path")
    parser.add_argument("--normal", help="normal set path")
    parser.add_argument("-o", "--output", help="output model path (pkl)")
    args = parser.parse_args()

    mecab = MeCab.Tagger('-Owakati')
    tokenizer = Tokenizer(mecab.parse, lambda s: s[:-1])

    with open(args.normal, 'r') as f:
        normal_set = [line for line in f.read().split('\n') if line != '']

    with open(args.tfidf, 'rb') as f:
        tfidf = pickle.load(f)

    with open(args.input, 'r') as f:
        test_X = [line for line in f.read().split('\n') if line != '']

    model = DNorm(tfidf, normal_set, tokenizer.tokenize)
    model.load(args.model)
    pred = model.predict(test_X)

    output = ['入力\t予測']
    for x, p in zip(test_X, pred):
        output.append(x + '\t' + p)

    with open(args.output, 'w') as f:
        f.write('\n'.join(output))
