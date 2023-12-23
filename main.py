from tkinter import *

root=Tk()
game_still_going=True
winner=None
player='X'
board=["_","_","_",
             "_","_","_",
             "_","_","_",
             ]
board2=["_","_","_",
             "_","_","_",
             "_","_","_",
             ]
def start():
    body(root)
    check_if_game_over()

def handle_turn():
    pass

def r(r):
    # global board ,root
    board=["_","_","_",
             "_","_","_",
             "_","_","_",
             ]
    root.destroy()
    root=Tk()
    creat_new(root)
def setboard():
	global board,game_still_going
	board=["_","_","_",
             "_","_","_",
             "_","_","_",
             ]
	game_still_going=True 
def creat_new(r):
    global root
    setboard()
    root=Tk()
    enable()
    body(root)
    y=Label(root,text=str(winner)+' is last winner')
    z=Label(root,text='hello')
    y.grid(row=5,column=2)
    z.grid(row=5,column=3)
    root.mainloop()
    

#defining button fucntions

def block(b):
        b1,b2,b3,b4,b5,b6,b7,b8,b9=body(root)
        b1["state"]="disabled"
        b2["state"]="disabled"
        b3["state"]="disabled"
        b4["state"]="disabled"
        b5["state"]="disabled"
        b6["state"]="disabled"
        b7["state"]="disabled"
        b8["state"]="disabled"
        b9["state"]="disabled"
	
def enable():
        b1,b2,b3,b4,b5,b6,b7,b8,b9=body(root)
        b1["state"]="normal"
        b2["state"]="normal"
        b3["state"]="normal"
        b4["state"]="normal"
        b5["state"]="normal"
        b6["state"]="normal"
        b7["state"]="normal"
        b8["state"]="normal"
        b9["state"]="normal"

def Labl():
    l=Label(root,text=str(winner)+" is current winner")
    l.grid(row=5 , column=1)
				
#main programm logic				
def check_if_game_over():
	check_for_winner()
	check_for_tie()
	
	
def check_for_winner():
	global winner
	row_winner =check_rows()
	colomn_winner=check_colomns()
	diagonal_winner=check_diagonals()
	if row_winner:
		winner=row_winner
	elif colomn_winner:
		winner=colomn_winner
	elif diagonal_winner:
		winner=diagonal_winner
	else:
		winner=None

	
def check_rows():
	global game_still_going
	row_1= board[0] == board[1] ==board[2]!= "_"
	row_2= board[3] == board[4] ==board[5]!= "_"
	row_3= board[6] == board[7] ==board[8]!= "_"
	
	if row_1 or row_2 or row_3 :
		game_still_going=False
	if row_1:
		return board[0]
	elif row_2:
		return board[3]
	elif row_3:
		return board[6]
	else:
		return None
		
def check_colomns():
	global game_still_going
	colomn_1= board[0]==board[3]==board[6]!="_"
	colomn_2= board[1]==board[4]==board[7]!="_"	
	colomn_3= board[2]==board[5]==board[8]!="_"
	
	if colomn_1:
		return board[0]
	elif colomn_2:
		return board[1]
	elif colomn_3:
		return board[2]
	else:
		return None
		
def check_diagonals():
	global game_still_going
	diagonal_1=board[0]==board[4]==board[8]!="_"
	diagonal_2=board[6]==board[4]==board[2]!="_"
	
	if diagonal_1:
		return board[0]
	elif diagonal_2:
		return board[6]
	else:
		return None
		
		
def check_for_tie():
	global game_still_going
	
	if "_" not in board:
		game_still_going=False
		return True
	else:
		return False

    



def swap():
    global player
    if game_still_going:
        if player=="X":
            player="O"
        elif player=="O":
            player="X"
    
def distroy(r):
    r.destroy()
    creat_new(r)
  
def btn_click(b,btn_val):
    global board
    if b['text']=='_' and game_still_going:
        board[btn_val]=b['text']=player
           
        b['fg']='red'
        b['bg']='black'
        swap()
        b["state"]="disabled"
        if game_still_going :
            check_if_game_over()
        else:
            block(b)
            Labl()


def body(root):
   
    l1=Label(root,text='tick tak toe in tkinter')
    b1=Button(root,text=board[0],font=('helvetica',20), height=3 ,width=6, fg='black',command=lambda: btn_click(b1,0), state ="active")
    b2=Button(root,text=board[1],font=('helvetica',20), height=3 ,width=6, fg='black',command=lambda: btn_click(b2,1))
    b3=Button(root,text=board[2],font=('helvetica',20), height=3 ,width=6, fg='black',command=lambda: btn_click(b3,2))
    b4=Button(root,text=board[3],font=('helvetica',20), height=3 ,width=6, fg='black',command=lambda: btn_click(b4,3))
    b5=Button(root,text=board[4],font=('helvetica',20), height=3 ,width=6, fg='black',command=lambda: btn_click(b5,4))
    b6=Button(root,text=board[5],font=('helvetica',20), height=3 ,width=6, fg='black',command=lambda: btn_click(b6,5))
    b7=Button(root,text=board[6],font=('helvetica',20), height=3 ,width=6, fg='black',command=lambda: btn_click(b7,6))
    b8=Button(root,text=board[7],font=('helvetica',20), height=3 ,width=6, fg='black',command=lambda: btn_click(b8,7))
    b9=Button(root,text=board[8],font=('helvetica',20), height=3 ,width=6, fg='black',command=lambda: btn_click(b9,8))
    ex=Button(root,text='reset',font=('helvetica',20),command=lambda: distroy(root), )



    l1.grid(row=0,column=1)
    b1.grid(row=1,column=0)
    b2.grid(row=1 , column=1)
    b3.grid(row=1 , column=2)
    b4.grid(row=2 , column=0)
    b5.grid(row=2 , column=1)
    b6.grid(row=2 , column=2)
    b7.grid(row=3 , column=0)
    b8.grid(row=3 , column=1)
    b9.grid(row=3 , column=2)
    ex.grid(row=4,column=1)

    # return b1,b2,b3,b4,b5,b6,b7,b8,b9

start()

root.mainloop()