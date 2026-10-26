#include "httplib.h"

#include <iostream>
using namespace std;

int main() {
    // チェックする場所。8000 は設定が弱いページ、8001 はそろえたページ
    httplib::Client cli("127.0.0.1", 8000);

    auto res = cli.Get("/");
    if (!res) {
        cout << "接続できませんでした。server.py は動いていますか?" << endl;
        return 1;
    }

    cout << "ステータス: " << res->status << endl;
    for (auto &h : res->headers) {
        cout << h.first << " : " << h.second << endl;
    }

    if (res->has_header("Strict-Transport-Security")) {
        cout << "OK: Strict-Transport-Security" << endl;
    } else {
        cout << "足りない: Strict-Transport-Security" << endl;
    }

    if (res->has_header("Content-Security-Policy")) {
        cout << "OK: Content-Security-Policy" << endl;
    } else {
        cout << "足りない: Content-Security-Policy" << endl;
    }

    if (res->has_header("X-Content-Type-Options")) {
        cout << "OK: X-Content-Type-Options" << endl;
    } else {
        cout << "足りない: X-Content-Type-Options" << endl;
    }

    if (res->has_header("X-Frame-Options")) {
        cout << "OK: X-Frame-Options" << endl;
    } else {
        cout << "足りない: X-Frame-Options" << endl;
    }

    if (res->has_header("Referrer-Policy")) {
        cout << "OK: Referrer-Policy" << endl;
    } else {
        cout << "足りない: Referrer-Policy" << endl;
    }

    return 0;
}