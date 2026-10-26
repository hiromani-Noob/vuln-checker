# server.py - 脆弱性チェッカーの練習用ローカルサーバー
#
# 使い方:  python3 server.py   (止めるときは Ctrl+C)
#
#   http://127.0.0.1:8000  ... セキュリティ設定が「弱い」ページ(チェッカーに NG を出させたい)
#   http://127.0.0.1:8001  ... セキュリティ設定を「そろえた」ページ(チェッカーに OK を出させたい)
#
# 127.0.0.1 は「自分のパソコン自身」という意味で、外からはアクセスできません。
# 自分で用意した場所だけをチェックする練習用です。

import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

PAGE = """<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>テストページ</title>
</head>
<body>
  <h1>脆弱性チェッカーの練習用ページ</h1>
  <p>このページは、自分のパソコンの中だけで動いています。</p>
</body>
</html>
""".encode("utf-8")

# 「そろえた」ほうのサーバーが返すセキュリティ関連ヘッダー
# (Strict-Transport-Security は本来 HTTPS で意味を持つ設定。ここでは練習用に付けているだけ)
SECURE_HEADERS = {
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Content-Security-Policy": "default-src 'self'",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
}


def make_handler(extra_headers):
    class Handler(BaseHTTPRequestHandler):
        def send_common_headers(self):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(PAGE)))
            for name, value in extra_headers.items():
                self.send_header(name, value)
            self.end_headers()

        def do_GET(self):
            self.send_common_headers()
            self.wfile.write(PAGE)

        def do_HEAD(self):
            self.send_common_headers()

    return Handler


def run(port, extra_headers):
    server = HTTPServer(("127.0.0.1", port), make_handler(extra_headers))
    server.serve_forever()


if __name__ == "__main__":
    # 「そろえた」ほうは別スレッドで動かす
    threading.Thread(target=run, args=(8001, SECURE_HEADERS), daemon=True).start()
    print("練習用サーバーを起動しました")
    print("  弱い設定  : http://127.0.0.1:8000")
    print("  そろえた設定: http://127.0.0.1:8001")
    print("止めるときは Ctrl+C")
    try:
        run(8000, {})  # 「弱い」ほうは追加ヘッダーなし
    except KeyboardInterrupt:
        print("\n終了します")
