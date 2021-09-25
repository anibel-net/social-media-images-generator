import os
import sys

if __name__ == '__main__':
    if sys.platform == 'win32':
        os.system('python -m venv venv')
        os.system('CALL venv\\scripts\\activate.bat && pip install -r requirements.txt')
        content = """@chcp 65001


set TITLE="ПРЫКЛАД"
set FORMAT="SUB/DUB"
set CATEGORY="ANIME/CINEMA"
set SUBCATEGORY="SERIAL/MOVIE"

cd /d %~dp0

CALL "{WORKDIR}\\venv\\scripts\\activate.bat"
"{WORKDIR}\\venv\\Scripts\\python.exe" "{WORKDIR}\\main.py" "{WORKDIR}" %TITLE% %FORMAT% %CATEGORY% %SUBCATEGORY% %*
""".format(WORKDIR=os.getcwd())
        open('example.cmd', 'wt', encoding='UTF-8').write(content)
    elif sys.platform == 'linux':
        os.system('python3 -m venv venv')
        os.system('source venv/bin/activate; pip install -r requirements.txt')
        content = """#!/bin/sh

export WORKDIR="{WORKDIR}"

export TITLE="ПРЫКЛАД"
export FORMAT="SUB/DUB"
export CATEGORY="ANIME/CINEMA"
export SUBCATEGORY="SERIAL/MOVIE"

source "$WORKDIR/venv/bin/activate"
python "$WORKDIR/main.py" "$WORKDIR" "$TITLE" "$FORMAT" "$CATEGORY" "$SUBCATEGORY" "$@"
""".format(WORKDIR=os.getcwd())
        open('example.sh', 'wt', encoding='UTf-8').write(content)
        os.system('chmod +x example.sh')
    else:
        print('Installer works only on win32 and linux platforms.')
        exit(255)
