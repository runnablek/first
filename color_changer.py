import tkinter

window=tkinter.Tk()
window.title("Color Changer")
window.geometry("300x300")

lbl=tkinter.Label(window,text="Click to change Screen Color",font=9)

def close_window():
  window.destroy()
def makeYellow():
    window.configure(background="yellow")
def makePink():
    window.configure(background="pink")
def makeGreen():
    window.configure(background="green")
def makeBlue():
    window.configure(background="blue")
def makeRed():
    window.configure(background="red")

btnb =tkinter.Button(window,text="Blue",height=2,width=8,command=makeBlue)
btnr =tkinter.Button(window,text="Red",height=2,width=8,command=makeRed)
btng =tkinter.Button(window,text="Green",height=2,width=8,command=makeGreen)
btnp =tkinter.Button(window,text="Pink",height=2,width=8,command=makePink)
btny =tkinter.Button(window,text="Yellow",height=2,width=8,command=makeYellow)
btne =tkinter.Button(window,text="Exit",height=2,width=8,command=close_window)

lbl.pack()
btnb.pack()
btnr.pack()
btng.pack()
btnp.pack()
btny.pack()
btne.pack()

window.mainloop()