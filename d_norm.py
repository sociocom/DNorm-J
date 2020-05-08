import MeCab
import pickle
from scipy.sparse import csr_matrix, save_npz, load_npz, vstack
import numpy as np
from tqdm import tqdm
mecab = MeCab.Tagger('-Owakati')

def tokenize(text):
    return text.split(' ')

class Tokenizer(object):
    def __init__(self, tokenizer, fn):
        self.tokenizer = tokenizer
        self.fn = fn

    def tokenize(self, text):
        return self.fn(self.tokenizer(text))

class DNorm(object):
    def __init__(self, model, normal_set, tokenizer):
        self.model = model
        self.normal_set = np.array(normal_set)
        self.normal_list = set(normal_set)
        self.tokenizer = tokenizer
        self.normal_vecs = self._encode(self.normal_set)

        num = len(self.model.vocabulary_)
        row = np.array([i for i in range(num)])
        col = np.array([i for i in range(num)])
        data = np.array([1 for i in range(num)])
        self.W = csr_matrix((data, (row, col)), shape=(num, num))

    def save(self, path):
        save_npz(path, self.W)
        
    def load(self, path):
        self.W = load_npz(path)

    def _encode(self, text_list):
        text_list = [self.tokenizer(text) for text in text_list]
        return self.model.transform(text_list)

    def _score_vec(self, v1, v2):
        return (v1.dot(self.W)).dot(v2.T)

    def _sample_negative(self, x, y):
        try:
            i = np.where(self.normal_set == y)[0][0]
        except:
            print(y, y in self.normal_set)
        if i == 0:
            neg_vecs = self.normal_vecs[1:]
        elif i == len(self.normal_set) - 1:
            neg_vecs = self.normal_vecs[:-1]
        else:
            neg_vecs = vstack([self.normal_vecs[:i], self.normal_vecs[i+1:]])
        #neg_list = list(self.normal_list - set([y]))
        #neg_vecs = self._encode(neg_list)
        #x_vecs = self._encode([x])
        sims = self._score_vec(x, neg_vecs)
        rank = sims.argmax()

        return neg_vecs[rank]

    def calc_avg_rank(self, x, y, encoded=False):
        pred = self.predict(x, k=-1, encoded=encoded)
        rank = 0
        cnt = 0
        zero = 0
        for p, t in zip(pred, y):
            tmp = np.where(p == t)[0]
            if tmp == 0:
                zero += 1
            tmp = min(tmp, 1000)
            rank += tmp
            cnt += 1
        print(zero, cnt)
        return rank / cnt

    def evaluate(self, x, y):
        pred = self.predict(x)
        cnt = 0
        total = 0
        for p, t in zip(pred, y):
            p = p[0]
            if p == t:
                cnt += 1
            total += 1
        return cnt / total


    def train(self, X, Y, val_x, val_y, eta):
        val_score = [1e8, 1e7]
        vec_X = self._encode(X)
        vec_Y = self._encode(Y)
        vec_val_x = self._encode(val_x)
        score = self.evaluate(val_x, val_y)
        while val_score[-1] < val_score[-2]:
            #idx = np.random.choice(len(X), 1)[0]
            idx_list = np.random.permutation([i for i in range(len(X))])
            for idx in tqdm(idx_list):
                x_vec = vec_X[idx]
                y_vec = vec_Y[idx]
                y = Y[idx]
                neg_vec = self._sample_negative(x_vec, y)
                #vecs = self._encode([x, y, neg])
                #x_vec, y_vec, neg_vec = vecs[0], vecs[1], vecs[2]
                self._update(x_vec, y_vec, neg_vec, eta)

            #score = self.evaluate(val_x, val_y)
            #score = self.calc_avg_rank(val_x, val_y, encoded=True)
            score = self.calc_avg_rank(vec_val_x, val_y, encoded=True)
            val_score.append(score)
            print(score)


    def predict(self, t, k=1, encoded=False):
        if not encoded:
            t = self._encode(t)
        sims = self._score_vec(t, self.normal_vecs).toarray()
        rank = sims.argsort(axis=1)[:, ::-1][:, :k]
        return np.take_along_axis(self.normal_set[:, np.newaxis], rank, axis=0)

    def _update(self, m, np, nn, eta):
        score = self._score_vec(m, np).toarray()[0][0] - self._score_vec(m, nn).toarray()[0][0]
        if score < 1:
            self.W = self.W + eta * (m.T.dot(np) - m.T.dot(nn))


if __name__ == '__main__':
    tokenizer = Tokenizer(mecab.parse, lambda s: s[:-1])

    with open('normal_set.txt', 'r') as f:
        normal_set = [line for line in f.read().split('\n') if line != '']

    with open('DATA_IM_tfidf.pkl', 'rb') as f:
        tfidf = pickle.load(f)

    """
    with open('data/train.txt', 'r') as f:
        lines = [line.split('\t') for line in f.read().split('\n') if line != '']
        train_X = [line[1] for line in lines]
        train_Y = [line[0] for line in lines]

    with open('data/valid.txt', 'r') as f:
        lines = [line.split('\t') for line in f.read().split('\n') if line != '']
        val_X = [line[1] for line in lines]
        val_Y = [line[0] for line in lines]
    """

    with open('sample.txt', 'r') as f:
        lines = [line.split('\t') for line in f.read().split('\n') if line != '']
        test_X = [line[1] for line in lines]
        test_Y = [line[0] for line in lines]

    #print(len(train_X), len(val_X))
    model = DNorm(tfidf, normal_set, tokenizer.tokenize)
    model.load('W.npz')
    print(model.evaluate(test_X, test_Y))
    #print(model.predict(test_X))
    #model.train(train_X, train_Y, val_X, val_Y, 1e-2)
    #model.train(val_X, val_Y, val_X, val_Y, 1e-1)
    #model.save('W_0.01.npz')