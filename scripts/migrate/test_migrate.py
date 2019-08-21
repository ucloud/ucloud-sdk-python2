import ast
import astor
import pytest

from scripts.migrate._plugin_py3to2 import SDK3to2Transformer


@pytest.mark.parametrize(
    "input_vector,expected",
    [
        ("foo: int = 42", "foo = 42"),
        ("def fn(foo: str) -> int: pass", "def fn(foo):\n    pass"),
        ("class Foo: pass", "class Foo(object):\n    pass"),
        ("import typing", ""),
        ("str(value)", "unicode(value)"),
        ("def deco(fn: typing.Callable[[Client, dict], dict]): pass", "def deco(fn):\n    pass"),
        ("""
def step(self, **kwargs):
    def deco(fn: typing.Callable[[Client, dict], dict]):
        return fn
    return deco
        """, """
def step(self, **kwargs):
    def deco(fn):
        return fn
    return deco
        """),
    ],
)
def test_transformer(input_vector, expected):
    transformer = SDK3to2Transformer()
    result = transformer.convert(input_vector)
    assert result == astor.to_source(ast.parse(expected))


def test_parse_ast():
    input_vector = """
def step(self, **kwargs):
    def deco(fn: typing.Callable[[Client, dict], dict]):
        return fn
    return deco
    """
    node = ast.parse(input_vector)
    print(astor.dump_tree(node))
