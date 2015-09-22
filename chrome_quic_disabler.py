#!/usr/bin/python

import json
import os

path = '~/Library/Application Support/Google/Chrome/Local State'
local_state = os.path.expanduser(path)

if os.path.exists(local_state):
    with open(local_state) as f:
        contents = json.load(f)

    # enabled == 1, disabled == 2, default == unlisted in local state file
    contents['browser']['enabled_labs_experiments'] = [u'enable-quic@2']

    # I got an error the first time I wrote this out because
    # I forgot to turn it back into proper JSON
    json_contents = json.JSONEncoder().encode(contents)

    with open(local_state, 'w') as f:
        f.write(str(json_contents))
else:
    new_contents = {}
    new_contents[u'browser'] = {u'enabled_labs_experiments': [u'enable-quic@2']}
    json_contents = json.JSONEncoder().encode(new_contents)

    with open(local_state, 'w') as f:
       f.write(json_contents) 
