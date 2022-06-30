import csv
import json
import re

import jaconv

from .util import load_abb_dic


class Converter(object):
    def __init__(self, med_dic_path):
        self.med_dic = load_abb_dic(med_dic_path)

    def convert(self, sent):
        sent = jaconv.z2h(sent, kana=False, ascii=True, digit=True)
        iters = re.finditer(r"([a-zA-Z][a-zA-Z\s]*)$", sent)
        output_word = ""
        pos = 0
        for i in iters:
            s_pos, e_pos = i.span()
            word = i.groups()[0]
            word = re.sub("^\s", r"", word)
            word = re.sub("\s$", r"", word)
            s_word = ""

            while pos < s_pos:
                output_word += sent[pos]
                pos += 1

            if word in self.med_dic:
                s_word = self.med_dic[word]
            elif word.lower() in self.med_dic:
                s_word = self.med_dic[word.lower()]
            else:
                s_word = word

            if s_word == "":
                s_word = word

            output_word += s_word
            pos = e_pos

        while pos < len(sent):
            output_word += sent[pos]
            pos += 1

        return jaconv.h2z(output_word, kana=True, ascii=True, digit=True)


if __name__ == "__main__":
    with open("data/abb_dic.json", "r") as f:
        med_dic = json.load(f)

    converter = Converter(med_dic)
    print(converter.convert("AML"))
