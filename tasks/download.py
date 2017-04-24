#!/usr/bin/env python

from utils import get_task_dict
import json
import sys

task_dict = get_task_dict(sys.argv[1])

for f in task_dict.get('input').get('files'):
	with open(f.get('file_name'), 'w') as l:
		l.write('this is a test file of %s' % f.get('ega_file_id'))

with open('task_json.json', 'w') as f:
  f.write(json.dumps(task_dict))


with open('output.json', 'w') as f:
  f.write(json.dumps({"task": "download"}))
