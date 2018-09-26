#!/usr/bin/python3

from requests import post
from subprocess import Popen, PIPE
import json
import re
import os

uri = os.environ['API_URI']
apiKey = os.environ['API_KEY']
masterNode = os.environ['MASTER_NODE']

eventRe = re.compile(r'Info, (Node\d+), Received Central Scene.*scene id=(\d+) in (\d+) seconds\.')

log = Popen(('/usr/bin/tail', '-F', '-n', '0', '/home/hass/hass/OZW_Log.txt'), stdout=PIPE)
while True:
  line = log.stdout.readline()
  if not line:
    break
  line = line.strip().decode('utf-8')

  # Fast match to discard non-info log messages
  if 'Info,' not in line:
    continue

  match = eventRe.search(line)
  if match:
    groups = list(match.groups())
    groups[0] = masterNode
    data = {'button': '_'.join(groups)}
    post(uri, data=json.dumps(data), headers={'Authorization': 'Bearer ' + apiKey, 'content-type': 'application/json'})