import os.path
import string
import asyncio
import tkinter as tk
from tkinter import *
from tkinter import ttk

# import welcome_win

eText = ''


async def main():
    global eText
    main_win = tk.Tk()
    main_win.resizable(width=False, height=False)
    w = main_win.winfo_screenwidth()  # ширина экрана
    h = main_win.winfo_screenheight()  # высота экрана
    rw = 600
    rh = 300
    w = w // 2 - rw // 2  # середина экрана
    h = h // 2 - rh // 2
    main_win.geometry('{}x{}+{}+{}'.format(rw, rh, w, h))
    main_win.title('Установка русификатора')
    main_win.iconbitmap("ICON2.ico")
    main_win.wm_attributes("-topmost", True)

    textbox_1_label = Label(text="Автоматически определенный путь:", font=('FOT-ANITO STD', '12'))
    textbox_1_label.pack(padx=30, pady=15, anchor=NW)

    Canvas(main_win, bg='white')
    eText = StringVar()
    e = Entry(main_win, width=27, state="readonly", textvariable=eText, font=('FOT-ANITO STD', '12'))
    eText.set("Путь определяется...")
    e.pack(padx=30, anchor=NW, ipadx=100)

    # progress = ttk.Progressbar(main_win, orient=HORIZONTAL, length=500, mode='determinate')
    # progress.pack(padx=30, pady=80, anchor=S)

    await get_path()
    main_win.mainloop()


async def get_path():
    # progress.start()
    global eText
    file_path = ':\\'
    file_name = "hackGU_cmn_a.cpk"
    for letter in string.ascii_uppercase:
        path_file = letter + file_path
        for (current, folders_in_current, files_in_current) in os.walk(path_file):
            for files in files_in_current:
                if files == file_name and files in files_in_current:
                    eText.set(current)
                if files != file_name and files not in files_in_current:
                    eText.set("Путь не найден.")
    return eText

if __name__ == '__main__':
    eText = "Путь определяется..."
    asyncio.run(main())
