# kybo

## How to

```
python HorseNameCollector.py
python UrlCollector.py
python ExperienceCollector.py
python RandamForest.py
```

## Python Version

python 2.7


## Python files

### HorseNameCollector :
```
http://www.jbis.or.jpから馬の基本情報を取得する。
output 馬の名前, 父親の名前, 母親の名前　形式のCSVファイル
```

### UrlCollector :
```
http://db.netkeiba.comのレース情報があるURLを取得する。
output レース情報があるURL
```

### ExperienceCollector :
```
http://db.netkeiba.comからレース情報を取得する。
output  特徴量のCSVファイル
```

## Bugs
```
HorseNameCollector から出力される馬名に地域名がついている。
例) (USA), (AUS), (FR)
```