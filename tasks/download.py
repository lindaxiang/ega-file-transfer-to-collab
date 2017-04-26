#!/usr/bin/env python

import sys
import json
import time
from utils import get_task_dict, save_output_json

task_dict = get_task_dict(sys.argv[1])

task_start = int(time.time())

# do the real work here
task_input = task_dict.get('input')
abs_file = os.path.join(os.getcwd(), task_input.get('file_name'))

# need to do the real download based on input 
with open(abs_file, 'w') as l:
	l.write('this is a test file of %s' % f.get('ega_file_id'))


# complete the task

task_stop = int(time.time())

output_json = {
    'task_start': task_start,
    'task_stop': task_stop,
    'file': abs_file
}

for i in ['ega_file_id', 'file_name', 'object_id', 'file_size', 'file_md5sum']:
	output_json.update({i: task_input.get(i)})

save_output_json(output_json)
