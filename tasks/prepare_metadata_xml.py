#!/usr/bin/env python

import os
import sys
import json
import time
from utils import get_task_dict, save_output_json

task_dict = get_task_dict(sys.argv[1])

task_start = int(time.time())

# do the real work here
task_input = task_dict.get('input')

# build the content of xml file




# write the xml file
xml_file_name = '.'.join([task_input.get('project_code'), task_input.get('submitter_sample_id'), 'xml'])
xml_file = os.path.join(os.getcwd(), xml_file_name)
with open(xml_file, 'w') as l:
	l.write('this is a test xml file of %s' % task_input.get('submitter_sample_id'))

# get the md5sum and file size of the xml file
xml_file_md5sum = get_md5(xml_file)
xml_file_size = os.path.getsize(xml_file)

# complete the task
task_stop = int(time.time())

output_json = {
    'task_start': task_start,
    'task_stop': task_stop,
    'xml_file': xml_file,
    'xml_file_name': xml_file_name,
    'xml_file_size': xml_file_size,
    'xml_file_md5sum': xml_file_md5sum
}

save_output_json(output_json)

