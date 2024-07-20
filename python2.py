from tkinter import *
from PIL import ImageTk,Image
from pygame import mixer 
from functools import partial 



root = Tk()
root.title("musical instrument")
root.geometry("1000x1000")
texts=[]
photos=[]
mixer.init()

instrumentList = ["PIANO","GUITAR", "HARMONIUM","SITAR","FLUTE"]
titlePhotos = []
innerFramePhotos = []

for i in range(5):
    with open(f"{i+1}.txt") as f:
         text = f.read()
         texts.append(text)
         image = Image.open(f"{i+1}.jpeg")
         image = image.resize((400,400))
         innerFramePhotos.append(ImageTk.PhotoImage(image))
         image = image.resize((80,80))
         titlePhotos.append(ImageTk.PhotoImage(image))

buttons = []
for i in range(4):
    i = i+11
    image = Image.open(f"{i}.jpg")
    image = image.resize((50,30))
    buttons.append(ImageTk.PhotoImage(image))

Label(root, text="WHICH IS YOUR FAVORITE INSTRUMENT ? ", font=('Helvetica 25 bold')).pack(pady=20)

def close(popupwindow):
    mixer.music.stop()
    popupwindow.destroy()

def buttonAction(instrument,action):
    if action.upper() == "PLAY":
        if instrument[action]['relief'] == "raised":
            thisInstrument = instrument['name']
            mixer.music.load(f"{thisInstrument}.mp3")
            mixer.music.play()
            instrument[action].config(relief="sunken")
            instrument['pause'].config(relief='raised')
            instrument['resume'].config(relief='raised')
    if action.upper() == "PAUSE":
        if instrument['play']['relief'] == "sunken":
            mixer.music.pause()
            instrument[action].config(relief="sunken")
            instrument['play'].config(relief='raised')
    if action.upper() == "RESUME":
        if instrument['pause']['relief'] == "sunken":
            mixer.music.unpause()
            instrument[action].config(relief="raised")
            instrument['pause'].config(relief='raised')
            instrument['play'].config(relief="sunken")
    if action.upper() == "STOP":
        mixer.music.stop()
        instrument[action].config(relief="raised")
        instrument['pause'].config(relief='raised')
        instrument['play'].config(relief='raised')
        instrument['resume'].config(relief='raised')


def open_popup(instrumentName):
    popupwindow = Toplevel(root)
    popupwindow.attributes('-fullscreen', True)
    popupwindow.title(instrumentName.upper())
    index = instrumentList.index(instrumentName.upper())
    Label(popupwindow, text=texts[index], font="helvectica 20 italic", padx=22,pady=52).pack(anchor="n",side="left")
    Label(popupwindow, image=innerFramePhotos[index], anchor="nw",relief="solid").pack()
    piano= {}
    piano['name']=instrumentName.upper()

    piano['play'] = Button(popupwindow,image=buttons[0], font=('Helvetica',20,'bold'),borderwidth=12,width=50,height=30,bg="green",anchor="w",padx=5)
    piano['play'].config(command = partial(buttonAction,piano,'play'))
    piano['play'].pack()

    piano['pause'] = Button(popupwindow,image=buttons[1], font=('Helvetica',20,'bold'),borderwidth=12,width=50,height=30,bg="grey",anchor="w",padx=5)
    piano['pause'].config(command = partial(buttonAction,piano,'pause'))
    piano['pause'].pack()

    piano['resume'] = Button(popupwindow, image=buttons[2], font=('Helvetica',20,'bold'),borderwidth=12,width=50,height=30,bg="orange",anchor="w",padx=5)
    piano['resume'].config(command =partial(buttonAction,piano,'resume'))
    piano['resume'].pack()

    piano['stop'] = Button(popupwindow, image=buttons[3], font=('Helvetica',20,'bold'),borderwidth=12,width=50,height=30,bg="red",anchor="w",padx=5)
    piano['stop'].config(command = partial(buttonAction,piano,'stop'))
    piano['stop'].pack()

    closeButton = Button(popupwindow, text='CLOSE', font=('Helvetica',20,'bold'),borderwidth=12,height=2,width=5,relief="raised",command = lambda: close(popupwindow),bg="cyan").pack(side="bottom",anchor="se")
loopVar = 0
for instrument in instrumentList:
    click_button = Button(root, image=titlePhotos[loopVar], font=('Helvetica',20,'bold'),borderwidth=12,command = partial(open_popup,instrument)).pack()
    loopVar = loopVar+1

Button(root, text="QUIT",font=('Helvetica',20,'bold'), borderwidth=12,command=root.destroy).pack()

root.mainloop()
