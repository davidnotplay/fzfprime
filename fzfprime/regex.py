"""
    :author: David Casado Martínez <dcasadomartinez@gmail.com>
"""
import re

class MatchObject:
    def __init__(self, match):
        self._match = match

    def __getattr__(self, name):
        try:
            return self._match[name]
        except IndexError:
            try:
                name = int(name)
                return self._match[name]
            except (IndexError, ValueError):
                return None

    def get_groups(self):
        return (self._match[0],) + self._match.groups()

    def get_groupdict(self):
        return self._match.groupdict()

def get_matches(lines, regex):
    for line in lines:
        match = regex.fullmatch(line)

        if match is None:
            continue

        yield MatchObject(match)
