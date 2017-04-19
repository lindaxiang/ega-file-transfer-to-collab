#!/usr/bin/env python
import json

with open('output.json', 'w') as f:
  f.write(json.dumps({"task": "upload"}))

