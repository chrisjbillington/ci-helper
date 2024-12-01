import sys
import os
import shutil
import subprocess
import shlex
from setuptools import Command
import json
from textwrap import dedent
import hashlib
from pathlib import Path
import configparser
import re
import itertools

import toml
import distlib.markers


# Command line args that can be used in place of "setup.py" for projects that lack a
# setup.py, runs a minimal setup.py similar to what pip does for projects with no
# setup.py.
_SETUP_PY_STUB = [
    "-c",
    'import sys, setuptools; sys.argv[0] = __file__ = "setup.py"; setuptools.setup()',
]


def setup_py(project_dir):
    """Returns a list of command line arguments to be used in place of ["setup.py"]. If
    setup.py exists, then this is just ["setup.py"]. Otherwise, if setup.cfg or
    pyproject.toml exists, returns args that pass a code snippet to Python with "-c" to
    execute a minimal setup.py calling setuptools.setup(). If none of pyproject.toml,
    setup.cfg, or setup.py exists, raises an exception."""
    if Path(project_dir, 'setup.py').exists():
        return ['setup.py']
    elif any(Path(project_dir, s).exists() for s in ['setup.cfg', 'pyproject.toml']):
        return _SETUP_PY_STUB
    msg = f"""{project_dir} does not look like a python project directory: contains no
        setup.py, setup.cfg, or pyproject.toml"""
    raise RuntimeError(' '.join(msg.split()))


class ci_distinfo(Command):
    description = "Ger info on package purity and platform-dependence of requirements"

    def run(self):
        print("ci_distinfo running")
