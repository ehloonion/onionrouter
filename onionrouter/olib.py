import sys
import os
import re


def cross_input(text):
    """
    Returns the correct input function callback to be used for python 3.x
    and python 2.x
    """
    if sys.version_info[0] < 3:
        return raw_input(text)  # noqa
    return input(text)


def get_full_path_files_for_dir(directory_path):
    """
    List all filepaths in a dir recursively
    """
    return set([os.path.join(dirpath, fname) for dirpath, dirnames, filenames
                in tuple(os.walk(directory_path))
                for fname in filenames])


def find_file(directory_path, filename):
    """
    Find filename in a dir recursively
    """
    return next((x for x in get_full_path_files_for_dir(directory_path)
                 if filename == os.path.split(x)[-1]), None)


def find_files_with_suffix(directory_path, suffix):
    all_files = get_full_path_files_for_dir(directory_path)
    matcher = re.compile(r".*\.{suffix}$".format(suffix=suffix), re.IGNORECASE)
    return (a_file for a_file in all_files if re.match(matcher, a_file))
