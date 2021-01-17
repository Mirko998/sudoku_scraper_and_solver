from tkinter import *


sudoku = Tk()
sudoku.title('Sudoku Game')

menubar = Menu(sudoku)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Easy level sudoku", command=lambda:easy())
filemenu.add_command(label="Medium level sudoku", command=lambda:medium())
filemenu.add_command(label="Hard level sudoku", command=lambda:hard())
filemenu.add_command(label="Expert level sudoku", command=lambda:expert())

filemenu.add_separator()

filemenu.add_command(label="Easy level sudoku solved", command=lambda:easy_solved())
filemenu.add_command(label="Medium level sudoku solved", command=lambda:medium_solved())
filemenu.add_command(label="Hard level sudoku solved", command=lambda:hard_solved())
filemenu.add_command(label="Expert level sudoku solved", command=lambda:expert_solved())

filemenu.add_separator()


filemenu.add_command(label="Exit", command=sudoku.quit)
menubar.add_cascade(label="SUDOKU(Chose level)", menu=filemenu)
editmenu = Menu(menubar) 
editmenu.add_separator()


start_list_all_zero=[0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0]

expert_level=   [0,0,0,8,0,1,0,0,0,
                0,0,0,0,0,0,0,4,3,
                5,0,0,0,0,0,0,0,0,
                0,0,0,0,7,0,8,0,0,
                0,0,0,0,0,0,1,0,0,
                0,2,0,0,3,0,0,0,0,
                6,0,0,0,0,0,0,7,5,
                0,0,3,4,0,0,0,0,0,
                0,0,0,2,0,0,6,0,0]

expert_level_solved=[2,3,7,8,4,1,5,6,9,
                    1,8,6,7,9,5,2,4,3,
                    5,9,4,3,2,6,7,1,8,
                    3,1,5,6,7,4,8,9,2,
                    4,6,9,5,8,2,1,3,7,
                    7,2,8,1,3,9,4,5,6,
                    6,4,2,9,1,8,3,7,5,
                    8,5,3,4,6,7,9,2,1,
                    9,7,1,2,5,3,6,8,4]

hard_level=     [9,0,0,0,2,5,0,0,8,
                0,0,1,8,0,0,0,0,5,
                0,0,0,3,0,0,0,2,0,
                5,0,0,0,1,0,0,9,3,
                0,3,0,0,0,0,0,8,0,
                8,9,0,0,3,0,0,0,4,
                0,7,0,0,0,9,0,0,0,
                4,0,0,0,0,3,0,0,0,
                2,0,0,6,4,0,0,0,1]

hard_level_solved=[9,4,3,7,2,5,6,1,8,
                    7,2,1,8,6,4,9,3,5,
                    6,5,8,3,9,1,4,2,7,
                    5,6,7,4,1,8,2,9,3,
                    1,3,4,9,7,2,5,8,6,
                    8,9,2,5,3,6,1,7,4,
                    3,7,6,1,5,9,8,4,2,
                    4,1,5,2,8,3,7,6,9,
                    2,8,9,6,4,7,3,5,1]

medium_level=   [1,0,0,6,0,0,0,2,0,
                0,0,0,0,0,2,0,0,1,
                0,4,0,1,0,0,0,0,5,
                9,0,3,0,0,8,0,6,0,
                0,0,7,4,0,1,3,0,0,
                0,1,0,5,0,0,7,0,9,
                7,0,0,0,0,9,0,1,0,
                5,0,0,0,1,0,0,0,0,
                0,3,0,0,0,5,0,0,8]

medium_level_solved=[1,7,9,6,5,4,8,2,3,
                    3,8,5,9,2,7,6,4,1,
                    6,4,2,1,8,3,9,7,5,
                    9,5,3,2,7,8,1,6,4,
                    8,6,7,4,9,1,3,5,2,
                    2,1,4,5,3,6,7,8,9,
                    7,2,8,3,4,9,5,1,6,
                    5,9,6,8,1,2,4,3,7,
                    4,3,1,7,6,5,2,9,8]

easy_level=[1,5,0,7,0,0,0,9,0,
               3,0,0,9,1,0,0,6,0,
               0,0,0,0,0,4,0,1,0,
               0,8,0,5,0,0,0,0,6,
               0,9,0,8,0,7,0,4,0,
               6,0,0,0,0,2,0,7,0,
               0,3,0,4,0,0,0,0,0,
               0,6,0,0,7,9,0,0,2,
               0,4,0,0,0,3,0,8,9]

easy_level_solved=[1,5,6,7,3,8,2,9,4,
               3,2,4,9,1,5,8,6,7,
               8,7,9,6,2,4,5,1,3,
               4,8,7,5,9,1,3,2,6,
               2,9,3,8,6,7,1,4,5,
               6,1,5,3,4,2,9,7,8,
               9,3,2,4,8,6,7,5,1,
               5,6,8,1,7,9,4,3,2,
               7,4,1,2,5,3,6,8,9]

i=0
j=0

thelist= [start_list_all_zero, easy_level, easy_level_solved, medium_level, medium_level_solved, hard_level ,hard_level_solved, expert_level, expert_level_solved ]

def easy():
    global j
    j=1
    createGrid()

def easy_solved():
    global j
    j=2
    createGrid()

def medium():
    global j
    j=3
    createGrid()

def medium_solved():
    global j
    j=4
    createGrid()

def hard():
    global j
    j=5
    createGrid()

def hard_solved():
    global j
    j=6
    createGrid()

def expert():
    global j
    j=7
    createGrid()

def expert_solved():
    global j
    j=8
    createGrid()

def button(x):
    if x==0:
        x=x+1
    
def createGrid():
    for row in range (9):
        for column in range (9):
            if (row in (0,1,2,6,7,8) and column in (3,4,5) or \
                (row in (3,4,5) and column in (0,1,2,6,7,8))):
                    color="dark blue"
            else:
                color="light blue"

            global i
            x=thelist[j][i]

            i=i+1

            if i==81:
                i=0

            if x==0:
                text_color="red"
            else:
                text_color="black" 
            btn=Button(sudoku, padx=16, pady=16, bd=7, font=("arial", 10, "bold"),
                 bg=color, text=x, fg=text_color, command=lambda:button(x))   
            btn.grid(row=row, column=column)

createGrid()
sudoku.config(menu=menubar)
sudoku.mainloop()