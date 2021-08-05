import os

if __name__ == '__main__':
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
