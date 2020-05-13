if [ -d data ]; then
    echo "path ./data is already exists"
else
    mkdir data
    wget http://aoi.naist.jp/DNorm/train.txt -O data/train.txt
    wget http://aoi.naist.jp/DNorm/valid.txt -O data/valid.txt
    wget http://aoi.naist.jp/DNorm/test.txt -O data/test.txt
    wget http://aoi.naist.jp/DNorm/sample.txt -O data/sample.txt
    wget http://aoi.naist.jp/DNorm/normal_set.txt -O data/normal_set.txt
fi
