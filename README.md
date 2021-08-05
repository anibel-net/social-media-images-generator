# anibel-social-media-images-generator

## Усталёўка

### Windows

1. Спампаваць праграму, распакаваць у любое месца, дзе яна не будзе перашкаджаць (хуткі доступ да папкі з праграмай не будзе патрэбны).

1. Усталяваць Python 3 з [python.org](https://python.org) ці Microsoft Store:
   - Пры ўсталёўкі з python.org неабходна адзначыць "Add Python to PATH":
     
   ![скрыншот](https://i.imgur.com/Wl5lFWy.png)
   - на апошніх версіях Windows 10 гэта можна зрабіць камандай `python`:
     
   ![скрыншот](https://i.imgur.com/7hcQj38.png)
     
2. Запусціць install.cmd, дачакацца ўсталёўкі залежнасцей.

3. У выніку павінен з'явіцца example.cmd, які далей будзе выкарыстоўвацца.

### Linux і мб Mac OS + іншыя Unix/*nix

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Выкарыстоўванне

### Windows

1. Адкрыць example.cmd праз любы рэдактар тэксту, адрэдагаваць наступны блок:
   ```
   set TITLE="ПРЫКЛАД"
   set FORMAT="SUB/DUB"
   set CATEGORY="ANIME/CINEMA"
   set SUBCATEGORY="SERIAL/MOVIE"
   ```

   - TITLE — назва тайтла
   
   - FORMAT — выбар субцітры/агучка (`SUB`/`DUB` адпаведна), заставіць толькі нешта адно.
   
   - CATEGORY — выбар анімэ/кіно (`ANIME`/`CINEMA` адпаведна), заставіць толькі нешта адно.
   
   - SUBCATEGORY — выбар шматсерыйны/аднасерыйны тайтл (`SERIAL`/`MOVIE` адпаведна), заставіць толькі нешта адно.

2. Перацягнуць скрыншот на адрэдагаваны файл:
   
   ![гіфка](https://i.imgur.com/xeFWFkj.gif)

### Linux і мб Mac OS + іншыя Unix/*nix

```shell
source venv/bin/activate
export TITLE="ПРЫКЛАД"
export FORMAT="SUB/DUB"
export CATEGORY="ANIME/CINEMA"
export SUBCATEGORY="SERIAL/MOVIE"
python main.py "$PWD" "$TITLE" "$FORMAT" "$CATEGORY" "$SUBCATEGORY" "<шлях да выявы>"
```