"""
    :author: David Casado Martínez <dcasadomartinez@gmail.com>
"""
from iterfzf import iterfzf
from fzfprime.toml import get_command_data, TomlError
from fzfprime.regex import get_matches

def parse_transformer(transformer):
    lines = transformer["lines"]
    regex = transformer["regex"]
    key   = transformer["key"]

    # Create the fzf options
    match_dict = {}
    for match in get_matches(lines, regex):
        dkey = key.format(*match.get_groups(), **match.get_groupdict())
        match_dict[dkey] = match

    # create fzf prompt
    options = iterfzf(match_dict.keys())
    if options is None:
        # no option selected.
        return None

    return match_dict[options]


def main():
    try:
        command_data = get_command_data()

        transformers = command_data["transformers"]
        cmd_out      = command_data["cmd_out"]

        for transformer in transformers:
            match = parse_transformer(transformer)
            cmd_out = cmd_out.format(**{transformer["name"]: match})
            print(match.david, cmd_out)


    except TomlError as err:
        # TODO: handler the error here.
        # TODO: Invalid toml syntax.
        raise err

if __name__ == "__main__":
    main()

