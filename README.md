# Auto Typer

---

## 🧾 必要環境

- Windows OS
- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract/releases)
- 下記 Python ライブラリ

## 📂 ファイル構成
```
├─ main.py                # メインスクリプト
├─ coords.json            # 座標データ(初回起動で生成される)
```

```bash
pip install pyautogui pytesseract pillow keyboard pyperclip pywin32
```
## 🛠️ 使い方
1. `main.py` を実行します。
2. 初回起動時、Tesseract の存在を確認します。インストールされていない場合はダウンロードリンクが表示され、URLが自動でクリップボードにコピーされます。
3. 座標の選択：
   - `y` を入力すると新しい座標を選べます。
   - `p` キーで「開始位置」を指定。
   - もう一度 `p` キーで「終了位置」を指定。
   - 選択範囲が `coords.json` に保存されます（次回から自動読み込み）。
4. 認識されたテキストが自動的にキーボード入力されます。
5. スクリプトを終了するには、ウィンドウを閉じるか `Ctrl + C` で停止してください。

使用動画
[Youtube](https://www.youtube.com/watch?v=hsmz4dzfpfI)
