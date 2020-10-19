import tkinter as tk
from tkinter import *
import time

    
window = tk.Tk( )
window.title("8 QUEENS")
window.geometry("1000x630")

canvas = Canvas(window,width=1000,height=620,bg="indianred")
color1="white";color2="black"
canvas.pack()
x1=0;y1=0;x2=70;y2=70
for i in range(8):
    y1=0; y2=70
    if(i%2==0):
        for y in range(8):
            if(y%2==0):
                rc=canvas.create_rectangle(x1,y1,x2,y2,fill=color1)
            else:
                rc=canvas.create_rectangle(x1,y1,x2,y2,fill=color2)
            #print(x1,y1,x2,y2)
            y1+=70; y2+=70
            
        x1+=70; x2+=70
            
    else:
        for y in range(8):
            if(y%2==1):
                rc=canvas.create_rectangle(x1,y1,x2,y2,fill=color1)
            else:
                rc=canvas.create_rectangle(x1,y1,x2,y2,fill=color2)
            #print(x1,y1,x2,y2)
            y1+=70; y2+=70
    
        x1+=70; x2+=70


#B= Button(window,text='Regular Hill Climbing',width=2,bg='blue',fg='black',font='bold')
#canvas.create_window(780,150,window=B,height=30,width=150)

#B= Button(window,text='Random Restart Hill Climbing',width=2,bg='gold2',fg='black',font='bold')
#canvas.create_window(780,200,window=B,height=30,width=220)


#L1 = Label(canvas, text="Select Algorithm",bg='ivory3',fg='black',font='bold')
#canvas.create_window(785,80,window=L1,height=30,width=150)

x1,y1=40,40
x2,y2=110,180
x3,y3=180,320
x4,y4=250,110
x5,y5=320,460
x6,y6=390,250
x7,y7=460,390
x8,y8=530,530
L2 = Label(canvas, text="Q",bg='crimson',fg='black',font='bold')
canvas.create_window(x1,y1,window=L2,height=40,width=30)
L3 = Label(canvas, text="Q",bg='crimson',fg='black',font='bold')
canvas.create_window(x2,y2,window=L3,height=40,width=30)
L4 = Label(canvas, text="Q",bg='crimson',fg='black',font='bold')
canvas.create_window(x3,y3,window=L4,height=40,width=30)
L5 = Label(canvas, text="Q",bg='crimson',fg='black',font='bold')
canvas.create_window(x4,y4,window=L5,height=40,width=30)
L6 = Label(canvas, text="Q",bg='crimson',fg='black',font='bold')
canvas.create_window(x5,y5,window=L6,height=40,width=30)
L7 = Label(canvas, text="Q",bg='crimson',fg='black',font='bold')
canvas.create_window(x6,y6,window=L7,height=40,width=30)
L8 = Label(canvas, text="Q",bg='crimson',fg='black',font='bold')
canvas.create_window(x7,y7,window=L8,height=40,width=30)
L9 = Label(canvas, text="Q",bg='crimson',fg='black',font='bold')
canvas.create_window(x8,x8,window=L9,height=40,width=30)

Q = [[1,0,0,0,0,0,0,0],
     [0,0,0,1,0,0,0,0],
     [0,1,0,0,0,0,0,0],
     [0,0,0,0,0,1,0,0],
     [0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,1,0],
     [0,0,0,0,1,0,0,0],
     [0,0,0,0,0,0,0,1]
     ]

def calHeuristic(x,y):
    cnt = 0
    for z in range(y+1,8):
        if(Q[x][z]==1):
            cnt = cnt+1
    t = x+1
    for z in range(y+1,8):
        if(t<8):
            if(Q[t][z]==1):
                cnt = cnt+1
                t = t+1
    t = x-1
    for z in range(y+1,8):
        if(t>=0):
            if(Q[t][z]==1):
                cnt = cnt+1
                t = t-1
    return cnt


                
ans = 0
for x in range(8):
    for y in range(8):
        if(Q[x][y]==1):
            ans = ans + calHeuristic(x,y)         
print("Heuristic value: ",ans)
h =Label(canvas, text = 'Heuristic Value',bg='indianred',fg='black',font='bold')
canvas.create_window(785,200,window=h,height=100,width=100) 
heu =Label(canvas, text=ans,bg='tomato',fg='black',font='bold')
canvas.create_window(785,250,window=heu,height=40,width=40)   

sx1,sy1=40,40
sx2,sy2=110,320
sx3,sy3=180,530
sx4,sy4=250,390
sx5,sy5=320,180
sx6,sy6=390,460
sx7,sy7=460,110
sx8,sy8=530,250
def solve():
    
    x1,y1=40,40
    x2,y2=110,180
    x3,y3=180,320
    x4,y4=250,110
    x5,y5=320,460
    x6,y6=390,250
    x7,y7=460,390
    x8,y8=530,530
    
    
    sx1,sy1=40,40
    sx2,sy2=110,320
    sx3,sy3=180,530
    sx4,sy4=250,390
    sx5,sy5=320,180
    sx6,sy6=390,460
    sx7,sy7=460,110
    sx8,sy8=530,250
    
    
    for i in range(9):
        canvas.create_window(x1,y1,window=L2,height=40,width=30)
        if(y1!=sy1):
            time.sleep(0.5)
            canvas.update()
            if(y1>sy1):
                y1 = y1-70
            else:
                y1+=70
    for i in range(9):
        window.after(500, lambda: display_procedure()) 
        canvas.create_window(x2,y2,window=L3,height=40,width=30)
        if(y2!=sy2):
            time.sleep(0.5)
            canvas.update()
            if(y2>sy2):
                y2-=70
            else:
                y2+=70
    for i in range(9):
        canvas.create_window(x3,y3,window=L4,height=40,width=30)
        if(y3!=sy3):
            time.sleep(0.5)
            canvas.update()
            if(y3>sy3):
                y3-=70
            else:
                y3+=70
    for i in range(9):
        canvas.create_window(x4,y4,window=L5,height=40,width=30)
        if(y4!=sy4):
            time.sleep(0.5)
            canvas.update()
            if(y4>sy4):
                y4-=70
            else:
                y4+=70
    for i in range(9):
        canvas.create_window(x5,y5,window=L6,height=40,width=30)
        if(y5!=sy5):
            time.sleep(0.5)
            canvas.update()
            if(y5>sy5):
                y5-=70
            else:
                y5+=70
    for i in range(9):
        canvas.create_window(x6,y6,window=L7,height=40,width=30)
        if(y6!=sy6):
            time.sleep(0.5)
            canvas.update()
            if(y6>sy6):
                y6-=70
            else:
                y6+=70
    for i in range(9):
        canvas.create_window(x7,y7,window=L8,height=40,width=30)
        if(y7!=sy7):
            time.sleep(0.5)
            canvas.update()
            if(y7>sy7):
                y7-=70
            else:
                y7+=70
    for i in range(9):
        
        canvas.create_window(x8,y8,window=L9,height=40,width=30)
        if(y8!=sy8):
            time.sleep(0.5)
            canvas.update()
            if(y8>sy8):
                y8-=70
            else:
                y8+=70
    

B= Button(window,text='Play',width=2,bg='darkcyan',fg='black',font='bold',command=solve)
canvas.create_window(780,300,window=B,height=30,width=120)

canvas.pack()    
window.mainloop()