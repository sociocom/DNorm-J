if [ -d models ]; then
    echo "path ./models is already exists"
else
    mkdir models
    wget http://aoi.naist.jp/DNorm/W.npz -O models/W.npz
    wget http://aoi.naist.jp/DNorm/EHR_idf.pkl -O models/EHR_idf.pkl
fi
