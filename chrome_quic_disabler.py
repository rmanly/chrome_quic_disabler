#!/usr/bin/python

import json
import os

path = '~/Library/Application Support/Google/Chrome/Local State'
local_state = os.path.expanduser(path)


def write_json(contents, file=local_state):
    json_contents = json.JSONEncoder().encode(contents)

    with open(local_state, 'w') as f:
        f.write(str(json_contents))


if os.path.exists(local_state):
    with open(local_state) as f:
        contents = json.load(f)

    # enabled == 1, disabled == 2, default == unlisted in local state file
    contents['browser']['enabled_labs_experiments'] = [u'enable-quic@2']

    write_json(contents)
else:
    new_contents = {}
    new_contents[u'browser'] = {u'enabled_labs_experiments': [u'enable-quic@2']}

    write_json(new_contents)
