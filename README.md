# vuln-checker

自分のサイトのセキュリティ設定を調べる、C++製の小さなチェッカーです。
Webサーバーが返す「セキュリティヘッダー」が付いているかを調べて、「OK」か「足りない」かを表示します。

## チェックしているヘッダー

| ヘッダー | 役割 |
|---|---|
| Strict-Transport-Security | HTTPSでの接続を強制する |
| Content-Security-Policy | 読み込んでよいスクリプトなどを制限して、XSSの被害を減らす |
| X-Content-Type-Options | ブラウザによるファイル形式の推測を防ぐ |
| X-Frame-Options | 他のサイトの枠の中に埋め込まれるのを防ぐ |
| Referrer-Policy | 他のサイトに送る参照元の情報を制限する |

## ファイル

| ファイル | 役割 |
|---|---|
| `checker.cpp` | チェッカー本体 |
| `server.py` | 練習用サーバー。ポート8000は設定が弱いページ、ポート8001はヘッダーをそろえたページ |
| `httplib.h` | HTTP通信用ライブラリ([cpp-httplib](https://github.com/yhirose/cpp-httplib)) |

## 動かし方(Windows)

ターミナルを2つ開きます。

1つ目で、練習用サーバーを動かします。

```
python server.py
```

2つ目で、コンパイルして実行します。

```
g++ -std=c++17 -pthread checker.cpp -o checker -lws2_32
chcp 65001
./checker
```

Mac / Linux の場合は、`python3 server.py` と、`-lws2_32` なしのコンパイルで動かします。

`checker.cpp` の `8000` を `8001` に書き換えると、ヘッダーをそろえたページを調べられます。

## 実行結果の例

ポート8000(設定が弱いページ)

```
足りない: Strict-Transport-Security
足りない: Content-Security-Policy
足りない: X-Content-Type-Options
足りない: X-Frame-Options
足りない: Referrer-Policy
```

ポート8001(ヘッダーをそろえたページ)

```
OK: Strict-Transport-Security
OK: Content-Security-Policy
OK: X-Content-Type-Options
OK: X-Frame-Options
OK: Referrer-Policy
```

## 今後やること

- 同じ形が5回並んでいる部分を、`vector` と `for` でまとめる
- 調べる場所(URL・ポート)を、プログラムの外から指定できるようにする
- 足りない設定ごとに、「なぜ必要か」「どう直すか」を表示する

## 注意

このツールは、自分で用意したもの、自分で管理するもの、許可をもらったものだけに使ってください。
許可なく他人のサイトやサーバーを調べると、不正アクセス禁止法などに触れるおそれがあります。
