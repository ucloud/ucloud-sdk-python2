

class DocTransformer:
    def __init__(self, replaces=None):
        self.replaces = replaces

    def convert(self, source: str) -> str:
        result = source
        for r in self.replaces:
            result = result.replace(r['from'], r['to'])
        return result
