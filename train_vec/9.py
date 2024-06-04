import re


def main(x):
    matches = re.findall(r"new\s+(\w+)\s*is\s*\[\s*([#\-\d\s#]+)\s*\]", x)
    return [(name, list(map(int, re.findall(r'-?\d+', values))))
            for name, values in matches]
