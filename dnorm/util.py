import shutil
import requests

def download_fileobj(src, dst, binary=False):
    res = requests.get(src, stream=True)
    with open(dst, "wb") as f:
        shutil.copyfileobj(res.raw, f)

