# DNorm-J
## 概要
日本語の病名を正規化するツールです

## 手法
[DNorm](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3810844/)の日本語実装になります．

詳細はリンク先の論文をご参照ください．

## 環境
```
python>=3.6.1
MeCab==0.996.5
```

## インストール
```
pip install .
```

## 使い方
- -i：入力ファイル
- -o：出力ファイル
- -n：正規化先の病名リスト（デフォルト設定では指定する必要はありません）
- -d：略語展開辞書（デフォルト設定では指定する必要はありません）

```python -m dnorm_j -i sample.txt -o output.txt```

## コマンドから
### 入力（sample.txt）

### 出力（output.txt）

### スクリプトから

```
from dnorm_j import DNorm

model = DNorm.from_pretrained()
result = model.normalize('AML')
print(result)
```

