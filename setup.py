#coding:GB2312

from distutils.core import setup
import py2exe
import sys
import os
import shutil
sys.path.append('lib')

def _translate(text):
    return unicode(text, 'gb2312', 'ignore')

setup(
    name = 'surf',
    description = _translate('CATR测试专用'),
    version = '1.3',
    url='http://www.catr.cn',
    author = 'luocheng',
    data_files=[
        ('imageformats', [r'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qico4.dll']),
        ("res", [r".\res\surf.ico"])
    ],
    windows=[{"script":"start.py", "icon_resources": [(1, r'.\res\surf.ico')],
              "dest_base": "surf", "copyright": "Copyright \u00A9 2013-2015 CATR"}],
    options={
        "py2exe":{
        "unbuffered": True,
        "optimize": 2,
        "includes":['sip'],
        "compressed": True,
        "dll_excludes":["QtCore4.dll","QtGui4.dll"],
        "bundle_files": 1
        }
    },
    zipfile = None
)

if os.path.isdir('build'):
    shutil.rmtree('build')