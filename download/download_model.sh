if [ -d models ]; then
    echo "path ./models is already exists"
else
    mkdir models
    wget http://aoi.naist.jp/DNorm/W.npz -O models/W.npz
    wget http://aoi.naist.jp/DNorm/DATA_IM_tfidf.pkl -O models/DATA_IM_tfidf.pkl
fi
