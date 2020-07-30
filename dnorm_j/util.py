import shutil
import requests
import csv


def tokenize(text):
    return text.split(' ')


def download_fileobj(src, dst, binary=False):
    res = requests.get(src, stream=True)
    with open(dst, "wb") as f:
        shutil.copyfileobj(res.raw, f)

def load_abb_dic(path):
    dic = {}
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            dic[row[0]] = row[1]

    return dic

def load_normal_set(path):
    with open(path, 'r') as f:
        normal_set = [line for line in f.read().split('\n') if line != '']

    return normal_set


