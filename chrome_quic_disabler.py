#!/usr/bin/python

import json
import os

chrome_dir = os.path.expanduser('~/Library/Application Support/Google/Chrome/')
local_state = os.path.join(chrome_dir, 'Local State')


def write_json(contents, file=local_state):
    json_contents = json.JSONEncoder().encode(contents)

    with open(file, 'w') as f:
        f.write(str(json_contents))


if os.path.exists(local_state):
    with open(local_state) as f:
        contents = json.load(f)

    # enabled == 1, disabled == 2, default == unlisted in local state file
    contents['browser']['enabled_labs_experiments'] = [u'enable-quic@2']

    write_json(contents)
else:
    if not os.path.exists(chrome_dir):
        os.makedirs(chrome_dir, 0700)

    new_contents = {}
    new_contents[u'browser'] = {u'enabled_labs_experiments': [u'enable-quic@2']}

    write_json(new_contents)
