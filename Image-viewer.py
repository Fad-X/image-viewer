from tkinter import *
from PIL import ImageTk, Image

root=Tk()

#FUNCTIONS
def forward(imgNum):
	global forward
	global back
	global img
	
	img.grid_forget()
	img = Label(image=imgList[imgNum -1])
	img.grid(row=0,column=0,columnspan=40)
	
	forwardB = Button(root,text=">>",command=lambda: forward(imgNum+1))
	backB = Button(root,text="<<",command=lambda: back(imgNum-1))
	
	if imgNum ==  len(imgList):
		forwardB = Button(root,text=">>",command=lambda: forward(imgNum+1),state=DISABLED)
	
	

	img.grid(row=0,column=0,columnspan=40)
	forwardB.grid(row=1,column=1)
	backB.grid(row=1,column=0)
	
	imgNo = Label(root, text="Image " + str(imgNum) +" of  " + str(len(imgList)))	
	imgNo.grid(row=2,column=0,columnspan=2)
	
def back(imgNum):
	global forward
	global back
	global img
	global ImgNo
	
	
	img.grid_forget()
	img = Label(image=imgList[imgNum -1])
	img.grid(row=0,column=0,columnspan=40)
	
	forwardB = Button(root,text=">>",command=lambda: forward(imgNum+1))
	backB = Button(root,text="<<",command=lambda: back(imgNum-1))
	
	if imgNum ==  1:
		backB = Button(root,text="<<",command=lambda: forward(imgNum-1),state=DISABLED)
	
	
	img.grid(row=0,column=0,columnspan=40)
	forwardB.grid(row=1,column=1)
	backB.grid(row=1,column=0)
	
	
	imgNo = Label(root,text="Image " + str(imgNum) +" of " + str(len(imgList)))	
	imgNo.grid(row=2,column=0,columnspan=2)
	
# IMAGE
img1=ImageTk.PhotoImage(Image.open("img1.jpg")) 
img2=ImageTk.PhotoImage(Image.open("img2.jpg")) 
img3=ImageTk.PhotoImage(Image.open("img3.jpg")) 
img4=ImageTk.PhotoImage(Image.open("img4.jpg")) 
img5=ImageTk.PhotoImage(Image.open("img5.jpg")) 
img6=ImageTk.PhotoImage(Image.open("img6.jpg")) 
img7=ImageTk.PhotoImage(Image.open("img7.jpg")) 
img8=ImageTk.PhotoImage(Image.open("img8.jpg")) 
img9=ImageTk.PhotoImage(Image.open("img9.jpg")) 
img10=ImageTk.PhotoImage(Image.open("img10.jpg")) 
img11=ImageTk.PhotoImage(Image.open("img11.jpg")) 
img12=ImageTk.PhotoImage(Image.open("img12.jpg")) 
img13=ImageTk.PhotoImage(Image.open("img13.jpg")) 
img14=ImageTk.PhotoImage(Image.open("img14.jpg")) 
img15=ImageTk.PhotoImage(Image.open("img15.jpg")) 
img16=ImageTk.PhotoImage(Image.open("img16.jpg")) 
img17=ImageTk.PhotoImage(Image.open("img17.jpg")) 

imgList = [
    img1,
    img2,
    img3,
    img4,
    img5,
    img6,
    img7,
    img8,
    img9,
    img10,
    img11,
    img13,
    img13,
    img14,
    img15,
    img16,
    img17,
    ]


#LABELS
img=Label(image=img1)

imgNo = Label(root,text= "Image 1 of  "+str(len(imgList)))
#BUTTONS
forwardB = Button(root,text=">>",command=lambda: forward(2))
backB = Button(root,text="<<",command=lambda: back(1))
terminate = Button(root,text="Exit",command=root.quit)

#OUTPUT
img.grid(row=0,column=0,columnspan=40)
forwardB.grid(row=1,column=1)
backB.grid(row=1,column=0)
imgNo.grid(row=2,column=0,columnspan=2)
terminate.grid(row=3,column=0,columnspan=2)















root.mainloop()
