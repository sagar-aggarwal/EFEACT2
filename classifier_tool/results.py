#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#

import sys
import pandas as pd
import os
try:
    from Tkinter import *
    from Tkinter import messagebox
except ImportError:
    from tkinter import *
    from tkinter import messagebox
from PIL import ImageTk,Image

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import results_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    results_support.set_Tk_var()
    top = Show_Results (root)
    results_support.init(root, top)
    root.mainloop()

w = None
def create_Show_Results(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    results_support.set_Tk_var()
    top = Show_Results (w)
    results_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Show_Results():
    global w
    w.destroy()
    w = None


class Show_Results:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font12 = "-family Calibri -size 14 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font13 = "-family {Times New Roman} -size 24 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
        font9 = "-family Calibri -size 12 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font=font9)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("729x477+309+92")
        top.title("Show Results")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.08, rely=0.31, relheight=0.06, relwidth=0.4)
        self.TCombobox1.configure(textvariable=results_support.combobox)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.configure(values=tuple(os.listdir("Results/")))
        self.TCombobox1.bind("<<ComboboxSelected>>", self.showTable)

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.64, rely=0.05, height=39, width=178)
        self.TButton1.configure(command=self.accgraph)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Show Accuracy Graphs''')

        self.TButton1_1 = ttk.Button(top)
        self.TButton1_1.place(relx=0.64, rely=0.18, height=39, width=178)
        self.TButton1_1.configure(command=self.fittimegraph)
        self.TButton1_1.configure(takefocus="")
        self.TButton1_1.configure(text='''Show Fit Time Graphs''')

        self.TButton1_2 = ttk.Button(top)
        self.TButton1_2.place(relx=0.64, rely=0.31, height=39, width=178)
        self.TButton1_2.configure(command=self.refresh)
        self.TButton1_2.configure(takefocus="")
        self.TButton1_2.configure(text='''Refresh Result List''')


        self.style.configure('Treeview.Heading',  font=font9)
        self.Scrolledtreeview1 = ScrolledTreeView(top)
        self.Scrolledtreeview1.place(relx=0.08, rely=0.48, relheight=0.35, relwidth=0.85)
        self.Scrolledtreeview1.configure(columns="Col1 Col2")
        self.Scrolledtreeview1.heading("#0",text="Model Name")
        self.Scrolledtreeview1.heading("#0",anchor="center")
        self.Scrolledtreeview1.column("#0",width="153")
        self.Scrolledtreeview1.column("#0",minwidth="20")
        self.Scrolledtreeview1.column("#0",stretch="1")
        self.Scrolledtreeview1.column("#0",anchor="w")
        self.Scrolledtreeview1.heading("Col1",text="Accuracy")
        self.Scrolledtreeview1.heading("Col1",anchor="center")
        self.Scrolledtreeview1.column("Col1",width="110")
        self.Scrolledtreeview1.column("Col1",minwidth="20")
        self.Scrolledtreeview1.column("Col1",stretch="1")
        self.Scrolledtreeview1.column("Col1",anchor="w")
        self.Scrolledtreeview1.heading("Col2",text="Best Parameters")
        self.Scrolledtreeview1.heading("Col2",anchor="center")
        self.Scrolledtreeview1.column("Col2",width="340")
        self.Scrolledtreeview1.column("Col2",minwidth="20")
        self.Scrolledtreeview1.column("Col2",stretch="1")
        self.Scrolledtreeview1.column("Col2",anchor="w")

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.08, rely=0.25, height=27, width=185)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font=font12)
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text='''Select FeatureSet''')

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.43, rely=0.86, height=39, width=108)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Cancel''')
        self.TButton2.configure(command=results_support.destroy_window)


        self.TLabel2_2 = ttk.Label(top)
        self.TLabel2_2.place(relx=0.08, rely=0.06, height=67, width=225)
        self.TLabel2_2.configure(background="#d9d9d9")
        self.TLabel2_2.configure(foreground="#000000")
        self.TLabel2_2.configure(font=font13)
        self.TLabel2_2.configure(relief=FLAT)
        self.TLabel2_2.configure(text='''Result Viewer''')

    def showTable(self,event=None):
        self.Scrolledtreeview1.delete(*self.Scrolledtreeview1.get_children())
        if os.path.exists("Results/"+results_support.combobox.get()+"/"+results_support.combobox.get()+".csv"):
            toshow=pd.read_csv("Results/"+results_support.combobox.get()+"/"+results_support.combobox.get()+".csv")
            for index, row in toshow.iterrows():
                self.Scrolledtreeview1.insert("",'end',text=row["Model"],values=(str(row["BestScore"]*100)[:6],row["BestParameters"]))
        else:
            messagebox.showinfo("Incomplete Result","Complete results not generated yet. Wait till completion or run again.\n Meanwhile you can check the completed graphs.")

    def refresh(self):
        self.TCombobox1.configure(values=tuple(os.listdir("Results/")))
    def fittimegraph(self):
        self.accgraph('MeanFitTime')

    def accgraph(self,strs='MeanTestScore'):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font12 = "-family Calibri -size 14 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font13 = "-family {Times New Roman} -size 24 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
        font9 = "-family Calibri -size 12 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"

        win=Toplevel()
        win.geometry("1073x560+126+74")
        win.title(strs+" Graphs")
        win.configure(background="#d9d9d9")

        present=os.listdir("Results/"+results_support.combobox.get())
        required={}
        for img in present:
            if img[-4:]=='.png':
                if img.split('_')[1].split('.')[0]==strs:
                    required[img.split('_')[0]]="Results/"+results_support.combobox.get()+"/"+img

        #KNN
        Label1 = Label(win)
        Label1.place(relx=0.03, rely=0.04, height=244, width=324)
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font=font9)
        Label1.configure(foreground="#000000")
        try:
            img1 = Image.open(required["KNN"])
            img1=img1.resize((320,240),Image.ANTIALIAS)
            _img1 = ImageTk.PhotoImage(img1)
            Label1.configure(image=_img1)
            Label1.photo = _img1
        except:
            pass
        Label1.configure(text='''KNN was not run.''')

        #SVM
        Label1_1 = Label(win)
        Label1_1.place(relx=0.03, rely=0.52, height=244, width=324)
        Label1_1.configure(activebackground="#f9f9f9")
        Label1_1.configure(activeforeground="black")
        Label1_1.configure(background="#d9d9d9")
        Label1_1.configure(disabledforeground="#a3a3a3")
        Label1_1.configure(font=font9)
        Label1_1.configure(foreground="#000000")
        Label1_1.configure(highlightbackground="#d9d9d9")
        Label1_1.configure(highlightcolor="black")
        try:
            img2 = Image.open(required["SVM"])
            img2=img2.resize((320,240),Image.ANTIALIAS)
            _img2 = ImageTk.PhotoImage(img2)
            Label1_1.configure(image=_img2)
            Label1_1.photo = _img2
        except:
            pass
        Label1_1.configure(text='''SVM was not run.''')


        #LogRegr
        Label1_2 = Label(win)
        Label1_2.place(relx=0.34, rely=0.04, height=244, width=324)
        Label1_2.configure(activebackground="#f9f9f9")
        Label1_2.configure(activeforeground="black")
        Label1_2.configure(background="#d9d9d9")
        Label1_2.configure(disabledforeground="#a3a3a3")
        Label1_2.configure(font=font9)
        Label1_2.configure(foreground="#000000")
        Label1_2.configure(highlightbackground="#d9d9d9")
        Label1_2.configure(highlightcolor="black")
        try:
            img3 = Image.open(required["LogRegr"])
            img3=img3.resize((320,240),Image.ANTIALIAS)
            _img3 = ImageTk.PhotoImage(img3)
            Label1_2.configure(image=_img3)
            Label1_2.photo = _img3
        except:
            pass
        Label1_2.configure(text='''Logistic Regression was not run.''')

        #XGB
        Label1_3 = Label(win)
        Label1_3.place(relx=0.34, rely=0.52, height=244, width=324)
        Label1_3.configure(activebackground="#f9f9f9")
        Label1_3.configure(activeforeground="black")
        Label1_3.configure(background="#d9d9d9")
        Label1_3.configure(disabledforeground="#a3a3a3")
        Label1_3.configure(font=font9)
        Label1_3.configure(foreground="#000000")
        Label1_3.configure(highlightbackground="#d9d9d9")
        Label1_3.configure(highlightcolor="black")
        try:
            img4 = Image.open(required["XGB"])
            img4=img4.resize((320,240),Image.ANTIALIAS)
            _img4 = ImageTk.PhotoImage(img4)
            Label1_3.configure(image=_img4)
            Label1_3.photo = _img4
        except:
            pass
        Label1_3.configure(text='''XGBClassifier was not run.''')

        #LGB
        Label1_4 = Label(win)
        Label1_4.place(relx=0.67, rely=0.04, height=244, width=324)
        Label1_4.configure(activebackground="#f9f9f9")
        Label1_4.configure(activeforeground="black")
        Label1_4.configure(background="#d9d9d9")
        Label1_4.configure(disabledforeground="#a3a3a3")
        Label1_4.configure(font=font9)
        Label1_4.configure(foreground="#000000")
        Label1_4.configure(highlightbackground="#d9d9d9")
        Label1_4.configure(highlightcolor="black")
        try:
            img5 = Image.open(required["LGB"])
            img5=img5.resize((320,240),Image.ANTIALIAS)
            _img5 = ImageTk.PhotoImage(img5)
            Label1_4.configure(image=_img5)
            Label1_4.photo = _img5
        except:
            pass
        Label1_4.configure(text='''LGBMClassifier was not run.''')


        TButton1 = ttk.Button(win)
        TButton1.place(relx=0.73, rely=0.64, height=69, width=198)
        TButton1.configure(takefocus="")
        TButton1.configure(text='''Close Window''')
        TButton1.configure(width=198)
        TButton1.configure(command=lambda : win.destroy())


        
        



# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


if __name__ == '__main__':
    vp_start_gui()



