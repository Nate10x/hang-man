from widgets import *
import tkinter as tk
from widgets import gp

class Game:
	guessed = ""
	guessed_list = []
	game_display_guessed = ""
	step = 0

	def __init__(self, phrase, category):
		self.phrase = phrase
		self.category = category
		self.guessed_list = []
		
		for char in phrase:
			if char == " ":
				self.guessed += " "
			else:
				self.guessed += "_"
		for char in self.guessed:
			self.guessed_list.append(char)
		self.guessed = ""
		for char in self.guessed_list:
			self.guessed += char
		for char in self.guessed_list:
			if char == " ":
				self.game_display_guessed += " "
			self.game_display_guessed += char + " "
	

	def send_guess(self):
		try:
			empty = gp.guess.get()[1]
			gp.commentary_label.config(text="One letter at a time please!")
		except:
			if gp.guess.get() == "":
				gp.commentary_label.config(text="Atleast try!")
			else:
				self.check_guessORsolve(gp.guess.get(), "guess")		
		gp.guess.set("")

	def send_solve(self):
		if gp.solve.get() == "":
			gp.commentary_label.config(text="Quit goofing off!")
		else:
			self.check_guessORsolve(gp.solve.get(), "solve")
		gp.solve.set("")
	

	def check_guessORsolve(self, guesSolve, guess_or_solve ):
		
		if guess_or_solve == "guess":
			index_of_letters_to_display =[]
			letters_to_display = []
			guess = guesSolve
			for letter in enumerate(self.phrase):
				if letter[1] == guess:
					letters_to_display.append(letter[1])
					index_of_letters_to_display.append(letter[0])
			if letters_to_display != []:
				self.add_letter(letters_to_display, index_of_letters_to_display)
			else:
				self.add_limb()


		else:
			solve = guesSolve
			if solve == self.phrase:
				self.guessed = solve
				self.WIN()
			else:
				self.add_limb()
			
	
	def add_letter(self,letters, indexes):
		for i in enumerate(indexes):
			INDEX1 = i[0]
			INDEX2 = i[1]
			LETTER = letters[INDEX1]
			self.guessed_list[INDEX2] = LETTER
		self.game_display_guessed = ""
		for char in self.guessed_list:
			if char == " ":
				self.game_display_guessed += " "
			self.game_display_guessed += char + " "
		gp.phrase_label.config(text=self.game_display_guessed)
		gp.commentary_label.config(text=positive_message)
		self.win_or_gameover()

	def add_limb(self):
		self.step += 1
		steps = {'1': self.draw_step1,'2':self.draw_step2,'3':self.draw_step3,'4':self.draw_step4,'5':self.draw_step5,'6':self.draw_step6}
		steps[str(self.step)](gp.hangman_canvas)
		gp.commentary_label.config(text=negative_message)
		self.win_or_gameover()

	def win_or_gameover(self):
		if self.step == 6:
			self.LOSE()
		self.guessed = ""
		for char in self.guessed_list:
			self.guessed += char
		if self.guessed == self.phrase:
			self.WIN()



	def WIN(self):
		self.game_display_guessed = ""
		for char in self.phrase:
			if char == " ":
				self.game_display_guessed += " "
			self.game_display_guessed += char + " "
		gp.phrase_label.config(text=self.game_display_guessed)
		gp.commentary_label.config(text="Congratulations... You Win.\n press back to reset and play again...")
		gp.guess_butt.config(state="disabled")
		gp.solve_butt.config(state="disabled")

	def LOSE(self):
		gp.commentary_label.config(text="Ouch... Better Luck Next Time.\n press back to reset and play again...")
		gp.guess_butt.config(state="disabled")
		gp.solve_butt.config(state="disabled")

	def printVars(self):
		print("below are the class variables: ")
		print("step: ", self.step)
		print("phrase: ", self.phrase)
		print("guessed_list: ", self.guessed_list)
		print("guessed: ", self.guessed)
		print("game_display_guessed: ", self.game_display_guessed)


	def draw_start(self, canvas):
		wood_pole = canvas.create_rectangle(270,15,300,500, width = 2, fill = "brown")
		wood_branch = canvas.create_rectangle(160,25,270,15, width = 2, fill = "brown")
		noose = canvas.create_line(160,25,160,100, width = 2, fill = "grey")
		#this noose is longer than other noose
		knot = canvas.create_oval(155,100,165,110, width = 2, fill = "grey")
	def draw_step1(self, canvas):
		wood_pole = canvas.create_rectangle(270,15,300,500, width = 2, fill = "brown")
		wood_branch = canvas.create_rectangle(160,25,270,15, width = 2, fill = "brown")
		noose = canvas.create_line(160,25,160,40, width = 2, fill = "grey")
		#this noose is shorter than other noose
		head = canvas.create_oval(130,40,190,100, width = 2, fill = head_color, outline = "black")
	def draw_step2(self, canvas):
		wood_pole = canvas.create_rectangle(270,15,300,500, width = 2, fill = "brown")
		wood_branch = canvas.create_rectangle(160,25,270,15, width = 2, fill = "brown")
		noose = canvas.create_line(160,25,160,40, width = 2, fill = "grey")
		#this noose is shorter than other noose
		head = canvas.create_oval(130,40,190,100, width = 2, fill = head_color, outline = "black")
		torso = canvas.create_line(160,100,160,155, width = 2, fill = "black")
		knot = canvas.create_oval(155,100,165,110, width = 2, fill = "grey")
	def draw_step3(self, canvas):
		wood_pole = canvas.create_rectangle(270,15,300,500, width = 2, fill = "brown")
		wood_branch = canvas.create_rectangle(160,25,270,15, width = 2, fill = "brown")
		noose = canvas.create_line(160,25,160,40, width = 2, fill = "grey")
		#this noose is shorter than other noose
		head = canvas.create_oval(130,40,190,100, width = 2, fill = head_color, outline = "black")
		torso = canvas.create_line(160,100,160,155, width = 2, fill = "black")
		knot = canvas.create_oval(155,100,165,110, width = 2, fill = "grey")
		left_arm = canvas.create_line(160,110,130,140, width = 2, fill = "black")
	def draw_step4(self, canvas):
		wood_pole = canvas.create_rectangle(270,15,300,500, width = 2, fill = "brown")
		wood_branch = canvas.create_rectangle(160,25,270,15, width = 2, fill = "brown")
		noose = canvas.create_line(160,25,160,40, width = 2, fill = "grey")
		#this noose is shorter than other noose
		head = canvas.create_oval(130,40,190,100, width = 2, fill = head_color, outline = "black")
		torso = canvas.create_line(160,100,160,155, width = 2, fill = "black")
		knot = canvas.create_oval(155,100,165,110, width = 2, fill = "grey")
		left_arm = canvas.create_line(160,110,130,140, width = 2, fill = "black")
		right_arm = canvas.create_line(160,110,190,140, width = 2, fill = "black")
	def draw_step5(self, canvas):
		wood_pole = canvas.create_rectangle(270,15,300,500, width = 2, fill = "brown")
		wood_branch = canvas.create_rectangle(160,25,270,15, width = 2, fill = "brown")
		noose = canvas.create_line(160,25,160,40, width = 2, fill = "grey")
		#this noose is shorter than other noose
		head = canvas.create_oval(130,40,190,100, width = 2, fill = head_color, outline = "black")
		torso = canvas.create_line(160,100,160,155, width = 2, fill = "black")
		knot = canvas.create_oval(155,100,165,110, width = 2, fill = "grey")
		left_arm = canvas.create_line(160,110,130,140, width = 2, fill = "black")
		right_arm = canvas.create_line(160,110,190,140, width = 2, fill = "black")
		left_leg = canvas.create_line(160,152,140,200, width = 2, fill = "black")
	def draw_step6(self, canvas):
		head = canvas.create_oval(130,40,190,100, width = 2, fill = dead_color, outline = "black")
		torso = canvas.create_line(160,100,160,155, width = 2, fill = "black")
		left_arm = canvas.create_line(160,110,130,140, width = 2, fill = "black")
		right_arm = canvas.create_line(160,110,190,140, width = 2, fill = "black")
		left_leg = canvas.create_line(160,152,140,200, width = 2, fill = "black")
		right_leg = canvas.create_line(160,152,180,200, width = 2, fill = "black")
		wood_pole = canvas.create_rectangle(270,15,300,500, width = 2, fill = "brown")
		wood_branch = canvas.create_rectangle(160,25,270,15, width = 2, fill = "brown")
		noose = canvas.create_line(160,25,160,40, width = 2, fill = "grey")
		knot = canvas.create_oval(155,100,165,110, width = 2, fill = "grey")
		#(left-x,bottom-y,right-x,top-y)(160,110,225,175)


	