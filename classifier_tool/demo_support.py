#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import os
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def set_Tk_var():
    global filez
    filez = StringVar()
    global ch1
    ch1 = IntVar(value=0)
    global ch2
    ch2 = IntVar(value=0)
    global ch3
    ch3 = IntVar(value=0)
    global ch4
    ch4 = IntVar(value=0)
    global ch5
    ch5 = IntVar(value=0)
    global ch6
    ch6 = IntVar(value=0)

    global par1,par2,par3,par4,par5
    par1 = StringVar()
    par2 = StringVar()
    par3 = StringVar()
    par4 = StringVar()
    par5 = StringVar()
    global cv1,cv2,cv3,cv4,cv5
    cv1 = IntVar(value=5)
    cv2 = IntVar(value=5)
    cv3 = IntVar(value=5)
    cv4 = IntVar(value=5)
    cv5 = IntVar(value=5)

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
    if os.path.exists('parameter.cfg'):
        os.remove('parameter.cfg')
    if os.path.exists('feature.cfg'):
        os.remove('feature.cfg')


if __name__ == '__main__':
    import demo
    demo.vp_start_gui()



