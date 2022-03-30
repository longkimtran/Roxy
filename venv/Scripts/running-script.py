#!D:\Virtual_Assisstance_Project\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'running==0.1.1','console_scripts','running'
__requires__ = 'running==0.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('running==0.1.1', 'console_scripts', 'running')()
    )
