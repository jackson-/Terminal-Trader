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
		return input('''

	What would you like your password to be?
		''')

	@staticmethod
	def permission_prompt():
		answer =  input('''

	Are you a banker or a client?
		''')
		if answer is 'banker' or answer is 'client':
			return answer
		else:
			Views.invalid()
			return None 

	@staticmethod
	def verify_password(user):
		password_try = input('''

	What is your password?:  
		''')
		if password_try != user.password:
			Views.invalid()
			return None
		else:
			return "pass"


	@staticmethod
	def main_menu():
		return input('''
	[1] Manage Bank Accounts
	[2] Create Bank Account
	[3] Logout

	What would you like to do?:  
		''')


	@staticmethod
	def account_register():
		name =  input('''

	What would you like to name the account?:  
		''')
		balance =  input('''

	How much is the initial balance?:  
		''')
		balance = int(balance)
		if balance < 0:
			Views.invalid()
			return None
		else:
			return(name, balance)


	@staticmethod
	def account_chooser(accounts):
		for account in accounts:
			print('''
		Account Name: {0}
		Balance: {1}
			'''.format(account.account_name, account.balance))
		account_name = input("What is the name of the account you want to manage?:  ")
		for account in accounts:
			print('this is acct name', account_name)
			print('this is obj', account.account_name)
			if account_name == account.account_name:
				return account
			else:
				Views.invalid()
				return None