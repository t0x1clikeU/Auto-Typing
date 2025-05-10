import pyautogui
import pytesseract
from PIL import Image
import time
import keyboard
import json
import os
import string
import pyperclip
import win32gui
import win32con
import sys

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                      win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if os.path.exists(tesseract_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    url = "https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe"
    print("アプリケーションが見つかりません。Tesseractをダウンロードしてください。\ntesseract-ocr-w64-setup-5.5.0.20241111.exe をDLしてください(^^♪")
    print("URLをクリップボードにコピーしました：")
    pyperclip.copy(url)
    print("エンター押して終了してください")
    keyboard.wait('enter')
    sys.exit()

coords_file = "coords.json"

print("アプリケーション :tesseract が見つかりました\n正常に起動しました。\n")

if not os.path.exists(coords_file) or input("新しく座標を選びますか？ (y/n): ").lower() == "y":
    print("\npキーで開始点を指定してください...")
    keyboard.wait('p')
    start_x, start_y = pyautogui.position()
    print(f"開始点: ({start_x}, {start_y})")

    print("再度pキーで終了点を指定してください...")
    keyboard.wait('p')
    end_x, end_y = pyautogui.position()
    print(f"終了点: ({end_x}, {end_y})")

    coords = {
        "left": min(start_x, end_x),
        "top": min(start_y, end_y),
        "right": max(start_x, end_x),
        "bottom": max(start_y, end_y)
    }
    with open(coords_file, "w") as f:
        json.dump(coords, f)
else:
    with open(coords_file, "r") as f:
        coords = json.load(f)


print("ready..")


while True:
    screenshot = pyautogui.screenshot()
    cropped = screenshot.crop((coords["left"], coords["top"], coords["right"], coords["bottom"]))
    text = pytesseract.image_to_string(cropped).strip()
    print("recognition:", text)

    for char in text:
        if char in string.printable:
            pyautogui.typewrite(char)


