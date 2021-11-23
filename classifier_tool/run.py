#! /usr/bin/env python
#  -*- coding: utf-8 -*-
import logging
import sys
import os
from subprocess import *
try:
    from Tkinter import *
    from Tkinter import filedialog
    from Tkinter import messagebox
except ImportError:
    from tkinter import *
    from tkinter import filedialog
    from tkinter import messagebox

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import demo_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    demo_support.set_Tk_var()
    top = EEG_Classification_Demo (root)
    demo_support.init(root, top)
    root.mainloop()

w = None
def create_EEG_Classification_Demo(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    demo_support.set_Tk_var()
    top = EEG_Classification_Demo (w)
    demo_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_EEG_Classification_Demo():
    global w
    w.destroy()
    w = None


class EEG_Classification_Demo:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family Calibri -size 12 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
        font12 = "-family Calibri -size 14 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font22 = "-family Calibri -size 20 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font13 = "-family {Times New Roman} -size 28 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
        font14 = "-family Calibri -size 11 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
        font9 = "-family Calibri -size 13 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.Bstyle=ttk.Style()
        self.Bstyle.configure('my.TButton',font=font22)
        self.featurefiles=[]
        top.geometry("1092x615+125+42")
        top.title("EEG Classification Demo")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.58, rely=0.73, height=45, width=216)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Generate Parameter Configuration''')
        self.TButton1.configure(command=self.createparameter)



        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.TButton2 = ttk.Button(top,style='my.TButton')
        self.TButton2.place(relx=0.39, rely=0.85, height=65, width=246)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Generate Results''')
        self.TButton2.configure(width=246)
        self.TButton2.configure(command=self.generateresult)


        self.TButton3 = ttk.Button(top)
        self.TButton3.place(relx=0.13, rely=0.78, height=45, width=116)
        self.TButton3.configure(command=self.browsefunc)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Browse''')
        self.TButton3.configure(width=116)


        self.TButton3 = ttk.Button(top)
        self.TButton3.place(relx=0.02, rely=0.78, height=45, width=116)
        self.TButton3.configure(command=self.removeselect)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Remove Selected''')
        self.TButton3.configure(width=116)

        self.TButton4 = ttk.Button(top)
        self.TButton4.place(relx=0.10, rely=0.88, height=45, width=206)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Generate Features Configuration''')
        self.TButton4.configure(command=self.createfeature)


        self.Listbox1 = Listbox(top)
        self.Listbox1.place(relx=0.05, rely=0.24, relheight=0.47, relwidth=0.32)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font=font10)
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=344)
        self.Listbox1.configure(listvariable=demo_support.filez)

        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.41, rely=0.27, relheight=0.05
                , relwidth=0.07)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font=font9)
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''KNN''')
        self.Checkbutton1.configure(variable=demo_support.ch1)
        self.Checkbutton1.configure(width=71)

        self.Checkbutton1_1 = Checkbutton(top)
        self.Checkbutton1_1.place(relx=0.41, rely=0.36, relheight=0.05
                , relwidth=0.07)
        self.Checkbutton1_1.configure(activebackground="#d9d9d9")
        self.Checkbutton1_1.configure(activeforeground="#000000")
        self.Checkbutton1_1.configure(background="#d9d9d9")
        self.Checkbutton1_1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_1.configure(font=font9)
        self.Checkbutton1_1.configure(foreground="#000000")
        self.Checkbutton1_1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_1.configure(highlightcolor="black")
        self.Checkbutton1_1.configure(justify=LEFT)
        self.Checkbutton1_1.configure(text='''SVM''')
        self.Checkbutton1_1.configure(variable=demo_support.ch2)
        self.Checkbutton1_1.configure(width=71)

        self.Checkbutton1_2 = Checkbutton(top)
        self.Checkbutton1_2.place(relx=0.41, rely=0.44, relheight=0.05
                , relwidth=0.16)
        self.Checkbutton1_2.configure(activebackground="#d9d9d9")
        self.Checkbutton1_2.configure(activeforeground="#000000")
        self.Checkbutton1_2.configure(background="#d9d9d9")
        self.Checkbutton1_2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_2.configure(font=font9)
        self.Checkbutton1_2.configure(foreground="#000000")
        self.Checkbutton1_2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_2.configure(highlightcolor="black")
        self.Checkbutton1_2.configure(justify=LEFT)
        self.Checkbutton1_2.configure(text='''Logistic Regression''')
        self.Checkbutton1_2.configure(variable=demo_support.ch3)
        self.Checkbutton1_2.configure(width=171)

        self.Checkbutton1_3 = Checkbutton(top)
        self.Checkbutton1_3.place(relx=0.41, rely=0.53, relheight=0.05
                , relwidth=0.12)
        self.Checkbutton1_3.configure(activebackground="#d9d9d9")
        self.Checkbutton1_3.configure(activeforeground="#000000")
        self.Checkbutton1_3.configure(background="#d9d9d9")
        self.Checkbutton1_3.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_3.configure(font=font9)
        self.Checkbutton1_3.configure(foreground="#000000")
        self.Checkbutton1_3.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_3.configure(highlightcolor="black")
        self.Checkbutton1_3.configure(justify=LEFT)
        self.Checkbutton1_3.configure(text='''XGB Classifier''')
        self.Checkbutton1_3.configure(variable=demo_support.ch4)
        self.Checkbutton1_3.configure(width=131)

        self.Checkbutton1_4 = Checkbutton(top)
        self.Checkbutton1_4.place(relx=0.41, rely=0.63, relheight=0.05
                , relwidth=0.14)
        self.Checkbutton1_4.configure(activebackground="#d9d9d9")
        self.Checkbutton1_4.configure(activeforeground="#000000")
        self.Checkbutton1_4.configure(background="#d9d9d9")
        self.Checkbutton1_4.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_4.configure(font=font9)
        self.Checkbutton1_4.configure(foreground="#000000")
        self.Checkbutton1_4.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_4.configure(highlightcolor="black")
        self.Checkbutton1_4.configure(justify=LEFT)
        self.Checkbutton1_4.configure(text='''LGBM Classifier''')
        self.Checkbutton1_4.configure(variable=demo_support.ch5)
        self.Checkbutton1_4.configure(width=151)

        
        self.CheckbuttonF = Checkbutton(top)
        self.CheckbuttonF.place(relx=0.24, rely=0.79, relheight=0.05, relwidth=0.17)
        self.CheckbuttonF.configure(activebackground="#d9d9d9")
        self.CheckbuttonF.configure(activeforeground="#000000")
        self.CheckbuttonF.configure(background="#d9d9d9")
        self.CheckbuttonF.configure(disabledforeground="#a3a3a3")
        self.CheckbuttonF.configure(font=font9)
        self.CheckbuttonF.configure(foreground="#000000")
        self.CheckbuttonF.configure(highlightbackground="#d9d9d9")
        self.CheckbuttonF.configure(highlightcolor="black")
        self.CheckbuttonF.configure(justify=LEFT)
        self.CheckbuttonF.configure(text='''Combine All Features''')
        self.CheckbuttonF.configure(variable=demo_support.ch6)
        self.CheckbuttonF.configure(width=151)

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.32, rely=0.03, height=47, width=399)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font=font13)
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''EEG Classification Demo''')

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.1, rely=0.18, height=27, width=205)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font=font12)
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text='''List of input Feature Files''')

        self.TLabel2_5 = ttk.Label(top)
        self.TLabel2_5.place(relx=0.4, rely=0.18, height=27, width=185)
        self.TLabel2_5.configure(background="#d9d9d9")
        self.TLabel2_5.configure(foreground="#000000")
        self.TLabel2_5.configure(font=font12)
        self.TLabel2_5.configure(relief=FLAT)
        self.TLabel2_5.configure(text='''Classification Models''')
        self.TLabel2_5.configure(width=185)

        self.TLabel2_6 = ttk.Label(top)
        self.TLabel2_6.place(relx=0.6, rely=0.18, height=27, width=235)
        self.TLabel2_6.configure(background="#d9d9d9")
        self.TLabel2_6.configure(foreground="#000000")
        self.TLabel2_6.configure(font=font12)
        self.TLabel2_6.configure(relief=FLAT)
        self.TLabel2_6.configure(text='''Parameter Tuning Dictionary''')
        self.TLabel2_6.configure(width=235)

        self.TLabel2_7 = ttk.Label(top)
        self.TLabel2_7.place(relx=0.88, rely=0.18, height=27, width=165)
        self.TLabel2_7.configure(background="#d9d9d9")
        self.TLabel2_7.configure(foreground="#000000")
        self.TLabel2_7.configure(font=font12)
        self.TLabel2_7.configure(relief=FLAT)
        self.TLabel2_7.configure(text='''CV Value''')
        self.TLabel2_7.configure(width=165)

        self.TButton4 = ttk.Button(top)
        self.TButton4.place(relx=0.83, rely=0.86, height=45, width=136)
        self.TButton4.configure(command=demo_support.destroy_window)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Exit''')
        self.TButton4.configure(width=136)

        self.TButton4 = ttk.Button(top)
        self.TButton4.place(relx=0.65, rely=0.86, height=45, width=136)
        self.TButton4.configure(command=self.showresults)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Show Past Result''')
        self.TButton4.configure(width=136)


        self.TLabel3 = ttk.Label(top)
        self.TLabel3.place(relx=0.1, rely=0.72, height=25, width=225)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font=font9)
        self.TLabel3.configure(relief=FLAT)
        self.TLabel3.configure(text='''(Select all required files at once)''')

        self.TLabel3_8 = ttk.Label(top)
        self.TLabel3_8.place(relx=0.64, rely=0.21, height=25, width=165)
        self.TLabel3_8.configure(background="#d9d9d9")
        self.TLabel3_8.configure(foreground="#000000")
        self.TLabel3_8.configure(font=font14)
        self.TLabel3_8.configure(relief=FLAT)
        self.TLabel3_8.configure(text='''(Leave blank for default)''')
        self.TLabel3_8.configure(width=165)

        self.TLabel3_9 = ttk.Label(top)
        self.TLabel3_9.place(relx=0.88, rely=0.21, height=25, width=165)
        self.TLabel3_9.configure(background="#d9d9d9")
        self.TLabel3_9.configure(foreground="#000000")
        self.TLabel3_9.configure(font=font14)
        self.TLabel3_9.configure(relief=FLAT)
        self.TLabel3_9.configure(text='''(Default=5)''')

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.6, rely=0.28,height=20, relwidth=0.24)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=264)
        self.Entry1.configure(textvariable=demo_support.par1)


        self.Entry1_10 = Entry(top)
        self.Entry1_10.place(relx=0.6, rely=0.37,height=20, relwidth=0.24)
        self.Entry1_10.configure(background="white")
        self.Entry1_10.configure(disabledforeground="#a3a3a3")
        self.Entry1_10.configure(font="TkFixedFont")
        self.Entry1_10.configure(foreground="#000000")
        self.Entry1_10.configure(highlightbackground="#d9d9d9")
        self.Entry1_10.configure(highlightcolor="black")
        self.Entry1_10.configure(insertbackground="black")
        self.Entry1_10.configure(selectbackground="#c4c4c4")
        self.Entry1_10.configure(selectforeground="black")
        self.Entry1_10.configure(textvariable=demo_support.par2)

        self.Entry1_11 = Entry(top)
        self.Entry1_11.place(relx=0.6, rely=0.45,height=20, relwidth=0.24)
        self.Entry1_11.configure(background="white")
        self.Entry1_11.configure(disabledforeground="#a3a3a3")
        self.Entry1_11.configure(font="TkFixedFont")
        self.Entry1_11.configure(foreground="#000000")
        self.Entry1_11.configure(highlightbackground="#d9d9d9")
        self.Entry1_11.configure(highlightcolor="black")
        self.Entry1_11.configure(insertbackground="black")
        self.Entry1_11.configure(selectbackground="#c4c4c4")
        self.Entry1_11.configure(selectforeground="black")
        self.Entry1_11.configure(textvariable=demo_support.par3)

        self.Entry1_12 = Entry(top)
        self.Entry1_12.place(relx=0.6, rely=0.54,height=20, relwidth=0.24)
        self.Entry1_12.configure(background="white")
        self.Entry1_12.configure(disabledforeground="#a3a3a3")
        self.Entry1_12.configure(font="TkFixedFont")
        self.Entry1_12.configure(foreground="#000000")
        self.Entry1_12.configure(highlightbackground="#d9d9d9")
        self.Entry1_12.configure(highlightcolor="black")
        self.Entry1_12.configure(insertbackground="black")
        self.Entry1_12.configure(selectbackground="#c4c4c4")
        self.Entry1_12.configure(selectforeground="black")
        self.Entry1_12.configure(textvariable=demo_support.par4)

        self.Entry1_13 = Entry(top)
        self.Entry1_13.place(relx=0.6, rely=0.64,height=20, relwidth=0.24)
        self.Entry1_13.configure(background="white")
        self.Entry1_13.configure(disabledforeground="#a3a3a3")
        self.Entry1_13.configure(font="TkFixedFont")
        self.Entry1_13.configure(foreground="#000000")
        self.Entry1_13.configure(highlightbackground="#d9d9d9")
        self.Entry1_13.configure(highlightcolor="black")
        self.Entry1_13.configure(insertbackground="black")
        self.Entry1_13.configure(selectbackground="#c4c4c4")
        self.Entry1_13.configure(selectforeground="black")
        self.Entry1_13.configure(textvariable=demo_support.par5)

        self.Entry1_15 = Entry(top)
        self.Entry1_15.place(relx=0.88, rely=0.28,height=20, relwidth=0.06)
        self.Entry1_15.configure(background="white")
        self.Entry1_15.configure(disabledforeground="#a3a3a3")
        self.Entry1_15.configure(font="TkFixedFont")
        self.Entry1_15.configure(foreground="#000000")
        self.Entry1_15.configure(highlightbackground="#d9d9d9")
        self.Entry1_15.configure(highlightcolor="black")
        self.Entry1_15.configure(insertbackground="black")
        self.Entry1_15.configure(selectbackground="#c4c4c4")
        self.Entry1_15.configure(selectforeground="black")
        self.Entry1_15.configure(width=64)
        self.Entry1_15.configure(textvariable=demo_support.cv1)

        self.Entry1_16 = Entry(top)
        self.Entry1_16.place(relx=0.88, rely=0.37,height=20, relwidth=0.06)
        self.Entry1_16.configure(background="white")
        self.Entry1_16.configure(disabledforeground="#a3a3a3")
        self.Entry1_16.configure(font="TkFixedFont")
        self.Entry1_16.configure(foreground="#000000")
        self.Entry1_16.configure(highlightbackground="#d9d9d9")
        self.Entry1_16.configure(highlightcolor="black")
        self.Entry1_16.configure(insertbackground="black")
        self.Entry1_16.configure(selectbackground="#c4c4c4")
        self.Entry1_16.configure(selectforeground="black")
        self.Entry1_16.configure(textvariable=demo_support.cv2)

        self.Entry1_162 = Entry(top)
        self.Entry1_162.place(relx=0.88, rely=0.45,height=20, relwidth=0.06)
        self.Entry1_162.configure(background="white")
        self.Entry1_162.configure(disabledforeground="#a3a3a3")
        self.Entry1_162.configure(font="TkFixedFont")
        self.Entry1_162.configure(foreground="#000000")
        self.Entry1_162.configure(highlightbackground="#d9d9d9")
        self.Entry1_162.configure(highlightcolor="black")
        self.Entry1_162.configure(insertbackground="black")
        self.Entry1_162.configure(selectbackground="#c4c4c4")
        self.Entry1_16.configure(selectforeground="black")
        self.Entry1_162.configure(textvariable=demo_support.cv3)        

        self.Entry1_163 = Entry(top)
        self.Entry1_163.place(relx=0.88, rely=0.54,height=20, relwidth=0.06)
        self.Entry1_163.configure(background="white")
        self.Entry1_163.configure(disabledforeground="#a3a3a3")
        self.Entry1_163.configure(font="TkFixedFont")
        self.Entry1_163.configure(foreground="#000000")
        self.Entry1_163.configure(highlightbackground="#d9d9d9")
        self.Entry1_163.configure(highlightcolor="black")
        self.Entry1_163.configure(insertbackground="black")
        self.Entry1_163.configure(selectbackground="#c4c4c4")
        self.Entry1_16.configure(selectforeground="black")
        self.Entry1_163.configure(textvariable=demo_support.cv4)        

        self.Entry1_164 = Entry(top)
        self.Entry1_164.place(relx=0.88, rely=0.63,height=20, relwidth=0.06)
        self.Entry1_164.configure(background="white")
        self.Entry1_164.configure(disabledforeground="#a3a3a3")
        self.Entry1_164.configure(font="TkFixedFont")
        self.Entry1_164.configure(foreground="#000000")
        self.Entry1_164.configure(highlightbackground="#d9d9d9")
        self.Entry1_164.configure(highlightcolor="black")
        self.Entry1_164.configure(insertbackground="black")
        self.Entry1_164.configure(selectbackground="#c4c4c4")
        self.Entry1_164.configure(selectforeground="black")
        self.Entry1_164.configure(textvariable=demo_support.cv5)        



    def browsefunc(self):
        names=filedialog.askopenfilenames(title="Import Mat Files",filetypes=(("MAT files", "*.MAT;*.mat"),("All files", "*.*")))
        for i in names:
            self.Listbox1.insert(END,i.split('/')[-1:])
            self.featurefiles.append(i)

    def removeselect(self):
        selection = self.Listbox1.curselection()
        try:
            self.Listbox1.delete(selection[0])
            del self.featurefiles[selection[0]]
        except:
            pass

    def createfeature(self):
        if self.Listbox1.size()==0:
            messagebox.showwarning("No File","No Feature file has been selected. Please select the files first.")
        else:
            feat=open("feature.cfg",'w')
            feat.write(str(self.Listbox1.size())+'\n')
            for i in self.featurefiles[:-1]:
                feat.write(i+'\n')
            feat.write(self.featurefiles[-1])
            if demo_support.ch6.get()==1:
                feat.write('\n')
                for k in range(self.Listbox1.size()-1):
                    feat.write("True ")
                feat.write("True")
            feat.close()
            messagebox.showinfo("Configuration Generated","Configuration for selected features has been generated as \"feature.cfg\"")


    def showresults(self):
        call(['python', 'results.py'],shell=True)
    def generateresult(self):
        if not os.path.exists("parameter.cfg"):
            messagebox.showerror("Configuration Error","Parameter Configuration File not found.")
        elif not os.path.exists("feature.cfg"):
            messagebox.showerror("Configuration Error","Features Configuration File not found.")
        else:
            call(['python', 'results.py'],shell=True)
            call(['python', 'main_tool.py'],shell=True)


    def createparameter(self):
        param=open("parameter.cfg",'w')
        if demo_support.ch1.get()==1:
            if len(demo_support.par1.get())==0:
                param.write("{'n_neighbors':range(1,10)}"+' -- '+str(demo_support.cv1.get())+'\n')
            else:
                try:
                    if isinstance(eval(demo_support.par1.get()), dict):
                        param.write(demo_support.par1.get()+' -- '+demo_support.cv1.get()+'\n')
                    else:
                        raise SyntaxError()
                except:
                    param.write("SKIP\n")
                    messagebox.showerror("Invalid Parameter","Your parameter Dictionary input for KNN is Invalid.")
        else:
            param.write("SKIP\n")

        #SVM
        if demo_support.ch2.get()==1:
            if len(demo_support.par2.get())==0:
                param.write("{'C':[0.001, 0.01, 0.1, 1, 10],'gamma':[0.001, 0.01, 0.1, 1]}"+' -- '+str(demo_support.cv2.get())+'\n')
            else:
                try:
                    if isinstance(eval(demo_support.par2.get()), dict):
                        param.write(demo_support.par2.get()+' -- '+demo_support.cv2.get()+'\n')
                    else:
                        raise SyntaxError()
                except:
                    param.write("SKIP\n")
                    messagebox.showerror("Invalid Parameter","Your parameter Dictionary input for SVM is Invalid.")
        else:
            param.write("SKIP\n")
        #LogReg
        if demo_support.ch3.get()==1:
            if len(demo_support.par3.get())==0:
                param.write("{'C':[0.001,0.01,0.1,1,10,100]}"+' -- '+str(demo_support.cv3.get())+'\n')
            else:
                try:
                    if isinstance(eval(demo_support.par3.get()), dict):
                        param.write(demo_support.par3.get()+' -- '+demo_support.cv3.get()+'\n')
                    else:
                        raise SyntaxError()
                except:
                    param.write("SKIP\n")
                    messagebox.showerror("Invalid Parameter","Your parameter Dictionary input for Logistic Regression is Invalid.")
        else:
            param.write("SKIP\n")

        #XGB
        if demo_support.ch4.get()==1:
            if len(demo_support.par4.get())==0:
                param.write("{'max_depth':range(3,11)}"+' -- '+str(demo_support.cv4.get())+'\n')
            else:
                try:
                    if isinstance(eval(demo_support.par4.get()), dict):
                        param.write(demo_support.par4.get()+' -- '+demo_support.cv4.get()+'\n')
                    else:
                        raise SyntaxError()
                except:
                    param.write("SKIP\n")
                    messagebox.showerror("Invalid Parameter","Your parameter Dictionary input for XGBoost is Invalid.")
        else:
            param.write("SKIP\n")

        #LGB
        if demo_support.ch5.get()==1:
            if len(demo_support.par5.get())==0:
                param.write("{'max_depth':range(3,11)}"+' -- '+str(demo_support.cv5.get())+'\n')
            else:
                try:
                    if isinstance(eval(demo_support.par5.get()), dict):
                        param.write(demo_support.par5.get()+' -- '+demo_support.cv5.get()+'\n')
                    else:
                        raise SyntaxError()
                except:
                    param.write("SKIP\n")
                    messagebox.showerror("Invalid Parameter","Your parameter Dictionary input for LightGBM is Invalid.")
        else:
            param.write("SKIP\n")

        param.close()
        with open('parameter.cfg', 'r') as in_file:
            with open('xparameter.cfg', 'w') as out_file:
                out_file.write(in_file.read()[:-1])
        os.remove('parameter.cfg')
        os.rename('xparameter.cfg','parameter.cfg')
        messagebox.showinfo("Configuration Generated","Configuration for selected models and their parameters has been generated as \"parameter.cfg\"")


if __name__ == '__main__':
    vp_start_gui()