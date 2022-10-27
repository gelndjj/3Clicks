from cgitb import text
import shutil, os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

#MAIN WINDOW
root = Tk()
root.title('3Clicks')
root.geometry('600x300')
root.resizable(0,0)

#CREATE A TAB
tabControl = ttk.Notebook(root)
tabControl.pack(fill='both', expand=True)

#FIRST TAB
tab0 = Frame(tabControl)
tab0.pack(fill='both')
tabControl.add(tab0,text='Copy tree')

#SECOND TAB
tab1 = Frame(tabControl)
tab1.pack(fill='both')
tabControl.add(tab1,text='Copy tree + data')

#THIRD TAB
tab2 = Frame(tabControl)
tab2.pack(fill='both')
tabControl.add(tab2,text='Copy .extension')


#ENTRIES AND LABELS ON FIRST TAB
entry_src = Entry(tab0, width=60, font=('Helvetica', 14, 'italic'), bg='blue', fg='yellow', relief=RIDGE)
entry_src.place(relx=0.50, rely=0.25, anchor=CENTER)
lbl_src = Label(tab0, text='Source', font=('Helvetica', 13, 'italic'))
lbl_src.place(relx=0.06, rely=0.10)
entry_dst = Entry(tab0, width=60, font=('Helvetica', 14, 'italic'), bg='blue', fg='yellow', relief=RIDGE)
entry_dst.place(relx=0.50, rely=0.65, anchor=CENTER)
lbl_dst = Label(tab0, text='Destination', font=('Helvetica', 13, 'italic'))
lbl_dst.place(relx=0.06, rely=0.50)

#ENTRIES AND LABELS ON SECOND TAB
entry_t1_src = Entry(tab1, width=60, font=('Helvetica', 14, 'italic'), bg='blue', fg='yellow', relief=RIDGE)
entry_t1_src.place(relx=0.50, rely=0.25, anchor=CENTER)
lbl_t1_src = Label(tab1, text='Source', font=('Helvetica', 13, 'italic'))
lbl_t1_src.place(relx=0.45, rely=0.10)
entry_t1_dst = Entry(tab1, width=60, font=('Helvetica', 14, 'italic'), bg='blue', fg='yellow', relief=RIDGE)
entry_t1_dst.place(relx=0.50, rely=0.65, anchor=CENTER)
lbl_t1_dst = Label(tab1, text='Destination', font=('Helvetica', 13, 'italic'))
lbl_t1_dst.place(relx=0.43, rely=0.50)

#ENTRIES, LABELS, MENUS ON THIRD TAB
combo_ls_files = [
                'PDF',
                'Text',
                'MS Office',
                'Picture',
                'Music',
                'Video',
                'PY',
]
ls_files_choice = ttk.Combobox(tab2, values = combo_ls_files, width=10)
ls_files_choice.place(relx= 0.05, rely= 0.10)
ls_files_choice.set('select')

entry_t2_src = Entry(tab2, width=60, font=('Helvetica', 14, 'italic'), bg='blue', fg='yellow', relief=RIDGE)
entry_t2_src.place(relx=0.50, rely=0.40, anchor=CENTER)
lbl_t2_src = Label(tab2, text='Source', font=('Helvetica', 13, 'italic'))
lbl_t2_src.place(relx=0.85, rely=0.24)
entry_t2_dst = Entry(tab2, width=60, font=('Helvetica', 14, 'italic'), bg='blue', fg='yellow', relief=RIDGE)
entry_t2_dst.place(relx=0.50, rely=0.75, anchor=CENTER)
lbl_t2_dst = Label(tab2, text='Destination', font=('Helvetica', 13, 'italic'))
lbl_t2_dst.place(relx=0.80, rely=0.59)


#SELECT SOURCE TO TREE COPY
def select_s():
    global pAth_s

    pAth_s = filedialog.askdirectory()
    entry_src.delete(0, 'end')
    entry_src.insert(0, pAth_s)

