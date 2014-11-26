from models import User, Portfolio, Account, Stock, DB_API, markit
from views import Views
import re
# markit = markit_wrapper.Markit()

class Controller(object):

	def sign_in(self):
		while(True):
			self.username = Views.sign_in()
			self.user = DB_API.fetch_user(self.username)
			if self.user == None:
				Views.clear()
				return self.user_registration()
			else:
				Views.clear()
				self.user = User(self.user[0][0], self.username, self.user[0][2], self.user[0][3], self.user[0][4])
				print(self.user.password)
				password_attempt = Views.user_prompt("What is your password?:  ")
				if password_attempt != self.user.password:
					Views.clear()
					print("I'm sorry that was the wrong password?")
					continue
				else:
					Views.clear()
					return self.main_menu()

	def user_registration(self):
		while(True):
			choice = Views.user_prompt("You don't seem to have an account with us. Would you like to register? Y/N?: ")
			if choice == "y" or choice == "Y":
				self.first_name = Views.user_prompt("What is your first name?:  ")
				self.last_name = Views.user_prompt("What is your last name?:  ")
				self.password = Views.user_prompt("What is your password?:  ")
				DB_API.create_user(self.username, self.password, self.first_name, self.last_name)
				self.user = DB_API.fetch_user(self.username)
				self.user = User(self.user[0][0], self.user[0][1], self.user[0][2], self.user[0][3], self.user[0][4])
				return self.main_menu()
			elif choice == "n" or choice == "N":
				return self.sign_in()

	def main_menu(self):
		while(True):
			choice = Views.main_menu()
			if choice == "1":
				self.account_menu()
			elif choice =="2":
				self.portfolio_list()
			elif choice =="3":
				self.stock_lookup()
			elif choice =="4":
				self.profile_manager()
			elif choice =="5":
				self.sign_in()
			else:
				Views.invalid()

	def account_menu(self):
		while(True):
			choice = Views.account_menu()
			if choice == "1":
				self.accounts_view()
			elif choice == "2":
				account_name = Views.account_register()
				init_balance = Views.user_prompt("What will be the initial balance?: ")
				if int(init_balance) < 1:
					Views.invalid()
				else:
					self.user.create_account(account_name, init_balance)
			
	def accounts_view(self):
		while(True):
			account_list = DB_API.fetch_accounts(self.username)
			if account_list == None:
				self.account_registration()
			else:
				account_name = Views.accounts_list(account_list)
				account = DB_API.fetch_account_by_name(account_name, self.username)
				if account == None:
					Views.invalid()
					continue
				else:
					self.account_edit(account)

	def account_registration(self):
		while(True):
			account_name = Views.account_register()
			init_balance = Views.user_prompt("What will be the initial balance?: ")
			if int(init_balance) < 1:
				Views.invalid()
			else:
				self.user.create_account(account_name, init_balance)
				self.account_menu()

	def account_edit(self, account):
		while(True):
			self.account = Account(account[0][0], account[0][1], account[0][2], account[0][3], account[0][4])
			choice = Views.account_manager(account)
			if choice == "1":
				amount = Views.user_prompt("How much would you like to deposit?: ")
				if int(amount) < 1:
					Views.invalid()
				else:
					self.account.deposit(amount)
					self.accounts_view()
			elif choice == "2":
				amount = Views.user_prompt("How much would you like to withdraw?: ")
				if int(amount) < 1:
					Views.invalid()
				elif int(amount) > self.account.balance:
					print("Error: You don't have that much")
				else:
					self.account.withdraw(amount)
					self.accounts_view()
			elif choice == "3":
				deleter = Views.user_prompt("Are you sure you want to delete this account? Y/N: ")
				if deleter == "Y" or deleter =="y":
					self.account.delete_self()
					self.main_menu()
				elif deleter == "N" or deleter == "n":
					continue
				else:
					Views.invalid()
			elif choice == "4":
				self.account_manager()
			elif choice == "5":
				self.main_menu()
			else:
				Views.invalid()

	def portfolio_view(self, portfolio):
		while(True):
			account = DB_API.fetch_account_by_portfolio(portfolio[0][3], self.username)
			account_name = account[0][0]
			self.portfolio = Portfolio(portfolio[0][0], self.username, portfolio[0][3], account_name)
			choice = Views.portfolio_manager(portfolio, account_name)
			if choice == "1":
				inventory =  DB_API.fetch_portfolio_inventory(self.username, self.portfolio.portfolio_name)
				if inventory == None:
					print("You do not seem to have any stocks. Go buy some!")
				else:
					Views.inventory_view(inventory)
			elif choice == "2":
				ticker = Views.user_prompt("What is the stock ticker?")
				amount = Views.user_prompt("How many would you like to buy?")
				buy = self.portfolio.buy_stock(ticker, amount)
				if buy == None:
					Views.invalid()
				elif buy == False:
					print("Not enough in account!")
				self.portfolio_list()
			elif choice == "3":
				pass
			elif choice == "4":
				account_list = DB_API.fetch_accounts(self.username)
				account_name = Views.account_list(account_list)
				account = DB_API.fetch_account_by_name(account_name ,self.username)
				account_id = account[0][0]
				self.portfolio.change_account(account_id, self.username, self.id)
				self.portfolio_list()
			elif choice == "5":
				self.portfolio_list()
			elif choice == "6":
				self.main_menu()
			else:
				Views.invalid()

	def portfolio_list(self):
		while(True):
			portfolio_list = DB_API.fetch_portfolios(self.username)
			if portfolio_list == None:
				self.portfolio_registration()
			else:
				portfolio_name = Views.portfolio_list(portfolio_list)
				portfolio = DB_API.fetch_portfolio_by_name(self.username, portfolio_name)
				if portfolio == None:
					Views.invalid()
				else:
					self.portfolio_view(portfolio)

	def portfolio_registration(self):
		while(True):
			portfolio_name = Views.user_prompt("You don't seem to have any portfolios. Let's make one. What would you like to name it?:  ")
			account_list = DB_API.fetch_accounts(self.username)
			if account_list == None:
				print("You don't seem to have any bank accounts to hook up to your portfolio.\n Let's make one now.")
				self.account_registration()
			else:
				account_name = Views.accounts_list(account_list)
				account = DB_API.fetch_account_by_name(account_name, self.username)
				if account == None:
					Views.invalid()
				else:
					self.user.create_portfolio(self.username, account_name, portfolio_name)
					self.portfolio_list()

	def stock_lookup(self):
		while(True):
			style_choice = Views.user_prompt("Would you like to find the company by name or ticker?")
			if style_choice == 'ticker':
				ticker = Views.user_prompt("What is the ticker of the company to look up?")
				quote = markit.get_quote(ticker)
				if quote == None:
					Views.invalid()
				else:
					Views.stock_lookup(quote)
					self.main_menu()
			elif style_choice == 'name':
				name = Views.user_prompt("What is the name of the company to look up?")
				search = markit.company_search(name)
				if search == None:
					Views.invalid()
				else:
					symbol = search[0]['Symbol']
					quote = markit.get_quote(symbol)
					Views.stock_lookup(quote)
					self.main_menu()
			else:
				Views.invalid()
				self.main_menu()

	def profile_manager(self):
		while(True):
			choice = Views.profile_manager(self.user)
			if choice == "1":
				new_username = Views.user_prompt("What would you like to change your username too?: ")
				self.user.change_username(self.user.username, new_username)
				user = DB_API.fetch_user(self.username)
				self.user = User(self.username, user[0][2], user[0][3], user[0][4])
			elif choice == "2":
				new_password = Views.user_prompt("What would you like to change your password too?: ")
				self.user.change_password(self.user.username, new_password)
				user = DB_API.fetch_user(self.username)
				self.user = User(self.username, user[0][2], user[0][3], user[0][4])
			elif choice == "3":
				new_first_name = Views.user_prompt("What would you like to change your first name too?: ")
				self.user.change_first_name(self.user.username, new_first_name)
				user = DB_API.fetch_user(self.username)
				self.user = User(self.username, user[0][2], user[0][3], user[0][4])
			elif choice == "4":
				new_last_name = Views.user_prompt("What would you like to change your last name too?: ")
				self.user.change_last_name(self.user.username, new_last_name)
				user = DB_API.fetch_user(self.username)
				self.user = User(self.username, user[0][2], user[0][3], user[0][4])
			elif choice == "5":
				self.main_menu()

c = Controller()
c.sign_in()