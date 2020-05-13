SCRIPT_DIR=$(cd $(dirname $0); pwd)
python $SCRIPT_DIR/predict.py --input data/sample.txt\
    --model models/W_EHR_all.npz\
    --normal data/normal_set.txt\
    --tfidf models/EHR_idf.pkl\
    --output data/sample_output.txt
