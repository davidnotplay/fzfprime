"""
    :author: David Casado Martínez <dcasadomartinez@gmail.com>
"""
import re
import toml
from fzfprime.cmd_args import args
from fzfprime.cmd import exec_cmd, CmdError

class Tomld:
    """ Handle the dict fetched from toml file

    Attributes:
        data (dict): Dict where are the data of the toml file.
    """
    def __init__(self):
        self.data = {}

    def set_toml_data(self, data):
        """ Set the value of the `data` attribute

        Args:
            data (dict): New dict for the `data` property
        """
        self.data = data

    def __getitem__(self, name):
        return self.data[name]

tomld = Tomld()

class TomlError(Exception):
    """ Toml base error
    """

def getp(target, *key_tree, error):
    """ Get the value, from the `target` dictionary, using the `key_tree` key tree.

    Args:
        target (dict): Target dictionary that contains the value.
        key_tree (list): Key tree necessary to get the value from the diccionary
        error: Error thrown if one of the key doesn't exist.

    Returns:
        Value of the dictionary
    """
    try:
        for key in key_tree:
            target = target[key]

        return target

    except KeyError as err:
        raise error from err

def get_toml_file():
    """ Get the toml data of the file defined in `args.file`, parse the file and save the results
        in tomld object.

    Raise:
        TomlError: File not found, cannot be opened or is bad formed
    """
    try:
        tomld.set_toml_data(toml.load(args.file))

    except IOError as err:
        raise TomlError("cannot open the file") from err
    except toml.TomlDecodeError as err:
        raise TomlError("toml file bad formed") from err

def get_command_data():
    """ Get the data of the `args.cmd` command, it is defined in toml file.

    Returns:
        (dict): Command data:

        - cmd_out:      Value of the cmd_out property in command.
        - transformers: List with the transformer dict. see get_transformer_data
    """
    try:
        # Open the toml file, get the tomld data and save it in tomld object.
        get_toml_file()

    except TomlError as err:
        message = "file {}: {}".format(args.file, str(err))
        raise TomlError(message) from err

    try:
        # get the command
        cmd = getp(tomld, "command", args.cmd, error=TomlError("command not found"))
        transformer_names = getp(cmd, "transformers", error=TomlError("transformers not found"))
        cmd_out = getp(cmd, "cmd_out", error=TomlError("cmd_out not found"))
        transformers = []

        if not transformer_names:
            raise TomlError("transformer list is empty")

        try:
            for t_name in transformer_names:
                transformers.append(get_transformer_data(t_name))

        except (TomlError, CmdError) as err:
            raise TomlError("transformer {}: {}".format(t_name, err)) from err

        try:
            cmd_out = cmd["cmd_out"]

        except KeyError as err:
            raise TomlError("cmd_out property not found") from err


        return {
            "cmd_out":      cmd_out,
            "transformers": transformers,
        }

    except TomlError as err:
        raise TomlError("command {}: {}".format(args.cmd, err)) from err



def get_transformer_data(transformer_name):
    """ Get, from toml file, the data of the `transformer_name` transformer.

    Args:
        transformer_name (str): Transformer name

    Returns:
        dict: Transformer data.

        The dict has got the next properties:

        - name:   Transformer name
        - lines: `list` transformer property or splitted result of execute the command defined in
                 `cmd` transformer property.
        - regex:  Regular expression object created using the Regular expression defined in
                  `regex` transformer property. Optional property. By default is `.*`
        - key:    Expression format used in fzf options. The format is fetched from the `key`
                  transformer property. Optional property. By default is `{}`
    """

    error = TomlError("transformer not found")
    transformer = getp(tomld, "transformer", transformer_name, error=error)

    cmd       = transformer.get("cmd")
    lines     = transformer.get("list")
    regex     = transformer.get("regex", ".*")
    key       = transformer.get("key", "{}")

    if cmd is None and lines is None:
        raise TomlError("cmd property or list property not found")

    if cmd is not None:
        lines = exec_cmd(cmd).split("\n")

    try:
        regex = re.compile(regex)
    except re.error as err:
        raise TomlError("regular expression {} is invalid: {}".format(regex, err)) from err

    return {
        "lines": lines,
        "regex": regex,
        "key":   key,
        "name":  transformer_name,
    }
