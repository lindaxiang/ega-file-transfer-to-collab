#!/usr/bin/env python

import sys
import json
import time
from utils import get_task_dict, save_output_json, get_md5

task_dict = get_task_dict(sys.argv[1])

task_start = int(time.time())

# do the real work here
for f in task_dict.get('input').get('files'):
    check_sum = get_md5(f.get('file_name'))
    if not check_sum: 
	task_info = 'Error: file does not exist'
    elif not check_sum == f.get('file_md5sum'):
	task_info = 'Error: mismatch file_md5sum'
    else:
    	task_info = 'Pass md5sum check'

# complete the task

task_stop = int(time.time())

output_json = {
    'task_start': task_start,
    'task_stop': task_stop,
    'task_info': task_info
}

save_output_json(output_json)

if task_info.startswith('Error'):
    sys.exit(1)

