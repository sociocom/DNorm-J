if [ -d models ]; then
    echo "path ./models is already exists"
else
    mkdir models
    wget http://aoi.naist.jp/DNorm/W_EHR_all.npz -O models/W_EHR_all.npz
    wget http://aoi.naist.jp/DNorm/EHR_idf.pkl -O models/EHR_idf.pkl
fi
