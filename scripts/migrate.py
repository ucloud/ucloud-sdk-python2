# -*- coding: utf-8 -*-

import os
import ast
import astor
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


class SDK3to2Transformer(ast.NodeTransformer):
    def visit_Import(self, node):
        is_typing = [alias for alias in node.names if alias.name == 'typing']
        return None if is_typing else node

    def visit_AnnAssign(self, node):
        if node.value is None:
            return node
        return ast.Assign(targets=[node.target], value=node.value)

    def visit_FunctionDef(self, node):
        body = []

        # remove type hints
        for arg in node.args.args:
            arg.annotation = None

        if node.args.kwarg:
            node.args.kwarg.annotation = None

        # visit children
        for child in node.body:
            if isinstance(child, ast.AnnAssign):
                body.append(self.visit_AnnAssign(child))
            else:
                body.append(child)

        node.body = body
        node.returns = None
        return node

    def visit_ClassDef(self, node):
        body = []

        # old-style class convert to new-style class
        if not node.bases:
            node.bases = [ast.Name(id='object', ctx=ast.Load())]

        # visit children
        for child in node.body:
            if isinstance(child, ast.FunctionDef):
                body.append(self.visit_FunctionDef(child))
            else:
                body.append(child)

        node.body = body
        return node


UTF8_HEADER = '# -*- coding: utf-8 -*-\n\n'
UNICODE_HEADER = 'from __future__ import unicode_literals\n\n'


class Migrate(object):
    def __init__(self, source, output=None):
        self.source = source
        self.output = output or source
        self.transformer = SDK3to2Transformer()

    def convert(self, source):
        ast_node = ast.parse(source)
        ast_node = self.transformer.visit(ast_node)
        return UTF8_HEADER + astor.to_source(ast_node)

    def find_python_files(self):
        for folder, _, files in list(os.walk(self.source)):
            for file in files:
                yield folder + os.path.sep + file

    def run(self):
        for path in self.find_python_files():
            logger.info('load {}'.format(path))
            relative_path = os.path.relpath(path, self.source)
            with open(path, encoding='utf-8') as f:
                source = f.read()

            code = self.convert(source)

            output_path = os.path.abspath(
                os.path.join(self.output, relative_path))
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(code)
                print('migrated {} to {}'.format(path, output_path))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='argument parser')
    parser.add_argument('--source', required=True,
                        help='source code file writen by python3')
    parser.add_argument('--output', required=True,
                        help='output source code file writen by python2')

    args = parser.parse_args()
    migrate = Migrate(args.source, args.output)
    migrate.run()
