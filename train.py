import MeCab
from d_norm import Tokenizer, DNorm, tokenize
from expand_abbreviation import Converter
import pickle
import argparse
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", help="train path")
    parser.add_argument("--valid", help="validation path")
    parser.add_argument("--normal", help="normal set path")
    parser.add_argument("--tfidf", help="tfidf model path (pkl)")
    parser.add_argument("--output", help="output model path (pkl)")
    args = parser.parse_args()

    mecab = MeCab.Tagger('-Owakati')
    tokenizer = Tokenizer(mecab.parse, lambda s: s[:-1])

    with open(args.normal, 'r') as f:
        normal_set = [line for line in f.read().split('\n') if line != '']

    with open(args.tfidf, 'rb') as f:
        tfidf = pickle.load(f)

    with open(args.train, 'r') as f:
        lines = [line.split('\t') for line in f.read().split('\n') if line != '']
        train_X = [line[1] for line in lines]
        train_Y = [line[0] for line in lines]

    with open(args.valid, 'r') as f:
        lines = [line.split('\t') for line in f.read().split('\n') if line != '']
        val_X = [line[1] for line in lines]
        val_Y = [line[0] for line in lines]

    with open('data/abb_dic.json') as f:
        med_dic = json.load(f)

    model = DNorm(tfidf, normal_set, tokenizer.tokenize, med_dic)
    #model.load('W.npz')
    #print(model.evaluate(test_X, test_Y))
    #print(model.predict(test_X))
    model.train(train_X, train_Y, val_X, val_Y, 1e-1)
    model.save(args.output)
