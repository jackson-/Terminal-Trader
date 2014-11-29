import sqlite3
from random import randint
from datetime import datetime

## default values
db = 'bank.db'

class BankAccount(object):
	def __init__(self, account_id, user_id, account_name, init_balance):
		self.account_id = account_id
		self.user_id = user_id
		self.account_name = account_name
		self.balance = init_balance

	def deposit(self, amount):
		self.balance = self.balance + amount

	def withdraw(self, amount):
		self.balance = self.balance - amount


class User(object):
	def __init__(self, user_id, username, password, permission_level):
		self.id = user_id
		self.username = username
		self.password = password
		self.permission_level = permission_level


class Client(User):


	def create_account(self, account_name, init_balance):
		account_number = randint(11111111, 99999999)
		DB_API.create_account(account_name, account_number, init_balance, self.username)

	def delete_account(self, account_name):
		Account.delete_self(self.username, self.user_password)

	def create_portfolio(self, username, account_name, portfolio_name):
		DB_API.create_portfolio( self.username, account_name, portfolio_name)

	def change_username(self, old_username, new_username):
		DB_API.change_username(self.username, new_username)

	def change_password(self, username, new_password):
		DB_API.change_password(self.username, new_password)

	def change_first_name(self, username, new_first_name):
		DB_API.change_first_name(self.username, new_first_name)

	def change_last_name(self, username, new_last_name):
		DB_API.change_last_name(self.username, new_last_name)


class Banker(User):
	def __init__(self, permission_level):
		pass


class DB_API:

	@staticmethod
	def create_user(username, password, permission_level):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO users(username, password, permission_level) VALUES (?, ?, ?)"
		c.execute(statement, (username, password, permission_level,))
		conn.commit()
		conn.close()

	@staticmethod
	def create_account(user_id, account_name, balance):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO bank_accounts(user_id, account_name, balance) VALUES (?, ?, ?)"
		c.execute(statement, (user_id, account_name, balance,))
		conn.commit()
		conn.close()
	
	@staticmethod
	def fetch_user(username):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM users WHERE username = ?"
		c.execute(statement, (username,))
		user = c.fetchall()
		if len(user) == 0:
			return None
		else:
			return User(user[0][0], user[0][1], user[0][2], user[0][3])
		conn.close()

	@staticmethod
	def fetch_accounts(user_id):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM bank_accounts WHERE user_id = ?"
		c.execute(statement, (user_id,))
		accounts = c.fetchall()
		account_list = []
		if len(accounts) == 0:
			return None
		else:
			for account in accounts:
				account_list.append(BankAccount(account[0], account[1], account[2], account[3]))
			return account_list
		conn.close()