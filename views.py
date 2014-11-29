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
	def invalid():
		print('''I'm sorry but that is not a valid answer.''')

	@staticmethod
	def user_prompt(string):
		return input(string)

	@staticmethod
	def user_register():
		username = input('''
	You don't have an account. What do you want your username to be?:  
		''')
		password = input('''
	What will your password be?
			''')
		return(username, password)

	@staticmethod
	def user_verify(user):
		password_try = input('''
	What is your password?:  
		''')
		if password_try == user.password:
			return 'pass'
		else:
			Views.invalid()
			return None

	@staticmethod
	def main_menu():
		while(True):
			choice = input('''
		[1] Accounts
		[2] Investment Portfolios
		[3] Stock Lookup
		[4] Logout

		What would you like to do?:  
			''')
			if choice is '1' or choice is '2' or choice is '3' or choice is '4':
				return choice
			else:
				Views.invalid()

	@staticmethod
	def accounts_main_menu():
		while(True):
			choice = input('''
		[1] Manage Accounts
		[2] Create Accounts
		[3] Delete Accounts
		[4] Main Menu

		What would you like to do?:  
			''')
			if choice is '1' or choice is '2' or choice is '3' or choice is '4':
					return choice
				else:
					Views.invalid()

	@staticmethod
	def account_register():
		return input('''
	You are trying to make a new bank account.

	What would you like to name the account?:  
		''')

	@staticmethod
	def accounts_list(account_list):
		item_num = 0
		for account in account_list:
			item_num += 1
			print('''
			{0}
			Account Name: {1}
			Balance: {2}
				'''.format(item_num, account[3], account[2]))
		return input("What is the name of the account you want to choose?:  ")

	@staticmethod
	def portfolios_main_menu():
		while(True):
			choice = input('''
		[1] Manage Portfolios
		[2] Create Portfolios
		[3] Delete Portfolios
		[4] Main Menu

		What would you like to do?:  
			''')
			if choice is '1' or choice is '2' or choice is '3' or choice is '4':
					return choice
				else:
					Views.invalid()

	@staticmethod
	def portfolio_list(portfolio_list):
		item_num = 0
		for portfolio in portfolio_list:
			item_num += 1
			print('''
			{0}
			Portfolio Name: {1}

				'''.format(item_num, portfolio[3]))
		return input("What is the name of the portfolio you want to choose?:  ")


	@staticmethod
	def account_manager(account):
		for item in account:
			print('''
			Account Name: {0}
			Balance: {1}

			[1] Deposit
			[2] Withdraw
			[3] Delete
			[4] Go back
			[5] Main Menu
				'''.format(item[3], item[2]))
		return input("What is would you like to do?: ")

	@staticmethod
	def portfolio_manager(portfolio, account_name):
		for item in portfolio:
			print('''
			Portfolio Name: {0}
			Account Name: {1}

			[1] Check Inventory
			[2] Buy
			[3] Sell
			[4] Change Account
			[5] Go back
			[6] Main Menu

				'''.format(item[3], account_name))
		return input("What would you like to do?:  ")

	@staticmethod
	def inventory_view(inventory):
		for stock in inventory:
			print('''
			
			Stock Ticker: {0}
			Company Name: {1}
			Buy Price: ${2}
			Quantity: {3}
			Timestamp: {4}

				'''.format(stock[2].upper(), stock[3], stock[4], stock[5], stock[6]))

	@staticmethod
	def stock_lookup(quote):
		while(True):
			search = input('''
		Do you want to search by name or ticker?:  
				''')
			if search == 'name':
				name = input("What is the name of the company to lookup?:  ")
				return('name', name)
			elif search == 'ticker':
				ticker = input("What is the ticker of the company to lookup?:  ")
				return('ticker', ticker)
			else:
				Views.invalid()