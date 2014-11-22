import sqlite3
from random import randint
import markit_wrapper

# default values
default_db = "trader.db"
markit = markit_wrapper.Markit()

class User(object):

	def __init__(self, username, password, first_name, last_name):
		self.username = username
		self.password = password
		self.first_name = first_name
		self.last_name = last_name

	def create_account(self, account_name, init_balance):
		pass

	def delete_account(self, account_name):
		Account.delete_self(self.username, self.user_password)

	def buy_stock(ticker, amount):
		pass

	def sell_stock(ticker, amount):
		pass


class Account(object):
	def __init__(self, balance, username, account_name):
		self.balance = balance
		self.user_id = DB_API.fetch_user_id(username)
		self.account_name = account_name
		self.account_number = randint(11111111, 99999999)
		self.user_username = user_username
		self.user_password = user_password

	@staticmethod
	def delete_self(self):
		DB_API.delete_account(self.account_name, self.user_id)

	def deposit(self, amount):
		self.balance = self.balance + amount

	def withdraw(self, amount):
		self.balance = self.balance - amount


class Portfolio(object):

	def __init__(self, username, portfolio_name, account_name):
		self.user_id = DB_API.fetch_user_id(username)
		self.portfolio_name = portfolio_name
		self.account = DB.fetch_account(self.user_id, account_name)

	def add_stock(self, ticker, amount):
		pass

	def delete_stock(self, ticker, amount):
		pass


class Stock(object):

	def __init__(self, ticker, company_name, buy_price, portfolio_id):
		self.ticker = ticker
		self.company_name = company_name
		self.buy_price = buy_price
		self.portfolio_id = portfolio_id


class DB_API:

	@staticmethod
	def delete_account(account_name, user_id):
		pass

	@staticmethod
	def fetch_user_id(username):
		pass

	@staticmethod
	def fetch_account(user_id, account_name):
		pass
