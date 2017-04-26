import json
import os
import hashlib

def get_task_dict(json_string):
    try:
        task_dict = json.loads(json_string)
    except:
        return {}

    return task_dict


def save_output_json(output_dict={}):
    with open('output.json', 'w') as f:
        f.write(json.dumps(output_dict))


def get_md5(fname):
    hash = hashlib.md5()
    if not os.path.isfile(fname): return None
    with open(fname) as f:
        for chunk in iter(lambda: f.read(1024*256), ""):
            hash.update(chunk)
    return hash.hexdigest()