#SELECT DESTINATION TO TREE COPY
def select_d():
    global pAth_d

    pAth_d = filedialog.askdirectory()
    pre_name = pAth_s.split('/')
    name = pre_name[-1]
    pAth_d = os.path.join(pAth_d, '%s' % name)
    entry_dst.delete(0, 'end')
    entry_dst.insert(0, pAth_d)

#FUNCTION TO COPY TREE WITHOUT FILES
def all_files(dir, files):
    return [x for x in files if os.path.isfile(os.path.join(dir, x))]

#COPY TREE
def copy_tree():
    global root

    try:
        entry_src.delete(0, 'end')
        entry_dst.delete(0, 'end')

        if os.path.exists(pAth_d):
            msg = messagebox.askyesno(message='The destination already exists.\n Do you want to replace it ?')
            if msg == True:
                shutil.rmtree(pAth_d)
                copy_tree()

        else:
            cp = Toplevel(root)
            cp.title('Directories copied')
            cp.geometry('1000x350')
            cp.resizable(0,0)
            cp_field = Text(cp, height=22, width=150, bd=3, relief=SUNKEN)
            cp_field.pack()
            
            btn_cp_copy = Button(cp, text='Copy', command=lambda:cp.clipboard_append(cp_field.get('1.0',END))).place(relx=0.01, rely=0.95, anchor=SW)
            btn_cp_quit = Button(cp, text='Quit', command=lambda:cp.clipboard_append(cp.destroy())).place(relx=0.20, rely=0.95, anchor=SW)

            shutil.copytree(pAth_s, pAth_d, ignore=all_files)
            for root, dirs, files in os.walk(pAth_s):
                for dir in dirs:
                    name = os.path.join(root, dir)
                    cp_field.insert('1.0','%s\n' % name)

    except OSError:
        messagebox.showerror(message='You can\'t copy here.\n Please, change destination path')

#SELECT SOURCE TO DATA COPY
def select_t1_s():
    global pAth_t1_s

    pAth_t1_s = filedialog.askdirectory()
    entry_t1_src.delete(0, 'end')
    entry_t1_src.insert(0, pAth_t1_s)

#SELECT DESTINATION TO DATA COPY
def select_t1_d():
    global pAth_t1_d

    pAth_t1_d = filedialog.askdirectory()
    pre_name_t1 = pAth_t1_s.split('/')
    name_t1 = pre_name_t1[-1]
    pAth_t1_d = os.path.join(pAth_t1_d, '%s' % name_t1)
    entry_t1_dst.delete(0, 'end')
    entry_t1_dst.insert(0, pAth_t1_d)

#COPY DATA
def copy_files():
    global root
    entry_t1_src.delete(0,'end')
    entry_t1_dst.delete(0,'end')

    try:

        if os.path.exists(pAth_t1_d):
            msg = messagebox.askyesno(message='The destination already exists.\n Do you want to replace it ?')
            if msg == True:
                shutil.rmtree(pAth_t1_d)
                copy_files()
        else:
            cp = Toplevel(root)
            cp.title('Files copied')
            cp.geometry('1000x350')
            cp.resizable(0,0)
            cp_field = Text(cp, height=22, width=150, bd=3, relief=SUNKEN)
            cp_field.pack()
            btn_cp_copy = Button(cp, text='Copy', command=lambda:cp.clipboard_append(cp_field.get('1.0',END))).place(relx=0.01, rely=0.95, anchor=SW)
            btn_cp_quit = Button(cp, text='Quit', command=lambda:cp.clipboard_append(cp.destroy())).place(relx=0.20, rely=0.95, anchor=SW)

            shutil.copytree(pAth_t1_s, pAth_t1_d)
            for root, dirs, files in os.walk(pAth_t1_s):
                for file in files:
                    name = os.path.join(root, file)
                    cp_field.insert('1.0','%s\n' % name)
            #messagebox.showinfo(message='Done')

    except OSError:
        messagebox.showerror(message='You can\'t copy here.\n Please, change destination path')

#SELECT SOURCE TO DATA COPY EXTENSIONS
def select_t2_s():
    global pAth_t2_s

    pAth_t2_s = filedialog.askdirectory()
    entry_t2_src.delete(0, 'end')
    entry_t2_src.insert(0, pAth_t2_s)

