from distutils.core import setup
import py2exe
import sys
sys.path.append('lib')
setup(
    name = 'surf',
    description = 'surf the web via proxy',
    version = '1.0',
    windows=[{"script":"main.py", "dest_base": "surf"}],
    options={
        "py2exe":{
        "unbuffered": True,
        "optimize": 2,
        "includes":['sip'],
        "compressed": True,
        "bundle_files": 1
        }
    },
    zipfile = None
)