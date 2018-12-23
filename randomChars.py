''' an attempt to randomly generate text
'''

from tkinter import *
from random import randint, sample, choice

class RandomCharsGen:
	def __init__(self):
		self.root = Tk()
		w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
		self.root.overrideredirect(1) # go in full screen mode
		self.root.geometry("%dx%d+0+0"%(w,h))
		self.root.title('Random Characters Generator')
		self.root.attributes('-alpha',0.99)
		# set of characters to choose from
		self.chars = 'abcdefghijklmnopqrstuvwxyz0123456789~`!@#$%^&*()-_+={[}]|\\:;,.<>?/'
		self.fontsChoices = ['Arial', 'Times', 'Comics', 'Sans','Symbol','Courier']

		self.canvas = Canvas(self.root, width=w, height=h, background='black')
		#self.canvas.create_text(w/2, h/2, text="Dhiraj", font=('Arial',16), fill='red')
		self.canvas.pack()
		# quit the program after any keypress or motion of mouse
		self.root.bind('<Any-KeyPress>', quit)
		self.root.bind('<Motion>', quit)
		self.create_random_text()
		
		self.root.mainloop()



	def create_random_text(self):
		r = lambda:randint(0,255) # random number between 0 and 255 to define colors
		self.color = '#%02x%02x%02x' % (r(), r(), r()) # define random colors
		self.color1 = '#%02x%02x%02x' % (r(), r(), r())
		self.color2 = '#%02x%02x%02x' % (r(), r(), r())

		self.xpos = randint(0, self.root.winfo_screenwidth()-10)
		self.ypos = randint(0, self.root.winfo_screenheight()-10)
						
		#self.itm1 = self.canvas.create_text(self.xpos, self.ypos,
		#		 text=sample(self.chars,6),	 font=('Arial',randint(16,24)), fill=self.color)
		
		self.itm1 = self.canvas.create_text(self.root.winfo_screenwidth()/2,
					self.root.winfo_screenheight()/2,
				 	text=sample(self.chars,randint(3,len(self.chars)/2)),
				 	font=(choice(self.fontsChoices),randint(16,34), 'bold'),
				 	fill=self.color)

		self.itm2 = self.canvas.create_text(self.root.winfo_screenwidth()/2,
					self.root.winfo_screenheight()/2 - 60,
				 	text=sample(self.chars,randint(3,len(self.chars)/2)),
				 	font=(choice(self.fontsChoices),randint(16,34), 'bold'),
				 	fill=self.color1)
		
		self.itm3 = self.canvas.create_text(self.root.winfo_screenwidth()/2,
					self.root.winfo_screenheight()/2 + 60,
				 	text=sample(self.chars,randint(3,len(self.chars)/2)),
				 	font=(choice(self.fontsChoices),randint(16,34), 'bold'),
				 	fill=self.color2)

		self.canvas.after(800, self.deleteOld) # repeatedly call deleteOld method aftr 300 milliseconds

		self.canvas.after(800, self.create_random_text)


	def deleteOld(self):
		# use this function to overwrite on previously created items/texts.
		self.canvas.delete(self.itm1, self.itm2, self.itm3)

	def quit(self, event):
		self.root.destroy()


# start the screensaver
if __name__ == '__main__':
	scv = RandomCharsGen()


         
