import ast

import astor


class SDK3to2Transformer(ast.NodeTransformer):
    UTF8_HEADER = '# -*- coding: utf-8 -*-\n\n'

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
            if isinstance(child, ast.FunctionDef):
                body.append(self.visit_FunctionDef(child))
            elif isinstance(child, ast.AnnAssign):
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

    def convert(self, source: str) -> str:
        ast_node = ast.parse(source)
        ast_node = self.visit(ast_node)
        return self.UTF8_HEADER + astor.to_source(ast_node)
