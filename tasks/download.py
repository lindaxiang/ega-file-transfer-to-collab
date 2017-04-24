#!/usr/bin/env python

from utils import get_task_dict
import json
import sys

task_dict = get_task_dict(sys.argv[1])

for f in task_dict.get('input').get('files'):
	echo 'this is a test file' > f.get('file_name')
	
with open('task_json.json', 'w') as f:
  f.write(json.dumps(task_dict))


with open('output.json', 'w') as f:
  f.write(json.dumps({"task": "download"}))
