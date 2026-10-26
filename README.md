# 脆弱性チェッカー(練習用)

自分のパソコンの中だけで動く練習用サーバー(`server.py`)を、C++のチェッカー(`checker.cpp`)で調べるプロジェクトです。

## 中身

| ファイル | 役割 |
|---|---|
| `server.py` | 練習用サーバー。ポート8000は設定が弱いページ、ポート8001はセキュリティ設定をそろえたページ |
| `checker.cpp` | チェッカー本体。いまはヘッダーを表示するだけ |
| `httplib.h` | HTTP通信用のライブラリ(cpp-httplib)。そのまま置いておく |

## 動かし方

1. 画面を2つ開く(ターミナルを2つ)
2. 1つ目で練習用サーバーを動かす

   ```
   python3 server.py
   ```

   Windowsで `python3` が動かないときは `python server.py`

3. 2つ目でコンパイルして実行する

   ```
   g++ -std=c++17 -pthread checker.cpp -o checker
   ./checker
   ```

   Windows(MinGW)のときは、コンパイルの最後に `-lws2_32` を付けて、実行は `checker.exe`

4. ポート8001を調べたいときは、`checker.cpp` の `8000` を `8001` に書き換えて、もう一度コンパイルする

## 次にやること

1. 調べたいヘッダー(`Strict-Transport-Security`、`Content-Security-Policy`、`X-Content-Type-Options` など)を、配列(`vector<string>`)に入れる
2. `for` で1つずつ取り出して、`res->has_header("名前")` で付いているか調べる
3. 「OK」「足りない」を表示する
4. 足りないものに、なぜ必要かを一言添える

## 注意

このチェッカーは、自分で用意したもの、自分で管理するもの、許可をもらったものだけに使ってください。
許可なく他人のサイトやサーバーを調べると、不正アクセス禁止法などに触れるおそれがあります。
