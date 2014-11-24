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
	def profile_manager(user):
		print('''
		Username: {0}
		Password: {1}
		First Name: {2}
		Last Name: {3}

		[1] Change Username
		[2] Change Password
		[3] Change First Name
		[4] Change Last Name
		[5] Main Menu

			'''.format(user.username, user.password, user.first_name, user.last_name,))
		return input("What is would you like to do?: ")

	@staticmethod
	def inventory_view(inventory):
		for stock in inventory:
			print('''
			
			Stock Ticker: {0}
			Company Name: {1}
			Buy Price: {2}

				'''.format(stock[3], stock[2]))