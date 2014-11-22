from blessings import Terminal # for formatting TUI
t = Terminal()

class Views:

	@staticmethod
	def clear():
		return print(t.clear)

	@staticmethod
	def sign_in():
		return input('''
	Welcome to the Terminal Trading Game!

		What is your username:
		''')
