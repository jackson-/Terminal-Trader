from models import User, Account, Purchase, DB_API, markit
from bank_models import BANK_DB_API
from views import Views
from bank_views import Views as BViews
from random import randint
import re

class Controller(object):

	def sign_in(self):
		username = Views.sign_in()
		self.user = DB_API.fetch_user(username)
		self.bank_user = BANK_DB_API.fetch_user(self.user.id)
		if self.user is None:
			self.user_register()
		else:
			self.user_verify()

	def user_register(self):
		registration = Views.user_register()
		DB_API.create_user(registration[0], registration[1])
		BANK_DB_API.create_user(registration[0], registration[1], 'client')
		self.user = DB_API.fetch_user(registration[0])
		self.bank_user = DB_API.fetch_user(self.user.id)
		self.main_menu()

	def user_verify(self):
		pass_or_not = Views.user_verify(self.user)
		choices = {'pass':self.main_menu, None:self.sign_in}
		choices[pass_or_not]()

	def main_menu(self):
		choice = Views.main_menu()
		choices = {'1':self.bank_account_menu, '2':self.accounts_main_menu, '3':self.sign_in}
		choices[choice]()

	def accounts_main_menu(self):
		choice = Views.accounts_main_menu()
		choices = {'1':self.account_manager, '2':self.account_register, '3':self.account_deleter, '4':self.main_menu}
		choices[choice]()

	def bank_account_menu(self):
		choice = BViews.main_menu()
		choices = {'1':self.bank_account_list, '2':self.bank_account_register, '3':self.bank_account_deleter}
		choices[choice]()

	def bank_account_deleter(self):
		accounts = BANK_DB_API.fetch_accounts(self.user.id)
		if accounts is None:
			Views.invalid()
			self.accounts_main_menu()
		else:
			account = BViews.account_chooser(accounts)
			self.bank_user.delete_account(account.account_name)
			self.bank_account_menu()

	def bank_account_list(self):
		accounts = BANK_DB_API.fetch_accounts(self.user.id)
		if accounts is None:
			self.bank_account_register()
		else:
			account = BViews.account_chooser(accounts)
			choice = Views.bank_account_menu(account)
			choices = {'1':self.bank_deposit, '2':self.bank_transfer, '3':self.main_menu}
			if choice == '3':
				choices[choice]()
			else:	
				choices[choice](account)

	def bank_deposit(self, account):
		amount = Views.bank_deposit(account)
		account.deposit(amount)
		self.main_menu()

	def bank_transfer(self, bank_account):
		port_accounts = DB_API.fetch_accounts(self.user.id)
		if port_accounts is None:
			self.account_register()
		else:
			port_account = Views.accounts_list(port_accounts)
			amount = Views.bank_transfer(port_account, bank_account)
			port_account.deposit(amount)
			bank_account.withdraw(amount)
			self.main_menu()


	def bank_account_register(self):
		registration = Views.bank_account_register()
		account_number = randint(11111111, 99999999)
		BANK_DB_API.create_account(self.user.id, registration[0], registration[1], account_number)
		self.bank_account_menu()

	def account_manager(self):
		accounts = DB_API.fetch_accounts(self.user.id)
		if accounts is None:
			self.account_register()
		else:
			account = Views.accounts_list(accounts)
			choice = Views.account_manager(account)
			choices = {'1':self.deposit_earnings, '2':self.bank_withdraw, '3':self.bank_account_change, '4':self.stock_lookup, '5':self.sell_stock, '6':self.check_inventory, '7':self.accounts_main_menu}
			if choice == '7':
				choices[choice]()
			else:
				choices[choice](account)

	def bank_account_change(self, account):
		pass

	def deposit_earnings(self, account):
		bank_account = BANK_DB_API.fetch_account_by_name(self.user.id, account.bank_account_name)
		amount = Views.deposit_to_bank(bank_account, account)
		bank_account.deposit(amount)
		account.withdraw(amount)
		self.accounts_main_menu()

	def bank_withdraw(self, account):
		bank_account = BANK_DB_API.fetch_account_by_name(self.user.id, account.bank_account_name)
		amount = Views.bank_transfer(account, bank_account)
		account.deposit(amount)
		bank_account.withdraw(amount)
		self.accounts_main_menu()


	def account_register(self):
		account_name = Views.account_register()
		bank_accounts = BANK_DB_API.fetch_accounts(self.user.id)
		if bank_accounts is None:
			self.bank_account_register()
		else:
			bank_account = BViews.account_chooser(bank_accounts)
			self.user.create_account(account_name, 0, bank_account.account_name)
			self.accounts_main_menu()

	def account_deleter(self):
		accounts = DB_API.fetch_accounts(self.user.id)
		if accounts is None:
			Views.invalid()
			self.accounts_main_menu()
		else:
			account = Views.accounts_list(accounts)
			self.user.delete_account(account.account_name)
			self.accounts_main_menu()

	def stock_lookup(self, account):
		lookup = Views.stock_lookup()
		choices = {'name':self.name_stock, 'ticker':self.ticker_stock}
		choices[lookup[0]](lookup[1], account)

	def name_stock(self, search, account):
		result = markit.company_search(search)
		ticker = Views.name_result(result)
		self.ticker_stock(ticker, account)

	def ticker_stock(self, search, account):
		quote = markit.get_quote(search)
		choice = Views.ticker_result(quote, account)
		choices = {'y': self.buy_stock, 'n':self.accounts_main_menu}
		if choice[0] == 'y':
			choices[choice[0]](quote, account, choice[1])
		else:
			choices[choice[0]]()

	
	def buy_stock(self, quote, account, amount):
		account.buy_stock(quote['Symbol'], amount)
		self.account_manager()

	def sell_stock(self, account):
		while(True):
			purchases = account.check_inventory()
			if purchases is None:
				Views.invalid()
				self.account_manager()
			else:
				sell_info = Views.sell_stock(purchases)
				purchase = purchases[sell_info[0]]
				amount = sell_info[1]
				account.sell_stock(purchase, amount)
				self.account_manager()

	def check_inventory(self, account):
		while(True):
			purchases = account.check_inventory()
			if purchases is None:
				Views.invalid()
				self.account_manager()
			else:
				Views.check_inventory(purchases)
				self.account_manager()

c = Controller()
c.sign_in()

## functions for every if statement, if you must use if else
## return objects from DB_API functions when neccesarry
## get rid of if else menus with dictionary objects