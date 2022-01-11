from bs4 import BeautifulSoup
import requests
import tkinter as tk

root = tk.Tk()
root.title("しりとり")
root.geometry("300x300")

txt = tk.Entry(root)
txt.pack(side="top")
answer = tk.StringVar()
btn = tk.Label(root, text="", textvariable=answer)
btn.pack(side="top")
nn = tk.StringVar()
btn = tk.Label(root, text="", textvariable=nn)
btn.pack(side="top")


def key_word():
    get = str(txt.get())
    x = get[-1]
    if x == "ん":
        global nn
        nn.set("んっていったからお前のまけー！！")
    else:
        url = f"https://xn--68j8a5fb.net/%E3%80%8C{x}%E3%80%8D%E3%81%8B%E3%82%89%E3%81%AF%E3%81%98%E3%81%BE%E3%82%8B%E8%A8%80%E8%91%89/"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        found = soup.find('td', class_='column-1').text

        global answer
        answer.set(found)


btn = tk.Button(root, text="決定", command=key_word)
btn.pack(side="top")

lb = tk.Label(root, text="最後の文字は絶対にひらがなにしてください\nプログラムからの返答がない場合はエラーの可能性が高いです\n[を]などは対応しておりません...sry")
lb.pack(side="top")

root.mainloop()
