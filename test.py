import tkinter

# リストの作成
a = [57, 16, 99, 10, 45]
n = len(a)
print('番号', 'データ')

# コールバック関数
def btn_click():
    for i in range(0,n,1):
        if a[i] == s:
            print(s, 'は', i+1, '番目に存在します')

# ボタン画面の作成
tki = tkinter.Tk()
tki.geometry('300x200')
tki.title('test')

# 探索値の入力
for i in range(0,n,1):
    print(i, ' ', a[i])
print('')
s = int(input('探索値の入力'))

# ボタンクリックイベント
btn = tkinter.Button(tki, text='クリック', command=btn_click)
btn.place(x=140, y=170)

# mainループ
tki.mainloop()