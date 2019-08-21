import os
import json

from scripts.migrate._migrate import Migrate, Config, PluginConfig


DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='argument parser')
    parser.add_argument('--source', required=True,
                        help='source code file writen by python3')
    parser.add_argument('--output', required=True,
                        help='output source code file writen by python2')
    parser.add_argument('--config', required=False,
                        help='the configuration file for migration processing')

    with open(DEFAULT_CONFIG_PATH) as f:
        d = json.load(f)

    config = Config()
    config.plugins = [PluginConfig(**plugin) for plugin in d['plugins']]
    print(config.__dict__)

    args = parser.parse_args()
    migrate = Migrate(config)
    migrate.run(args.source, args.output)