#SELECT DESTINATION TO DATA COPY EXTENSIONS
def select_t2_d():
    global pAth_t2_d

    pAth_t2_d = filedialog.askdirectory()
    pre_name_t2 = pAth_t2_s.split('/')
    name_t2 = pre_name_t2[-1]
    pAth_t2_d = os.path.join(pAth_t2_d, '%s' % name_t2)
    entry_t2_dst.delete(0, 'end')
    entry_t2_dst.insert(0, pAth_t2_d)

#COPY DATA EXTENSIONS
def copy_files_ext():
    global root
    global cp_field
    dict_ext = {'PDF': ('.pdf','.PDF'),
                'TEXT': ('.txt', '.TXT', '.rtf', '.RTF'),
                'OFFICE': ('.doc', '.DOC', '.docx', '.DOCX', '.xls', '.XSLX',
                '.ppt', '.PPTX', '.one', '.ONE', '.ost', '.OST', '.pst', '.PST',
                '.docm', '.DOCM', '.dot', '.DOT', '.dotm', '.DOTM', '.dotx', '.DOTX',
                '.csv', '.CSV'),
                'PICTURE': ('.jpeg', '.JPEG', '.jpg', '.JPG', '.png', '.PNG', '.gif', '.GIF',
                '.heic', '.HEIC,', '.tiff', '.TIFF' ,'.psd', '.PSD' ,'.raw', '.RAW' ,'.dng', '.ai',
                '.AI', '.bmp', '.BMP'),
                'MUSIC': ('mp3', '.MP3', '.wav', '.WAV', '.aac', '.aac', '.m4a', '.M4A', '.ogg', '.OGG', '.flac',
                '.FLAC', '.mid', '.MID'),
                'VIDEO': ('.mp4', '.MP4', '.mov', '.MOV', '.wmv', '.WMV', '.avi', '.AVI', '.avch', '.AVCHD', '.flv',
                '.FLV', '.f4v', '.F4V', '.mkv', '.MKV', '.webm', '.WEBM', '.mpg', '.MPG', '.mpeg', '.MPEG'),
                'PYTHON': ('.py', '.PY', '.rd', '.RD', '.db', '.DB', '.json', '.JSON', '.key', '.KEY')  
                }

    entry_t2_src.delete(0,'end')
    entry_t2_dst.delete(0,'end')

    try:

        if os.path.exists(pAth_t2_d):
            msg = messagebox.askyesno(message='The destination already exists.\n Do you want to replace it ?')
            if msg == True:
                shutil.rmtree(pAth_t2_d)
                copy_files_ext()
        else:
            cp = Toplevel(root)
            cp.title('Files *.* copied')
            cp.geometry('1000x350')
            cp.resizable(0,0)
            cp_field = Text(cp, height=22, width=150, bd=3, relief=SUNKEN)
            cp_field.pack()
            btn_cp_copy = Button(cp, text='Copy', command=lambda:cp.clipboard_append(cp_field.get('1.0',END))).place(relx=0.01, rely=0.95, anchor=SW)
            btn_cp_quit = Button(cp, text='Quit', command=lambda:cp.clipboard_append(cp.destroy())).place(relx=0.20, rely=0.95, anchor=SW)

            if ls_files_choice.get() == 'PDF':
                os.mkdir(pAth_t2_d)
                for root, dirs, files in os.walk(pAth_t2_s):
                    for file in files:
                        if file.endswith(dict_ext['PDF']):
                            shutil.copy2(os.path.join(root, file), os.path.join(pAth_t2_d, file))
                            name = os.path.join(root, os.path.join(pAth_t2_d, file))
                            cp_field.insert('1.0','%s\n' % name)

            if ls_files_choice.get() == 'Text':
                os.mkdir(pAth_t2_d)
                for root, dirs, files in os.walk(pAth_t2_s):
                    for file in files:
                        if file.endswith(dict_ext['TEXT']):
                            shutil.copy2(os.path.join(root, file), os.path.join(pAth_t2_d, file))
                            name = os.path.join(root, os.path.join(pAth_t2_d, file))
                            cp_field.insert('1.0','%s\n' % name)

            if ls_files_choice.get() == 'MS Office':
                os.mkdir(pAth_t2_d)
                for root, dirs, files in os.walk(pAth_t2_s):
                    for file in files:
                        if file.endswith(dict_ext['OFFICE']):
                            shutil.copy2(os.path.join(root, file), os.path.join(pAth_t2_d, file))
                            name = os.path.join(root, os.path.join(pAth_t2_d, file))
                            cp_field.insert('1.0','%s\n' % name)

            if ls_files_choice.get() == 'Picture':
                os.mkdir(pAth_t2_d)
                for root, dirs, files in os.walk(pAth_t2_s):
                    for file in files:
                        if file.endswith(dict_ext['PICTURE']):
                            shutil.copy2(os.path.join(root, file), os.path.join(pAth_t2_d, file))
                            name = os.path.join(root, os.path.join(pAth_t2_d, file))
                            cp_field.insert('1.0','%s\n' % name)

            if ls_files_choice.get() == 'Music':
                os.mkdir(pAth_t2_d)
                for root, dirs, files in os.walk(pAth_t2_s):
                    for file in files:
                        if file.endswith(dict_ext['MUSIC']):
                            shutil.copy2(os.path.join(root, file), os.path.join(pAth_t2_d, file))
                            name = os.path.join(root, os.path.join(pAth_t2_d, file))
                            cp_field.insert('1.0','%s\n' % name)

            if ls_files_choice.get() == 'Video':
                os.mkdir(pAth_t2_d)
                for root, dirs, files in os.walk(pAth_t2_s):
                    for file in files:
                        if file.endswith(dict_ext['VIDEO']):
                            shutil.copy2(os.path.join(root, file), os.path.join(pAth_t2_d, file))
                            name = os.path.join(root, os.path.join(pAth_t2_d, file))
                            cp_field.insert('1.0','%s\n' % name)

            if ls_files_choice.get() == 'PY':
                os.mkdir(pAth_t2_d)
                for root, dirs, files in os.walk(pAth_t2_s):
                    for file in files:
                        if file.endswith(dict_ext['PYTHON']):
                            shutil.copy2(os.path.join(root, file), os.path.join(pAth_t2_d, file))
                            name = os.path.join(root, os.path.join(pAth_t2_d, file))
                            cp_field.insert('1.0','%s\n' % name)

    except OSError:
        messagebox.showerror(message='You can\'t copy here.\n Please, change destination path')

