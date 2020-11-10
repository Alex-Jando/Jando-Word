from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser



class Gui:

	def __init__(self, root):
		self.root = root

		# File Menu Setup
		self.menubar = Menu(self.root)
		self.filemenu = Menu(self.menubar, tearoff=0)
		self.filemenu.add_command(label="New", command = self.New)
		self.filemenu.add_command(label="Open", command = self.Open)
		self.filemenu.add_command(label="Save", command = self.Save)
		self.menubar.add_cascade(label="File", menu=self.filemenu)

		# Fonts Menu Setup

		self.fontsmenu = Menu(self.menubar, tearoff=0)
		self.fontsmenu.add_command(label="Arial", command = self.Arial)
		self.fontsmenu.add_command(label="Times New Roman", command = self.Times)
		self.fontsmenu.add_command(label="System", command = self.Sys)
		self.fontsmenu.add_command(label="Change Colour", command = self.change_colour)
		self.menubar.add_cascade(label="Fonts", menu=self.fontsmenu)

		# Edits Menu Setup

		self.editmenu = Menu(self.menubar, tearoff=0)
		self.editmenu.add_command(label="Copy (CTRL + C)", command = self.copy)
		self.editmenu.add_command(label="Paste (CTRL + V)", command = self.paste)
		self.editmenu.add_command(label="Cut (CTRL + X)", command = self.cut)
		self.menubar.add_cascade(label="Edit", menu=self.editmenu)

		# Exit Menu
		self.exitmenu = Menu(self.menubar, tearoff=0)
		self.exitmenu.add_command(label="Exit", command = root.quit)
		self.menubar.add_cascade(label="Exit", menu=self.exitmenu)

		# File Menu Display
		self.root.config(menu=self.menubar)

		# Make Ehe Entry Box
		global txt_box
		txt_box = Text(self.root, border=5, width=200, height=200, font=("Arial", 12))
		txt_box.pack()
		txt_box.config(font="arial", selectbackground="gray")

	def New(self):
		txt_box.delete(1.0,END)
		self.file =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Text Documents","*.txt"),("Python Documents","*.py")))
		self.filenametemp = self.file.split("/")
		self.filelen = len(self.filenametemp)
		self.filename = str()
		self.filename = self.filenametemp[self.filelen-1]
		self.newfile = open(self.filename + ".txt", "w")
		self.newfile.write()
		self.newfile.close()

	def Open(self):
		txt_box.delete(1.0,END)
		self.openfile =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text Documents","*.txt"),("Python Documents","*.py")))
		with open(self.openfile, "r") as opened:
			self.txt = opened.read()
		txt_box.insert(1.0, self.txt)

	def Save(self):
		self.current_txt = txt_box.get(1.0, END)
		self.file =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Text Documents","*.txt"),("Python Documents","*.py")))
		self.filenametemp = self.file.split("/")
		self.filelen = len(self.filenametemp)
		self.filename = str()
		self.filename = self.filenametemp[self.filelen-1]
		self.newfile = open(self.filename + ".txt", "w")
		self.newfile.write(self.current_txt)

	def Arial(self):
		txt_box.config(font="arial")
		self.root.geometry("1000x575")

	def Times(self):
		txt_box.config(font="times")
		self.root.geometry("1000x575")

	def Sys(self):
		txt_box.config(font="system")
		self.root.geometry("1000x575")

	def change_colour(self):
		self.descoltemp = colorchooser.askcolor(color=None)
		self.descol = str()
		self.descol = self.descoltemp[1]
		txt_box.config(fg=self.descol)

	def copy(self):
		self.copy_txt = txt_box.selection_get()
		self.root.clipboard_append(self.copy_txt)

	def cut(self):
		self.copy_txt = txt_box.selection_get()
		self.root.clipboard_append(self.copy_txt)
		txt_box.delete(SEL_FIRST, SEL_LAST)

	def paste(self):
		self.paste = self.root.clipboard_get()
		txt_box.insert(INSERT, self.paste)
		try:
			txt_box.delete(SEL_FIRST, SEL_LAST)
		except:
			pass

root = Tk()

root.title("Jando Word")
root.resizable(width="false", height="false")
root.iconbitmap('Jando_Word.ico')
root.geometry("1000x575")

App = Gui(root)

root.clipboard_clear()

root.mainloop()