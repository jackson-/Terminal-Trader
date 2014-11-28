from blessings import Terminal # for formatting TUI
t = Terminal()

class Views:

	@staticmethod
	def clear():
		return print(t.clear)

	@staticmethod
	def invalid():
		print('''I'm sorry but that is not a valid answer.''')

	@staticmethod
	def sign_in():
		return input('''
	Welcome to the Terminal Trading Game!

		What is your username:  
		''')

	@staticmethod
	def user_register():
		return input('''
	You don't have an account with us.

	What would you like your username to be?
		''')

	@staticmethod
	def password_prompt():
		answer = input('''

	What would you like your password to be?
		''')

	@staticmethod
	def permission_prompt():
		answer = input('''

	Are you a banker or a client?
		''')
		if answer == 'banker' or answer == 'client':
			return answer
		else:
			Views.invalid()
