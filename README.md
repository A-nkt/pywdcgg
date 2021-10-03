this repository can be use for analysis of [WDCGG](https://gaw.kishou.go.jp/jp) data.

## install
I recommend that you use to ``sys``.

```python
import sys
sys.path.append('pywdcgg')
import pywdcgg as pw
```

I will make setup.py.
I'll let you know how to use pip install.

## Requirement
- pandas

## Quickstart
### get header information

```python
rdat = pw.read_file("ch4_syo_surface-flask_2_3001-9999_event.txt")
info = rdat.about_info()
```

### get value

```python
rdat = pw.read_file("ch4_syo_surface-flask_2_3001-9999_event.txt")
dat = rdat.get_value()
```

## Note
Commentary article (under construction)

if you want to new function related to WDCGG.
please contact me. off course please pull request.

---
### 日本語解説

このリポジトリは、[WDCGG](https://gaw.kishou.go.jp/jp)データの読み込み・解析に使用することができます。

## install
現状、``sys``を用いたimportを推奨します。

```python
import sys
sys.path.append('pywdcgg')
import pywdcgg as pw
```

``setup.py``を作成予定ですので、完成後はそちらを推奨します。

## Requirement
- pandas

## Quickstart

### ヘッダー情報を取得

```python
rdat = pw.read_file("ch4_syo_surface-flask_2_3001-9999_event.txt")
info = rdat.about_info()
```

### データを取得

```python
rdat = pw.read_file("ch4_syo_surface-flask_2_3001-9999_event.txt")
dat = rdat.get_value()
```

## Note
[解説記事](https://qiita.com/dsduoa31/items/52aa6f2bca6cab7ca5c2)

本ライブラリを用いてWDCGGに関する新機能が欲しい場合、ご連絡ください。
勿論、ご自身で開発されてpull requestでも大歓迎です。
