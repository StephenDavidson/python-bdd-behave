__author__ = 'Stephen'

import os
import yaml

# Fetch environment from os environment variables
env = os.getenv('ENV', 'production')

# Merge defaults with environment configuration
with open(os.path.join(os.path.dirname(__file__), 'defaults.yaml'), 'r') as defaults_file,\
        open(os.path.join(os.path.dirname(__file__), env + '.yaml')) as env_file:
    defaults_dict = yaml.load(defaults_file, Loader=yaml.FullLoader)
    env_dict = yaml.load(env_file, Loader=yaml.FullLoader)
    config = {**defaults_dict, **env_dict}


url = config['url']
