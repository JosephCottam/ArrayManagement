from os.path import join, dirname, split, realpath, exists
from six.moves import cPickle
import json

def jsload(path):
    with open(path) as f:
        return json.load(f)
    
def jswrite(obj, path):
    with open(path, "w+") as f:
        return json.dump(obj, f)
    
def jsupdate(path, update):
    if not exists(path):
        data = {}
    else:
        data = jsload(path)
    data.update(update)
    jswrite(data, path)

