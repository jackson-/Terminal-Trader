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
		[1] Bank Accounts
		[2] Portfolio Accounts
		[3] Logout

		What would you like to do?:  
			''')
			if choice is '1' or choice is '2' or choice is '3':
				return choice
			else:
				Views.invalid()

	@staticmethod
	def bank_account_menu(account):
		while(True):
			print('''
			Account Name: {0}
			Balance: {1}
			Account Number: {2}
				'''.format(account.account_name, account.balance, account.account_number))
			choice = input('''
		[1] Deposit to Bank (Create Money)
		[2] Transfer to Portfolio Account
		[3] Main Menu

		What would you like to do?:  
			''')
			if choice is '1' or choice is '2' or choice is '3':
				return choice
			else:
				Views.invalid()

	@staticmethod
	def bank_deposit(account):
		while(True):
			print('''
			Account Name: {0}
			Balance: {1}
			Account Number: {2}
				'''.format(account.account_name, account.balance, account.account_number))
			amount = input("How much do you want to deposit?")
			if amount.isdigit() != True:
				Views.invalid()
			elif int(amount) < 0:
				Views.invalid()
			else:
				return amount

	@staticmethod
	def deposit_to_bank(bank_account, port_account):
		while(True):
			print('''
			Bank Account Name: {0}
			Balance: {1}
			Bank Account Number: {2}

			Portfolio Account Name: {3}
			Balance: {4}
				'''.format(bank_account.account_name, bank_account.balance, bank_account.account_number, port_account.account_name, port_account.balance))
			amount = input("How much do you want to deposit into bank?")
			if amount.isdigit() != True:
				Views.invalid()
			elif int(amount) < 0:
				Views.invalid()
			elif int(amount) > port_account.balance:
				Views.invalid()
			else:
				return amount

	@staticmethod
	def bank_transfer(port_account, bank_account):
		while(True):
			print('''
			Bank Account Name: {0}
			Balance: {1}
			Account Number: {2}

			Portfolio Account Name: {3}
			Balance: {4}
				'''.format(bank_account.account_name, bank_account.balance, bank_account.account_number, port_account.account_name, port_account.balance))
			amount = input("How much do you want to transfer to portfolio account?")
			if amount.isdigit() != True:
				Views.invalid()
			elif int(amount) < 0:
				Views.invalid()
			elif int(amount) > bank_account.balance:
				Views.invalid()
			else:
				return amount

	@staticmethod
	def bank_account_register():
		while(True):
			account_name =  input('''
		You are trying to make a bank account.

		What would you like to name the account?:  
			''')
			init_balance = input('''
		What is the initial balance?:  
				''')
			if init_balance.isdigit() != True:
				Views.invalid()
			elif int(init_balance) < 0:
				Views.invalid()
			else:
				return(account_name, init_balance)



	@staticmethod
	def accounts_main_menu():
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
	def account_register():
		return input('''
		You are trying to make a new portfolio account.

		What would you like to name the account?:  
			''')

	@staticmethod
	def accounts_list(account_list):
		while(True):
			item_num = 0
			for account in account_list:
				item_num += 1
				print('''
				{0}
				Account Name: {1}
				Balance: {2}
					'''.format(item_num, account.account_name, account.balance))
			account_name = input("What is the name of the account you want to choose?:  ")
			for account in account_list:
				if account_name == account.account_name:
					return account
			Views.invalid()

	@staticmethod
	def account_manager(account):
		while(True):
			print('''
				Account Name: {0}
				Balance: {1}

				[1] Deposit to Bank
				[2] Withdraw from Bank
				[3] Change Account
				[4] Buy
				[5] Sell
				[6] Check Inventory
				[7] Accounts Main Menu
					'''.format(account.account_name, account.balance))
			choice = input("What is would you like to do?: ")
			if choice is '1' or choice is '2' or choice is '3' or choice is '4' or choice is '5' or choice is '6' or choice is '7':
						return choice
			else:
				Views.invalid()

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
	def stock_lookup():
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

	@staticmethod
	def name_result(result):
		while(True):
			for entry in result:
				print('''
		Ticker: {0}
		Exchange: {1}
		Name: {2}
					'''.format(entry['Symbol'], entry['Exchange'], entry['Name']))
			choice = input("What is the ticker of the stock to buy?")
			for entry in result:
				if choice.upper() == entry['Symbol']:
					return entry['Symbol']
				else:
					Views.invalid()

	@staticmethod
	def ticker_result(result, account):
		while(True):
			print('''
		Ticker: {0}
		Price: {1}
		Name: {2}
					'''.format(result['Symbol'], result['LastPrice'], result['Name']))
			choice = input("Do you want to buy this stock? y/n:  ")
			if choice == "y":
				amount = input("How many do you want to buy?:  ")
				if amount.isdigit() != True:
					Views.invalid()
				elif float(amount) < 0:
					Views.invalid()
				elif float(amount) * float(result['LastPrice']) > account.balance:
					Views.invalid()
				else:
					return (choice, amount)
			else:
				Views.invalid()

	@staticmethod
	def check_inventory(purchases):
		while(True):
			for purchase in purchases:
				print('''
		Ticker: {0}
		Company Name: {1}
		Buy Price: {2}
		Quantity: {3}
		Timestamp: {4}
					'''.format(purchase.ticker, purchase.company_name, purchase.buy_price, purchase.amount, purchase.timestamp))
			go_back = input("Say back to quit:  ")
			if go_back == 'back':
				return go_back
			else:
				Views.invalid()

	@staticmethod
	def sell_stock(purchases):
		while(True):
			counter = 0
			for purchase in purchases:
				counter+=1
				print('''
		UID: {0}
		Ticker: {1}
		Company Name: {2}
		Buy Price: {3}
		Quantity: {4}
		Timestamp: {5}
					'''.format(counter, purchase.ticker, purchase.company_name, purchase.buy_price, purchase.amount, purchase.timestamp))
			uid = input("What is the UID of the stock you want to sell?: ")
			amount = input("How many do you want to sell?:  ")
			if uid.isdigit() != True:
				Views.invalid()
			elif len(purchases) < int(uid):
				Views.invalid()
			elif int(amount) > purchases[int(uid)-1].amount:
				Views.invalid()
			else:
				index = int(uid)-1
				return(index, amount)