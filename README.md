[Magyar leírás lent]
# Music name exporter

Music file name --> author + title converter

### Introduction

If your music files have meta tags, it is better to export that, but if they don't have them, you need to export the artist and the title from the file name. That's what this small script does.
The sript chenges the first '-' to a TAB, so it is easily copyable to excel. Other informations in the file name will be removed, if those are in parentheses.

### How to

- Config the export.py file

```
file = 'Your output txt file'
folder = 'Your input folder'
```

Input: a **folder** that contains mp3 or wav files (of course, it is changeble in the script). The script is **recursive**, so sub-folders will be automatically added.

Output:

```
Blasterjaxx	 Gasolina Bootleg
Blasterjaxx	 Rio
Blasterjaxx Timmy Trumpet	 Narco
BLR x Rave Crave	 Taj
Bomfunk MC s	 Freestyler
```


# Zene fájlnévből előadó + dalcím átalakító

Ez a script a megadott mappában található mp3 és wav fájlok neveit menti ki excelbe másolható formában. Ha a zeneszámok meta címkéi tartalmaznak adatokat, érdemesebb onnan kiexportálni, de ha csak a fájlnév áll rendelkezésre, akkor ez a kis script segíthet.
A fájlnév első kötőjele egy TAB-ra lesz cserélve, ezért excelbe könnyen bemásolható külön oszlopba. Ha a DJ szövetségnek vagy a Mahasznak készítünk listát, mindenképpen nézzük át; ez a program nem helyettesíti a munkánkat, inkább csak felgyorsítja, a kész listát elég utólag átnézni.

### Használati utasítás

- Konfiguráljuk az export.py fájlt

```
file = 'Kimeneti txt fájl'
folder = 'Bemeneti mappa'
```

Bemenet: az a **mappa** ami tartalmazza az mp3 vagy wav fájlokat (természetesen a szkriptben ez átírható). A program **rekurzív**, tehát az almappák automatikusan feltérképezésre kerülnek.

Kimenet:

```
Blasterjaxx	 Gasolina Bootleg
Blasterjaxx	 Rio
Blasterjaxx Timmy Trumpet	 Narco
BLR x Rave Crave	 Taj
Bomfunk MC s	 Freestyler
```
