#!D:\Virtual_Assisstance_Project\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'python-weather==0.3.7','console_scripts','weather'
__requires__ = 'python-weather==0.3.7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('python-weather==0.3.7', 'console_scripts', 'weather')()
    )