#BUTTONS ON FIRST TAB
btn_select_src = Button(tab0, text='Browse', command=select_s)
btn_select_src.place(relx=0.5, rely=0.40, anchor=CENTER)
btn_select_dst = Button(tab0, text='Browse', command=select_d)
btn_select_dst.place(relx=0.5, rely=0.78, anchor=CENTER)
btn_copy = Button(tab0, text='Copy tree', command=copy_tree)
btn_copy.place(relx=0.5, rely=0.92, anchor=CENTER)

#BUTTONS ON SECOND TAB
btn_t1_select_src = Button(tab1, text='Browse', command=select_t1_s)
btn_t1_select_src.place(relx=0.5, rely=0.40, anchor=CENTER)
btn_t1_select_dst = Button(tab1, text='Browse', command=select_t1_d)
btn_t1_select_dst.place(relx=0.5, rely=0.78, anchor=CENTER)
btn_t1_copy = Button(tab1, text='Copy data', command=copy_files)
btn_t1_copy.place(relx=0.5, rely=0.92, anchor=CENTER)

#BUTTONS ON THIRD TAB
btn_t2_select_src = Button(tab2, text='Browse', command=select_t2_s)
btn_t2_select_src.place(relx=0.5, rely=0.53, anchor=CENTER)
btn_t2_select_dst = Button(tab2, text='Browse', command=select_t2_d)
btn_t2_select_dst.place(relx=0.5, rely=0.88, anchor=CENTER)
btn_t2_copy = Button(tab2, text='Copy files', command=copy_files_ext)
btn_t2_copy.place(relx=0.330, rely=0.095)

root.mainloop()
