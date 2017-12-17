# kybo

## How to

python main.py

## Python Version

python 2.7

## Flow main.py

```
args[stirng][string][string] = GetHorseInfomation();

url = Search(String, String, String);

args[String]*23 = GetExperience(url);

make csv
```

## API

### String String String GetHorseInfomation(void) :
```
http://www.jbis.or.jpから馬の基本情報を取得する。
return 馬の名前, 父親の名前, 母親の名前
```

### String Search(String, String, String) :
```
http://db.netkeiba.comのレース情報があるURLを取得する。
return レース情報があるURL
```

### String Stirng … GetExperience(url) :
```
http://db.netkeiba.comからレース情報を取得する。
return 23のレース結果のデータ
```





