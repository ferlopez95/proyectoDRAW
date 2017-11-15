## IDE para compilar el lenguaje
import c_lexer
import c_parser
import os
import turtle
from VirtualMachine import VirtualMachine
from Tkinter import *

parser = c_parser.parser
drawCompiler = c_parser.drawCompiler


## Inicializa libreria de graficos
root = Tk()
root.title("Draw compiler")

## Inicializa text boxes para el codigo, consola y resultado
text_code = Text(root, height=25, width=40)
text_console = Text(root, height=10, width=125)
canvas = Canvas(root, height=400, width=400)

class RedirectText(object):
    def __init__(self, text_ctrl):
        self.output = text_ctrl
    
    def write(self, string):
        self.output.insert(END, string)

## Funcion para compilar el codigo
def compile():
    drawCompiler.reset()
    text_console.delete(1.0, END)   
    code = text_code.get("1.0", END)
    try:
      parser.parse(code)
      text_console.insert(END, "Successfully compiled!\n")
    except SystemExit as e:
      text_console.insert(END, str(e.message))

def run():
    redir = RedirectText(text_console)
    sys.stdout = redir
    compile()
    virtual = VirtualMachine(drawCompiler.quad, drawCompiler.memory_manager)
    print("Cuadruplos")
    i = 0
    for quad in drawCompiler.quad :
        print(str(i) + " " + str(quad))
        i += 1
    #for key, value in drawCompiler.dir_func.items() :
    #    print(str(key) + " : " + str(value))
    #print(virtual.memory.mem_local.var_int)
    #print(virtual.memory.mem_local.var_float)
    #print(virtual.memory.mem_local.var_boolean)

## Menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close")

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")

editmenu.add_separator()

editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)

menubar.add_command(label="Compile", command= compile)

menubar.add_command(label="Run", command= run)

root.config(menu=menubar)

## Labels de Code, Result y Console
label_code = Label(root, text="Code:", width=40)
label_code.grid(row=1, column=0)

label_result = Label(root, text="Result:", width=40)
label_result.grid(row=1, column=1)

label_console = Label(root, text="Console:", width=40)
label_console.grid(row=3, column=0)

## Configura el grid de cada text box
text_code.grid(row=2, column=0)
text_console.grid(row=4, column=0, columnspan=3)
canvas.grid(row=2, column=1)


## Turtles

silly = turtle.RawTurtle(canvas)

silly.forward(50)
silly.right(90)     # Rotate clockwise by 90 degrees

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

turtle.done()

root.mainloop()
