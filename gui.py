from distutils.command.build import build
from tkinter import *
from mail import sendemail
from threading import *
from svm_handler import SVMHandler
from gui_util import set_label


def run_gui():
    root = Tk()
    root.title("SVM GUI")
    root.geometry("300x300")
    root.resizable(width=FALSE, height=FALSE)
    mainframe = Frame(root)
    mainframe.pack()
    text = StringVar()
    text_label = text
    set_label(text_label)
    svm_handler = SVMHandler()

    def run_in_thread(fn, *args):
        t1 = Thread(target=fn, args=args)
        t1.start()

    def activate_train():
        if svm_handler.busy:
            return
        run_in_thread(svm_handler.train)

    def activate_test():
        if svm_handler.busy or not svm_handler.has_trained:
            return
        run_in_thread(svm_handler.predict)

    def send_mail():
        if not svm_handler.error_percentage:
            return
        run_in_thread(
            sendemail, f"The error percentage are {svm_handler.error_percentage}"
        )

    greenbutton = Button(
        mainframe,
        text="Train module",
        fg="red",
        height=2,
        width=13,
        command=activate_train,
    )

    bluebutton = Button(
        mainframe,
        text="Test module",
        fg="blue",
        height=2,
        width=13,
        command=activate_test,
    )

    redbutton = Button(
        mainframe,
        text="Send email",
        fg="green",
        height=2,
        width=13,
        command=send_mail,
    )

    label = Label(mainframe, textvariable=text)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=22)

    root.mainloop()


if __name__ == "__main__":
    run_gui()
