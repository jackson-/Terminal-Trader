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

	@staticmethod
	def user_prompt(string):
		return input(string)

	@staticmethod
	def main_menu():
		return input('''
	[1] Bank Accounts
	[2] Investment Portfolios
	[3] Stock Lookup
	[4] Update Profile Info
	[5] Logout

	What would you like to do?:  
		''')

	@staticmethod
	def account_register():
		return input('''
	You don't seem to have any bank accounts. Let's make one.

		What would you like to name the account?:  
		''')