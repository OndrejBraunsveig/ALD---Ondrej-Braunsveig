import random
from tkinter import *
from PIL import ImageTk, Image


SIZE_BOARD = 20
SIZE_BLOCK = 40
SIZE_CANVAS = 800

def generateBoard(size : int) -> list:
    board = [[-1]*size for _ in range(size)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            viable = list(range(13))
            random.shuffle(viable)
            if (i != 0):
                viable = checkUp(board, viable, i, j)
            if (j != 0):
                viable = checkLeft(board, viable, i, j)
            board[i][j] = viable.pop()
            print(f"{board[i][j]:5}",end='')
        print("")
    return board

def checkUp(board : list, _viable : list, row : int, col : int) -> list:
    #connects
    if (board[row-1][col] in [3,4,6,7,8,10,12]):
        _viable = [piece for piece in _viable if piece not in (0,1,2,6,10,12)]
    #doesnt connect
    else:
        _viable = [piece for piece in _viable if piece not in (3,4,5,7,8,9,11)]

    return _viable

def checkLeft(board : list, _viable : list, row : int, col : int) -> list:
    #connects
    if (board[row][col-1] in [1,2,4,5,6,7,11,12]):
        _viable = [piece for piece in _viable if piece not in (0,1,3,7,11,12)]
    #doesnt connect
    else:
        _viable = [piece for piece in _viable if piece not in (2,4,5,6,8,9,10)]

    return _viable



gameBoard = generateBoard(SIZE_BOARD)

root = Tk()
root.title("World Generation")
root.geometry(f"{SIZE_CANVAS}x{SIZE_CANVAS}")

my_canvas = Canvas(root, width=SIZE_CANVAS, height=SIZE_CANVAS, bg="white")
my_canvas.pack(pady=0)

#image load
im = Image.open('Block0.jpg')
bl0 = ImageTk.PhotoImage(im)
im = Image.open('Block1.jpg')
bl1 = ImageTk.PhotoImage(im)
im = Image.open('Block2.jpg')
bl2 = ImageTk.PhotoImage(im)
im = Image.open('Block3.jpg')
bl3 = ImageTk.PhotoImage(im)
im = Image.open('Block4.jpg')
bl4 = ImageTk.PhotoImage(im)
im = Image.open('Block5.jpg')
bl5 = ImageTk.PhotoImage(im)
im = Image.open('Block6.jpg')
bl6 = ImageTk.PhotoImage(im)
im = Image.open('Block7.jpg')
bl7 = ImageTk.PhotoImage(im)
im = Image.open('Block8.jpg')
bl8 = ImageTk.PhotoImage(im)
im = Image.open('Block9.jpg')
bl9 = ImageTk.PhotoImage(im)
im = Image.open('Block10.jpg')
bl10 = ImageTk.PhotoImage(im)
im = Image.open('Block11.jpg')
bl11 = ImageTk.PhotoImage(im)
im = Image.open('Block12.jpg')
bl12 = ImageTk.PhotoImage(im)

#generate gui
for i in range(SIZE_BOARD):
    for j in range(SIZE_BOARD):
        match gameBoard[i][j]:
            case 0:
                my_canvas.create_image(j*SIZE_BLOCK, i*SIZE_BLOCK, image=bl0, anchor=NW)
            case 1:
                my_canvas.create_image(j*SIZE_BLOCK, i*SIZE_BLOCK, image=bl1, anchor=NW)
            case 2:
                my_canvas.create_image(j*SIZE_BLOCK, i*SIZE_BLOCK, image=bl2, anchor=NW)
            case 3:
                my_canvas.create_image(j*SIZE_BLOCK, i*SIZE_BLOCK, image=bl3, anchor=NW)
            case 4:
                my_canvas.create_image(j*SIZE_BLOCK, i*SIZE_BLOCK, image=bl4, anchor=NW)
            case 5:
                my_canvas.create_image(j*SIZE_BLOCK, i*SIZE_BLOCK, image=bl5, anchor=NW)
            case 6:
                my_canvas.create_image(j*SIZE_BLOCK, i*SIZE_BLOCK, image=bl6, anchor=NW)
            case 7:
                my_canvas.create_image(j*SIZE_BLOCK, i*SIZE_BLOCK, image=bl7, anchor=NW)
            case 8:
                my_canvas.create_image(j*SIZE_BLOCK, i*SIZE_BLOCK, image=bl8, anchor=NW)
            case 9:
                my_canvas.create_image(j*SIZE_BLOCK, i*SIZE_BLOCK, image=bl9, anchor=NW)
            case 10:
                my_canvas.create_image(j*SIZE_BLOCK, i*SIZE_BLOCK, image=bl10, anchor=NW)
            case 11:
                my_canvas.create_image(j*SIZE_BLOCK, i*SIZE_BLOCK, image=bl11, anchor=NW)
            case 12:
                my_canvas.create_image(j*SIZE_BLOCK, i*SIZE_BLOCK, image=bl12, anchor=NW)
#grid
for i in range(0,SIZE_CANVAS,SIZE_BLOCK):
    my_canvas.create_line(0, i, SIZE_CANVAS, i, fill="grey")
    my_canvas.create_line(i, 0, i, SIZE_CANVAS, fill="grey")

root.mainloop()

