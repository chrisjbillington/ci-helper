import os
from setuptools import setup

# Normally packages don't have to do this - the dist_conda command should be
# automatically available. But since we're installing it, it isn't there yet!
from ci_helper.ci_distinfo import ci_distinfo
CMDCLASS = {'ci_distinfo': ci_distinfo}

VERSION_SCHEME = {
    "version_scheme": os.getenv("SCM_VERSION_SCHEME", "guess-next-dev"),
    "local_scheme": os.getenv("SCM_LOCAL_SCHEME", "node-and-date"),
}

setup(
    use_scm_version=VERSION_SCHEME,
    cmdclass=CMDCLASS,
)
