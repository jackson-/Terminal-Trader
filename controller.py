from models import User, Portfolio, Account, Purchase, DB_API, markit
from views import Views
import re

class Controller(object):

	def sign_in(self):
		username = Views.sign_in()
		self.user = DB_API.fetch_user(username)
		if self.user is None:
			self.user_register()
		else:
			self.user_verify()

	def user_register(self):
		registration = Views.user_register()
		DB_API.create_user(registration[0], registration[1])
		self.user = DB_API.fetch_user(registration[0])
		self.main_menu()

	def user_verify(self):
		pass_or_not = Views.user_verify(self.user)
		choices = {'pass':self.main_menu, None:self.sign_in}
		choices[pass_or_not]()

	def main_menu(self):
		choice = Views.main_menu()
		choices = {'1':self.accounts_main_menu, '2':self.portfolios_main_menu, '3':self.stock_lookup, '4':self.sign_in}
		choices[choice]()

	def accounts_main_menu(self):
		choice = Views.accounts_main_menu()
		choices = {'1':self.account_manager, '2':self.account_register, '3':self.account_deleter, '4':self.main_menu}
		choices[choice]()

	def account_manager(self):
		accounts = DB_API.fetch_accounts(self.user.id)
		account = Views.accounts_list(accounts)

	def portfolios_main_menu(self):
		choice = Views.portfolios_main_menu()
		choices = {'1':}

	def stock_lookup(self):
		lookup = Views.stock_lookup()
	

c = Controller()
c.sign_in()

## functions for every if statement, if you must use if else
## return objects from DB_API functions when neccesarry
## get rid of if else menus with dictionary objects