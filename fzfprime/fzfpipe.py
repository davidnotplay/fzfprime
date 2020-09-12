"""
    Fzf prompt
"""
import os
import toml
from fzf_prime.args_parser import args
from fzf_prime.toml import parse_tom_file, parse_command
# import subprocess
# import sys
# import re


def parse_transformer(tomld, transf_name):
    print (transf_name)



def main():
    parse_tom_file()
    for cmd in args.cmd:
        parse_command(cmd)

# from iterfzf import iterfzf
# from fzfpipe.args_parser import args
# from fzfpipe.utils import get_item
# from fzfpipe.regex import get_re_match, transform_expression

# class CmdException (Exception):
#     def __init__(self, cmd, error):
#         message = "Executing %s command: %s" % (cmd, error)
#         super().__init__(message)

# def exec_cmd(command):
#     try:
#         result = subprocess.run(
#             command,
#             shell=True,
#             check=True,
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#         )
#         return result.stdout.decode("utf-8").strip()
#     except subprocess.CalledProcessError as err:
#         raise CmdException(err.cmd, err.stderr.decode("utf-8")) from err

# def get_matches(lines, regex, line_format):
#     regex = re.compile(regex)
#     match_dict = {}

#     for line in lines:
#         match = get_re_match(line, regex)

#         if match is None:
#             continue

#         key = transform_expression(line_format, match)
#         match_dict[key] = match


#     return match_dict

# # def apply_output_command(match_selected, option_key):
# #     o_cmd = args.o_cmd
# #     if o_cmd is None:
# #         print(option_key)
# #         sys.exit(0)

# #     o_cmd = transform_expression(o_cmd, match_selected)
# #     exec_cmd(o_cmd)

# def process_one_loop(index, i_cmd, regex, line_format, o_cmd):
#     result = exec_cmd(i_cmd)
#     lines = (line for line in result.split("\n") if line.strip() != "")
#     regex = re.compile(regex)

#     matches = get_matches(lines, regex, line_format)
#     fzf_options_selected = iterfzf(matches.keys())

#     if fzf_options_selected is not None:
#         o_cmd = transform_expression(o_cmd, matches[fzf_options_selected])

#     return o_cmd



# def main():
#     pass
#     # out_cmd = args.o_cmd or "%0"
#     # # TODO include exceptions
#     # for index, i_cmd in enumerate(args.i_cmd):
#     #     regex = get_item(args.regex, index, ".*")
#     #     line_format = get_item(args.line_format, index, "%0")

#     #     out_cmd = process_one_loop(index, i_cmd, regex, line_format, out_cmd)

#     # if not args.show:
#     #     exec_cmd(out_cmd)
#     # else:
#     #     print (out_cmd)

#     # print(args.i_cmd)

#     # try:
#     #     matches = get_matches(get_input_text())
#     #     option_selected = iterfzf(matches.keys())

#     #     if option_selected is None:
#     #         sys.exit(0) # No option selected

#     #     apply_output_command(matches[option_selected], option_selected)

#     # except CmdException as err:
#     #     raise err # @TODO handle errors
