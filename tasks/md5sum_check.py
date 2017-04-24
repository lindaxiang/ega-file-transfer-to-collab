#!/usr/bin/env python

from utils import get_task_dict, get_md5
import json
import sys

task_dict = get_task_dict(sys.argv[1])


with open('task_json.json', 'w') as f:
  f.write(json.dumps(task_dict))


with open('output.json', 'w') as f:
  f.write(json.dumps({"task": "md5sum_check"}))

