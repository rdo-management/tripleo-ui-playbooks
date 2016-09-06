#!/bin/env python

import json
import os
import re
import sys


EXCLUDED_PATTERNS = (
    r""".*\/liberty\/.*""",
    r""".*\.pyc$""",
    r""".*\.pyo$""",
)

URL = 'http://localhost:8585/v1/plans'


def _is_plan_file(file_name):
    for pattern in EXCLUDED_PATTERNS:
        if re.match(pattern, file_name):
            return False
    return True

def _get_template_paths(base_path):
    template_paths = []
    for (dirpath, dirnames, filenames) in os.walk(base_path):
        if len(filenames) > 0:
            template_paths.extend([os.path.join(dirpath, f) for f in filenames
                                   if _is_plan_file(os.path.join(dirpath, f))])
    return template_paths

def _get_plan_data(template_paths, base_path):
    data = {}
    for path in template_paths:
        with open(path, 'r') as f:
            file_key = path.replace(base_path, '')
            data[file_key] = {}
            data[file_key]['contents'] = f.read()
            if 'capabilities-map.yaml' in path:
                data[file_key]['meta'] = {
                    'file-type': 'capabilities-map'
                }
    return data

def run(args):
    template_paths = _get_template_paths(args[0])
    plan_data = _get_plan_data(template_paths, args[0])
    print(json.dumps({
        'files': plan_data,
        'name': args[1]
    }))


if __name__ == '__main__':
    run(sys.argv[1:])
