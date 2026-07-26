from customtkinter import CTk, CTkButton, CTkLabel, CTkEntry
from termcolor import cprint
from subprocess import run

class QpalzmWebSearch:
    def __init__(self, window: CTk) -> None:
        self.window = window
        self.number = 0
        self.window.geometry('300x330')
        self.window.resizable(True, True)
        self.window.wm_title('QPALZM Web Search')
        self.search_entry = CTkEntry(self.window, width=200, corner_radius=5,
                                     placeholder_text='搜索...')
        self.search_entry.place(relx=0.5, rely=0.2, anchor='center')
        self.ba_search_btn = CTkButton(self.window, text='百度搜索',
                                       command=self.ba_search_func, corner_radius=5)
        self.ba_search_btn.place(relx=0.5, rely=0.4, anchor='center')
        self.bi_search_btn = CTkButton(self.window, text='Bing搜索',
                                       command=self.bi_search_func, corner_radius=5)
        self.bi_search_btn.place(relx=0.5, rely=0.6, anchor='center')
        self.enter_url_btn = CTkButton(self.window, text='输入URL',
                                       command=self.enter_url_mfunc, corner_radius=5)
        self.enter_url_btn.place(relx=0.5, rely=0.8, anchor='center')

    def ba_search_func(self):
        try:
            self.number = 1
            run(f'open https://www.baidu.com/s?wd={self.search_entry.get()}&ie=utf-8', shell=True)
        except Exception as e:
            cprint(f'ERROR: {e}', 'red')

    def bi_search_func(self):
        try:
            self.number = 2
            run(f'open https://cn.bing.com/search?q={self.search_entry.get()}', shell=True)
        except Exception as e:
            cprint(f'ERROR: {e}', 'red')

    def enter_url_mfunc(self):
        try:
            self.number = 3
            for widget in self.window.winfo_children():
                widget.destroy()
            o_label1 = CTkLabel(self.window, text='请输入URL',
                                font=('Helvetica bold', 26))
            o_label1.place(relx=0.5, rely=0.4, anchor='center')
            self.o_entry1 = CTkEntry(self.window, width=200, placeholder_text='输入URL链接...',
                                     corner_radius=5)
            self.o_entry1.place(relx=0.5, rely=0.6, anchor='center')
            o_enter_btn = CTkButton(self.window, text='打开网页',
                                         command=self.enter_url_n, corner_radius=5)
            o_enter_btn.place(relx=0.5, rely=0.8, anchor='center')
        except Exception as e:
            cprint(f'ERROR: {e}', 'red')

    def enter_url_n(self):
        try:
            self.number = 4
            run(f'open {self.o_entry1.get()}', shell=True)
        except Exception as e:
            cprint(f'ERROR: {e}', 'red')

if __name__ == '__main__':
    app = CTk()
    gui = QpalzmWebSearch(app)
    app.mainloop()
