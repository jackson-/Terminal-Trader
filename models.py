import sqlite3
from random import randint


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
	def __init__(self, balance, user_username, user_password, account_name):
		self.balance = balance
		# self.user = DB_API.fetch_user_id(user_username, user_password)
		self.account_name = account_name
		self.account_number = randint(11111111, 99999999)
		self.user_username = user_username
		self.user_password = user_password

	@staticmethod
	def delete_self(user_username, user_password):
		DB_API.delete_account(self.account_name, user_username, user_password)

	def deposit(self, amount):
		self.balance = self.balance + amount

	def withdraw(self, amount):
		self.balance = self.balance - amount