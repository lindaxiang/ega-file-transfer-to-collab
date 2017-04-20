#!/usr/bin/env python

from utils import get_task_dict
import json

task_dict = get_task_dict(argv[1])


with open('task_json.json', 'w') as f:
  f.write(json.dumps(task_dict))


with open('output.json', 'w') as f:
  f.write(json.dumps({"task": "prepare_metadata_xml"}))

