## IDE para compilar el lenguaje
import c_lexer
import c_parser
import os
import turtle
from VirtualMachine import VirtualMachine
#import _tkinter
#import tkinter
from tkinter import *
from tkinter import filedialog

parser = c_parser.parser
drawCompiler = c_parser.drawCompiler

## Inicializa libreria de graficos
root = Tk()
root.title("Draw compiler")

## Inicializa text boxes para el codigo, consola y resultado
text_code = Text(root, height=28, width=65)
text_console = Text(root, height=10, width=125)
canvas = Canvas(root, height=400, width=400)

class RedirectText(object):
    def __init__(self, text_ctrl):
        self.output = text_ctrl
    
    def write(self, string):
        self.output.insert(END, string)

## Redirecciona output de consola a el IDE
redir = RedirectText(text_console)
sys.stdout = redir

## Funcion para abrir archivo
def open_file():
    ftypes = [
        ('Draw code files', '*.draws'),
        ('All files', '*')
    ]
    text_code.delete('1.0', END)
    clean_canvas()
    file_path = filedialog.askopenfilename(filetypes = ftypes)
    if file_path is None:
        return
    with open(file_path, 'r') as file:
        data = file.read()
    for line in data:
        text_code.insert(END, line)

## Funcion para guardar archivo
def file_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".draws")
    if f is None:
        return
    text = str(text_code.get(1.0, END))
    f.write(text)
    f.close()

## Funcion para compilar el codigo
def compile():
    drawCompiler.reset()
    text_console.delete(1.0, END)
    code = text_code.get("1.0", END)
    blank = "\n"
    code = blank.join(code.splitlines())
    try:
      parser.parse(code)
      text_console.insert(END, "Successfully compiled!\n")
      return True
    except SystemExit as e:
      text_console.insert(END, str(e))
    
            
def run():
    if (compile()):
        clean_canvas()
        virtual = VirtualMachine(drawCompiler.quad, drawCompiler.memory_manager, drawCompiler.dir_func, canvas)
        #print("Cuadruplos")
        #i = 0
        #for quad in drawCompiler.quad :
        #    print(str(i) + " (" + str(quad['operator']) + "," + str(quad['leftOperand']) + "," + str(quad['rightOperand']) + "," + str(quad['result']) + ")")
        #    i += 1


def clean_canvas():
    canvas.delete("all")

## Menu
menubar = Menu(root)
menubar.add_command(label="Save", command= file_save)

menubar.add_command(label="Open", command= open_file)

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
silly.hideturtle()


root.mainloop()
