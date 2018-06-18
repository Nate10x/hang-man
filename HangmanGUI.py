import tkinter as tk
from tkinter import ttk
from Game import *
from widgets import *

#fonts
title_font = ("serif", 45, "bold")
big_font = ("serif", 30, "bold")
normal_font = ("serif", 20)
entry_font = ("serif", 13)
buttonBig_font = ("serif", 35, "bold")
button_font = ("serif", 12, "bold")
button2_font = ("serif", 10, "bold")
comment_font = ("serif", 18)

#colors
canvas_color = "antique white"
darker_bg = "black"
#darker_bg = "#5aa57c"
bg_color = "#16e9af"
text_color = "white"

class Hangman(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.geometry("1500x700")
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		
		self.frames = {}

		for F in (StartPage, GamePage1, GamePage2):
			frame = F(container, self)
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky = "nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

	def set_label(self, value):
		print(value)
		self.display_phrase.set(value)


class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.configure(bg=bg_color)
		top = tk.Frame(self)
		top.pack(side = "top")

		labelTitle = tk.Label(top, font=title_font, text="Pythonic Hangman", bg=darker_bg, bd=5, relief="raised", fg=text_color)
		labelTitle.grid(column=10, row=10)
		labelTitle.config(highlightbackground="black", highlightthickness=10)

		s = ttk.Style()
		s.configure('mainbuttons.TButton', font=buttonBig_font, width=7, background="black", foreground="black")

		play_butt = ttk.Button(self, text="Play", style="mainbuttons.TButton", command=lambda: controller.show_frame(GamePage1))
		play_butt.pack(pady=(20,20))

		options_butt = ttk.Button(self, text="Options", style="mainbuttons.TButton")
		options_butt.pack(pady=(20,20))

		about_butt = ttk.Button(self, text="About", style="mainbuttons.TButton")
		about_butt.pack(pady=(20,20))


class GamePage1(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.config(bg=bg_color)
		top = tk.Frame(self)
		top.pack(side = "top")

		labelTitle = tk.Label(top, font=title_font, text="Pythonic Hangman", bg=darker_bg, bd=5, relief="raised", fg=text_color)
		labelTitle.grid(column=10, row=10)
		labelTitle.config(highlightbackground="black", highlightthickness=10)

		margin1 = tk.Frame(self, height=10, bg=bg_color)
		margin1.pack()

		middle = tk.Frame(self, bg=bg_color, bd=10, relief="ridge")
		middle.pack()
		middle.config(highlightbackground=bg_color)

		phrase_label = tk.Label(middle, font=normal_font, text="Phrase: ", bg=bg_color, width=25, anchor="w")
		phrase_label.grid(column=10, row=10, sticky="w")

		secret_phrase = tk.StringVar(middle)

		secretEntry = ttk.Entry(middle, textvariable=secret_phrase, font=entry_font)
		secretEntry.grid(column=11, row=10,padx=(20,0))

		category_label = tk.Label(middle, font=normal_font, text="Category: ", bg=bg_color, width=25, anchor="w")
		category_label.grid(column=10, row=11, sticky="w")

		category_choice = tk.StringVar(middle)

		category_choices = ['Movies                    ',
							'Movies                    ',
						    'Places                    ',
						    'Things                    ',
						    'Famous                 ',
						    'Cliche                     ',
						    'Humor                    ',
						    'Programming       ',
						    'Other                       ',]
		category_choice.set("Movies")

		s = ttk.Style()
		s.configure('categoryMenu.TMenubutton', font=button_font)
		s.configure('submit.TButton', font=button_font, width=7, background="black", foreground="black")

		categoryMenu = ttk.OptionMenu(middle, category_choice, *category_choices, style="categoryMenu.TMenubutton")###
		categoryMenu.grid(column=11, row=11)

		submitButt = ttk.Button(self, text="Play!", style="submit.TButton", command=lambda: self.startGame(secret_phrase, category_choice))
		submitButt.pack(pady=(20,20))

		back = ttk.Button(self, text="back", style="back.TButton", command=lambda: controller.show_frame(StartPage))
		back.pack(side="bottom")

	#~~~~~~~~~GAME STARTS HERE~~~~~~~~~~		
	def startGame(self, secret_phrase, category_choice):
			category = category_choice.get()
			temp=""
			for char in category:
				if char == " ":
					break
				temp += char
			category = temp
			game = Game(secret_phrase.get(), category)
			gp.phrase_label.config(text = game.game_display_guessed)
			gp.category_label.config(text= "Category: " + category)
			gp.commentary_label.config(text="Ok you can do this, good luck.")
			gp.guess_butt.config(command=lambda:game.send_guess())
			gp.solve_butt.config(command=lambda:game.send_solve())
			self.controller.show_frame(GamePage2)
			game.draw_start(gp.hangman_canvas)

class GamePage2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.config(bg=bg_color)
		gp.hangman_canvas = tk.Canvas(self, height=200,width=300, bg=canvas_color, bd=10, relief="raised")
		gp.hangman_canvas.pack(pady=(10,40))
		gp.hangman_canvas.config(highlightbackground="black")

		gp.phrase_label = tk.Label(self, font=title_font, text="", bd=5, bg=darker_bg, relief="sunken", fg=text_color)
		gp.phrase_label.pack()
		gp.phrase_label.config(highlightbackground="black")

		cat_frame = tk.Frame(self, bg=bg_color)
		cat_frame.pack()
		gp.category_label =tk.Label(cat_frame, font=big_font, text="", bd=10, relief="raised", bg=darker_bg, fg=text_color)
		gp.category_label.grid(column=0, row=0, pady=(40,20))
		gp.category_label.config(highlightbackground="black")

		gp.commentary_label = tk.Label(self, text="", font=comment_font, bg=bg_color)
		gp.commentary_label.pack(pady=(30,30))

		container_frame = tk.Frame(self, bg=bg_color)
		container_frame.pack()
		
		gp.guess = tk.StringVar()

		entry_guess = ttk.Entry(container_frame, width=5, textvariable=gp.guess)
		entry_guess.grid(column=10, row=10, padx=(0,10))

		s = ttk.Style()
		s.configure('buttons.TButton', font=button2_font, width=7, background="black", foreground="black")
		s.configure('back.TButton', font=button_font, width=7, background="black", foreground="black")
		s.configure('main.TButton', font=button_font, width=12, background="black", foreground="black")

		gp.guess_butt = ttk.Button(container_frame, text="Guess", style="buttons.TButton")
		gp.guess_butt.grid(column=9, row=10)

		gp.solve_butt = ttk.Button(container_frame, text="Solve", style="buttons.TButton")
		gp.solve_butt.grid(column=11, row=10)

		gp.solve = tk.StringVar()

		entry_solve = ttk.Entry(container_frame, textvariable=gp.solve)
		entry_solve.grid(column=12, row=10, padx=(0,10))

		bottom_buttons = tk.Frame(self, bg=bg_color)
		bottom_buttons.pack(side="bottom")

		back = ttk.Button(bottom_buttons, text="Back", style="back.TButton", command=lambda: self.clear_canvas("back"))
		back.grid(column=10, row=10, padx=(0,5))
		main = ttk.Button(bottom_buttons, text="Main Menu", style="main.TButton", command=lambda: self.clear_canvas("main"))
		main.grid(column=11, row=10, padx=(5,0))
		self.controller.show_frame(GamePage1)
	def clear_canvas(self, page):
		if page == "back":
			self.controller.show_frame(GamePage1)
		else:
			self.controller.show_frame(StartPage)
		gp.hangman_canvas.delete("all")
		gp.solve_butt.config(state="normal")
		gp.guess_butt.config(state="normal")


app = Hangman()
app.mainloop()

