from customtkinter import CTk, CTkButton, CTkLabel, CTkEntry
from termcolor import cprint
from subprocess import run

class QpalzmWebSearch:
    def __init__(self, window: CTk) -> None:
        self.window = window
        self.window.geometry('300x330')
        self.window.resizable(False, False)
        self.window.wm_title('QPALZM Web Search')
        self.search_entry = CTkEntry(self.window, width=200, corner_radius=5,
                                     placeholder_text='搜索...')
        self.search_entry.place(relx=0.5, rely=0.2, anchor='center')
        self.baidu_search_btn = CTkButton(self.window, text='百度搜索',
                                       command=self.baidu_search_func, corner_radius=5)
        self.baidu_search_btn.place(relx=0.5, rely=0.4, anchor='center')
        self.bing_search_btn = CTkButton(self.window, text='Bing搜索',
                                       command=self.bing_search_func, corner_radius=5)
        self.bing_search_btn.place(relx=0.5, rely=0.6, anchor='center')
        self.enter_url_btn = CTkButton(self.window, text='输入URL',
                                       command=self.enter_url, corner_radius=5)
        self.enter_url_btn.place(relx=0.5, rely=0.8, anchor='center')

    def baidu_search_func(self):
        try:
            print('Select your operating system.')
            print('1. MacOS')
            print('2. Windows')
            os_type1 = input('Enter: ')
            if int(os_type1) == 1:
                run(f'open https://www.baidu.com/s?wd={self.search_entry.get()}&ie=utf-8', shell=True)
            elif int(os_type1) == 2:
                run(f'start https://www.baidu.com/s?wd={self.search_entry.get()}&ie=utf-8', shell=True)
            else:
                cprint('Please enter a valid number.', 'red')
        except Exception as e:
            cprint(f'ERROR: {e}', 'red')

    def bing_search_func(self):
        try:
            print('Select your operating system.')
            print('1. MacOS')
            print('2. Windows')
            os_type2 = input('Enter: ')
            if int(os_type2) == 1:
                run(f'open https://cn.bing.com/search?q={self.search_entry.get()}', shell=True)
            elif int(os_type2) == 2:
                run(f'start https://cn.bing.com/search?q={self.search_entry.get()}', shell=True)
            else:
                cprint('Please enter a valid number.', 'red')
        except Exception as e:
            cprint(f'ERROR: {e}', 'red')

    def enter_url(self):
        try:
            for widget in self.window.winfo_children():
                widget.destroy()
            label1 = CTkLabel(self.window, text='请输入URL',
                                font=('Helvetica bold', 26))
            label1.place(relx=0.5, rely=0.4, anchor='center')
            self.entry1 = CTkEntry(self.window, width=200, placeholder_text='URL(需加http或https前缀)',
                                     corner_radius=5)
            self.entry1.place(relx=0.5, rely=0.6, anchor='center')
            enter_btn = CTkButton(self.window, text='打开网页',
                                         command=self.enter_url_func, corner_radius=5)
            enter_btn.place(relx=0.5, rely=0.8, anchor='center')
        except Exception as e:
            cprint(f'ERROR: {e}', 'red')

    def enter_url_func(self):
        try:
            run(f'open {self.entry1.get()}', shell=True)
        except Exception as e:
            cprint(f'ERROR: {e}', 'red')

if __name__ == '__main__':
    app = CTk()
    gui = QpalzmWebSearch(app)
    app.mainloop()
