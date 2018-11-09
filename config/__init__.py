__author__ = 'Stephen'

import os, yaml

# Fetch environment from os environment variables
env = os.getenv('ENV', 'production')


def merge_dicts(x,y):
    # store a copy of x, but overwrite with y's values where applicable
    merged = dict(x,**y)

    xkeys = x.keys()

    # if the value of merged[key] was overwritten with y[key]'s value
    # then we need to put back any missing x[key] values
    for key in xkeys:
        # if this key is a dictionary, recurse
        if isinstance(x[key], dict) and y.has_key(key):
            merged[key] = merge_dicts(x[key],y[key])

    return merged

# Merge defaults with environment configuration
with open(os.path.join(os.path.dirname(__file__), 'defaults.yaml'), 'r') as defaults_file,\
        open(os.path.join(os.path.dirname(__file__), env + '.yaml')) as env_file:
    defaults_dict = yaml.load(defaults_file)
    env_dict = yaml.load(env_file)
    config = merge_dicts(defaults_dict, env_dict)


url = config['url']
