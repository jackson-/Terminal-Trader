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
		while(True):
			answer =  input('''

		Are you a banker or a client?
			''')
			if answer == 'banker' or answer == 'client':
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
		while(True):
			choice =  input('''
		[1] Manage Bank Accounts
		[2] Create Bank Account
		[3] Delete Bank Account
		[4] Logout

		What would you like to do?:  
			''')
			if choice == '1' or choice == '2' or choice == '3' or choice == '4':
				return choice
			else:
				Views.invalid()


	@staticmethod
	def account_register():
		while(True):
			name =  input('''
		What would you like to name your new account?:  
			''')
			balance =  input('''
		How much is the initial balance?:  
			''')
			balance = int(balance)
			if balance < 0:
				Views.invalid()
			else:
				return(name, balance)

	@staticmethod
	def account_chooser(accounts):
		while(True):
			for account in accounts:
				print('''
			Account Name: {0}
			Balance: {1}
				'''.format(account.account_name, account.balance))
			account_name = input("What is the name of the account you want to manage?:  ")
			for account in accounts:
				if account_name == account.account_name:
					return account
				else:
					Views.invalid()

	@staticmethod
	def all_or_one():
		while(True):
			answer =  input('''

		Do you want to delete all accounts or just one?
			''')
			if answer == 'all' or answer == 'one':
				return answer
			else:
				Views.invalid()

	@staticmethod
	def account_delete(accounts):
		while(True):
			for account in accounts:
				print('''
			Account Name: {0}
			Balance: {1}
			Account Number: {2}
				'''.format(account.account_name, account.balance, account.account_number))
			account_name = input("What is the name of the account you want to delete?:  ")
			for account in accounts:
				if account_name == account.account_name:
					return account
				else:
					Views.invalid()

	@staticmethod
	def account_manager(account):
		while(True):
			print('''
			Account Name: {0}
			Balance: {1}
				'''.format(account.account_name, account.balance))
			choice = input('''
		[1] Deposit
		[2] Withdraw
		[3] Transfer
		[4] Main Menu

		What would you like to do?:  
			''')
			if choice is '1' or choice is '2' or choice is '3' or choice is '4':
				return choice
			else:
				Views.invalid()

	def account_deposit(account):
		print('''
		Account Name: {0}
		Balance: {1}
			'''.format(account.account_name, account.balance))
		amount = input('''
		How much would you like to deposit?:  
			''')
		if amount.isdigit() != True:
			Views.invalid()
		elif int(amount) < 0:
			Views.invalid()
		else:
			amount = int(amount)
			return amount

	def account_withdraw(account):
		while(True):
			print('''
			Account Name: {0}
			Balance: {1}
				'''.format(account.account_name, account.balance))
			amount = input('''
			How much would you like to withdraw?:  
				''')
			if amount.isdigit() != True:
				Views.invalid()
			elif int(amount) < 0:
				Views.invalid()
			elif int(amount) > account.balance:
				Views.invalid()
			else:
				amount = int(amount)
				return amount

	def account_transfer(transfer_account, accounts):
		while(True):
			print('''
			Transfer Account Name: {0}
			Balance: {1}
				'''.format(transfer_account.account_name, transfer_account.balance))
			for account in accounts:
				if account.account_name == transfer_account.account_name:
					continue
				else:
					print('''
				Account Name: {0}
				Balance: {1}
					'''.format(account.account_name, account.balance))
			account_name = input('''
			What is the name of the account to transfer to?:  
				''')
			for account in accounts:
				if account_name == account.account_name:
					return account
				else:
					continue
			Views.invalid()

	def transfer_amount(account):
		while(True):
			amount = input('''
			How much would you like to transfer?:  
				''')
			if amount.isdigit() != True:
				Views.invalid()
			elif int(amount) < 0:
				Views.invalid()
			elif int(amount) > account.balance:
				Views.invalid()
			else:
				amount = int(amount)
				return amount