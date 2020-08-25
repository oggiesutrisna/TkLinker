import tkinter as tk
import pyshorteners #import this as the library for shorteners

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack() #canvas to take out the agile 

label1 = tk.Label(root, text='Shortner Link Personal Use version')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Paste the link that you copied')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def getLinker():
    x1 = entry1.get()

    label3 = tk.Label(root, text='The Shortlink is ' + x1 + ' is:', font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

    label4 = tk.Label(root, label=pyshorteners.Shortener().tinyurl.short(x1))
    canvas1.create_window(200, 230, window=label4)


button1 = tk.Button(text='Get Shortner Link', command=getLinker, bg='black', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()