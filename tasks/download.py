#!/usr/bin/env python

import sys
import json
import time
from utils import get_task_dict, save_output_json

task_dict = get_task_dict(sys.argv[1])

task_start = int(time.time())

# do the real work here
for f in task_dict.get('input').get('files'):
	with open(f.get('file_name'), 'w') as l:
		l.write('this is a test file of %s' % f.get('ega_file_id'))


# complete the task

task_stop = int(time.time())

output_json = {
    'task_start': task_start,
    'task_stop': task_stop
}

save_output_json(output_json)
