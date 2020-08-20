# %%
# !/usr/bin/python
# -*- coding: UTF-8 -*-


import os
from PIL import Image
import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Label


class PhotoConcat(object):
    def __init__(self):
        self.width_size = 1184  # 宽
        self.row_patch = 10

        self.root = tkinter.Tk()
        self.root.geometry("300x160")
        v1 = Label(self.root, text='宽度：').place(x=30, y=30)
        v2 = Label(self.root, text='间隔：').place(x=30, y=70)
        # 创建一个输入框,并设置尺寸
        self.width_input = tkinter.Entry(self.root, textvariable=v1)
        self.row_input = tkinter.Entry(self.root, textvariable=v2)
        self.width_input.place(x=80, y=30)
        self.row_input.place(x=80, y=70)

        self.root.title("图片拼接")
        self.result_button = tkinter.Button(self.root, text="选择文件夹", command=self.functl)

        # self.path = self.btn1.getvar()

    def concat(self):
        imghigh = sum([len(x) for _, _, x in os.walk(os.path.dirname(self.path))])  # 获取当前文件路径下的文件个数
        imagefile = []
        reshigh = (imghigh - 1) * self.row_patch
        for root, dirs, files in os.walk(self.path):
            for f in files:
                img = Image.open(self.path + f)
                imagefile.append(img)
                bbox = img.getbbox()
                reshigh = reshigh + int(bbox[3] / bbox[2] * self.width_size)

        target = Image.new('RGB', (self.width_size, reshigh), color=(255, 255, 255))  # 最终拼接的图像的大小
        left = 0
        for image in imagefile:
            bbox = image.getbbox()
            high_size = int(bbox[3] / bbox[2] * self.width_size)
            image = image.resize((self.width_size, high_size), resample=0)
            target.paste(image, (0, left))

            left += high_size + self.row_patch  # 从上往下拼接，左上角的纵坐标递增
            target.save(self.path + 'result.jpg', quality=100)

    def functl(self):
        dir = filedialog.askdirectory()  # 返回目录名
        self.path = dir + '/'
        self.width_size = int(self.width_input.get())
        self.row_patch = int(self.row_input.get())
        self.concat()
        messagebox.showinfo('提示', '拼图完成')

    # 完成布局
    def gui_arrang(self):
        # self.width_input.pack()
        self.result_button.place(x=120, y=120)
        # self.result_button.pack()


def main():
    PC = PhotoConcat()
    PC.gui_arrang()
    # 主程序执行
    tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()

# %%
