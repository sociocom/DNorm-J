# DNorm-J
Japanese disease normalization tool ([DNorm](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3810844/))

## 環境
```
python>=3.6
MeCab==0.996.5
```
pythonの依存ライブラリ
```
numpy==1.18.2
scipy==1.4.1
sklearn==0.0
tqdm==4.45.0
```

以下のコードから上記ライブラリのインストールが行えます
```
pip install -r requirements.txt
```

## ダウンロード
- 標準病名リスト，コーパス（万病辞書）
```
sh download_corpus.sh
```

- 学習済みモデル
```
sh download_model.sh
```

## 使い方
- 標準化
```
python predict.py --input (病名リスト) --model (学習済みモデル) --normal (標準病名リスト) --tfidf (TF-IDFモデル) --output (出力パス)
```
- 学習
```
python train.py --train (学習データ) --valid (検証データ) --normal (標準病名リスト) -tfidf (TF-IDFモデル) --output (モデル出力パス)
```
