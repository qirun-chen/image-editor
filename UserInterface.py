# coding=utf-8
from Tkinter import *
import tkFileDialog
import tkMessageBox
from FileProcessor import FileProcessor


class UserInterface:

    def __init__(self):

        self.root = Tk()
        self.root.title(u"身份证认证")
        self.root.geometry('470x320')
        ########
        self.frm = Frame(self.root)
        # Top
        Label(self.root, text=u"批量修改身份证".encode('utf8'), font=('Arial', 15)).pack()
        self.frm = Frame(self.root)
        # Top
        self.frm_T = Frame(self.frm)
        self.frm_T1 = Frame(self.frm_T)
        self.frm_T2 = Frame(self.frm_T)

        self.text_input_path = StringVar()
        self.text_output_path = StringVar()

        Label(self.frm_T1, text=u'身份证名单路径:'.encode('utf8'), font=('Arial', 12)).pack(side=LEFT)
        Label(self.frm_T1, textvariable=self.text_input_path, font=('Verdana', 15)).pack(side=RIGHT)
        self.frm_T1.pack(side=TOP)

        Button(self.frm_T2, text=u"选择".encode('utf-8'), command=self.input_button_click, width=15, height=3,
               font=('Arial', 10)).pack()
        self.frm_T2.pack(side=BOTTOM)
        self.frm_T.pack(side=TOP)

        # middle
        self.frm_M = Frame(self.frm)
        self.frm_M1 = Frame(self.frm_M)
        self.frm_M2 = Frame(self.frm_M)

        Label(self.frm_M1, text=u'图片输出路径:'.encode('utf8'), font=('Arial', 12)).pack(side=LEFT)
        Label(self.frm_M1, textvariable=self.text_output_path, font=('Verdana', 15)).pack(side=RIGHT)
        self.frm_M1.pack()
        Button(self.frm_M2, text=u"选择".encode('utf-8'), command=self.output_button_click, width=15, height=3,
               font=('Arial', 10)).pack()
        self.frm_M2.pack()
        self.frm_M.pack()

        # bottom
        self.frm_B = Frame(self.frm)
        self.frm_B1 = Frame(self.frm_B)
        self.frm_B2 = Frame(self.frm_B)
        self.text_status_prompt = StringVar('')

        Label(self.frm_B1, textvariable=self.text_status_prompt, font=('Arial', 12)).pack(side=LEFT)
        Button(self.frm_B2, text=u"开始修改".encode('utf-8'), command=self.editing_images, width=15, height=2,
               font=('Arial', 10)).pack()
        self.frm_B1.pack()
        self.frm_B2.pack()
        self.frm_B.pack(side=BOTTOM)

        self.frm.pack()
        ########

    def input_button_click(self):
        filename = tkFileDialog.askopenfilename()
        print filename
        self.text_input_path.set(filename)

    def output_button_click(self):
        filename = tkFileDialog.askdirectory()
        self.text_output_path.set(filename)

    def judge_user_input_or_not(self):
        alert_message = StringVar()

        if len(self.text_input_path.get()) == 0:
            alert_message.set(alert_message.get() + u"Please choose an input directory\n")

        if len(self.text_output_path.get()) == 0:
            alert_message.set(alert_message.get() + u"Please choose an export directory!\n")

        if len(alert_message.get()):
            tkMessageBox.showwarning(u"Warning", alert_message.get())

    def editing_images(self):

        self.judge_user_input_or_not()

        file_handler = FileProcessor(self.text_input_path.get())

        if not file_handler.data_exist():
            tkMessageBox.showerror(u"Error", u"表格为空!\n")
            return

        name_id_dict = dict()
        name_id_dict = file_handler.parse_sheet()

        for k, v in name_id_dict.iteritems():
            print k, 'maps to', v


if __name__ == "__main__":
    d = UserInterface()
    mainloop()

