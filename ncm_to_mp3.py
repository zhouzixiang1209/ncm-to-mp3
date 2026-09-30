import os
from ncmdump import dump
import tkinter as tk
from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD


def convert_ncm(file_path):
    if not file_path.lower().endswith(".ncm"):
        return

    output_path = file_path[:-4] + ".mp3"
    try:
        dump(file_path, output_path)
    except Exception as e:
        messagebox.showerror("错误", f"{file_path}\n转换失败\n{e}")


def drop(event):
    files = root.tk.splitlist(event.data)
    for file in files:
        convert_ncm(file)

    messagebox.showinfo("完成", "转换完成！")


# GUI 主窗口
root = TkinterDnD.Tk()
root.title("NCM 转 MP3")
root.geometry("420x200")
root.resizable(False, False)

label = tk.Label(
    root,
    text="把 .ncm 文件拖到这里\n\n会自动生成 mp3",
    width=40,
    height=8,
    relief="ridge",
    bg="#f0f0f0",
    font=("微软雅黑", 11)
)
label.pack(padx=20, pady=20)

label.drop_target_register(DND_FILES)
label.dnd_bind("<<Drop>>", drop)

root.mainloop()
