"""
    :author: David Casado Martínez <dcasadomartinez@gmail.com>
"""
import subprocess

class CmdError (Exception):
    """ Error thrown when the executed command fails.

    Args:
        cmd (str): Command excecuted
        error (str): Error thrown by the command.

    """
    def __init__(self, cmd, error):
        message = "executing %s command: %s" % (cmd, error)
        super().__init__(message)

def exec_cmd(cmd):
    """ Execute the `cmd` command

    Raises:
        CmdError: Error executing the `cmd` command.

    Args:
        cmd (str): command

    Result:
        str: output of the command.
    """
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.stdout.decode("utf-8").strip()
    except subprocess.CalledProcessError as err:
        raise CmdError(err.cmd, err.stderr.decode("utf-8")) from err
