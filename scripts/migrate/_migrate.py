# -*- coding: utf-8 -*-
import itertools
import os
import typing
import logging
import dataclasses

from scripts.migrate._plugin_py3to2 import SDK3to2Transformer
from scripts.migrate._plugin_doc import DocTransformer

logging.basicConfig()
logger = logging.getLogger(__name__)


@dataclasses.dataclass
class PluginConfig:
    name: str
    ext: typing.List[str] = None
    options: dict = None


class Config:
    paths: typing.List[str] = []
    plugins: typing.List[PluginConfig] = []


class Migrate(object):
    default_plugins_classes = {
        "py3to2": SDK3to2Transformer,
        "doc": DocTransformer,
    }

    def __init__(self, config: Config = None):
        self.plugins = {}
        self.ext = {}
        for plugin in config.plugins:
            plugin_cls = self.default_plugins_classes.get(plugin.name)
            if plugin_cls is None:
                continue

            plugin_inst = plugin_cls(**(plugin.options or {}))
            self.plugins[plugin.name] = plugin_inst

            for ext in plugin.ext:
                self.ext.setdefault(ext, list())
                self.ext[ext].append(plugin_inst)

        self.paths = config.paths

    def find_python_files(self, dir_or_file):
        if os.path.isdir(dir_or_file):
            for folder, _, files in list(os.walk(dir_or_file)):
                for file in files:
                    yield folder + os.path.sep + file
        else:
            yield dir_or_file

    def run(self, source_path: str, output_path: str):
        for path in self.find_python_files(source_path):
            # find plugins by file extension
            plugins = [plugins for ext, plugins in self.ext.items() if path.endswith(ext)]
            plugins = plugins and plugins[0]

            # skip unexpected file by file extension
            if not plugins:
                continue

            # resolve path
            relative_path = os.path.relpath(path, source_path)
            result_path = os.path.abspath(os.path.join(output_path, relative_path))
            print('migrate {} to {}'.format(path, result_path))

            # read source code
            with open(path, encoding='utf-8') as f:
                source_code = f.read()

            # convert destination code
            output_code = source_code
            for plugin in plugins:
                output_code = plugin.convert(source_code)

            # output to file
            os.makedirs(os.path.dirname(result_path), exist_ok=True)

            with open(result_path, 'w', encoding='utf-8') as f:
                f.write(output_code)
