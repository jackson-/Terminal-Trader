import sqlite3
from random import randint
from datetime import datetime

## default values
db = 'bank.db'

class BankAccount(object):
	def __init__(self, account_id, user_id, account_name, init_balance, account_number):
		self.id = account_id
		self.user_id = user_id
		self.account_name = account_name
		self.balance = init_balance
		self.account_number = account_number

	def deposit(self, amount):
		self.balance = self.balance + int(amount)
		BANK_DB_API.deposit(self.id, self.balance)

	def withdraw(self, amount):
		self.balance = self.balance - int(amount)
		BANK_DB_API.withdraw(self.id, self.balance)

	def transfer(self, src_acct_id, dest_acct_id, amount, dest_balance):
		self.balance = self.balance - amount
		BANK_DB_API.transfer(src_acct_id, dest_acct_id, self.balance, dest_balance)

class User(object):
	def __init__(self, user_id, username, password, permission_level):
		self.id = user_id
		self.username = username
		self.password = password
		self.permission_level = permission_level

	def delete_account(self, account_name):
		BANK_DB_API.delete_account(self.id, account_name)

class Client(User):

	def create_account(self, account_name, init_balance):
		account_number = randint(11111111, 99999999)
		BANK_DB_API.create_account(self.id, account_name, init_balance, account_number)

class Banker(User):
	
	def delete_all_accounts(self):
		BANK_DB_API.delete_all_accounts()

class BANK_DB_API:

	@staticmethod
	def create_user(username, password, permission_level):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO users(username, password, permission_level) VALUES (?, ?, ?)"
		c.execute(statement, (username, password, permission_level,))
		conn.commit()
		conn.close()

	@staticmethod
	def create_account(user_id, account_name, balance, account_number):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO bank_accounts(user_id, account_name, balance, account_number) VALUES (?, ?, ?, ?)"
		c.execute(statement, (user_id, account_name, balance, account_number,))
		conn.commit()
		conn.close()

	@staticmethod
	def delete_account(user_id, account_name):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "DELETE FROM bank_accounts WHERE user_id = (?) AND account_name = (?)"
		c.execute(statement, (user_id, account_name,))
		conn.commit()
		conn.close()

	@staticmethod
	def delete_all_accounts():
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "DELETE FROM bank_accounts"
		c.execute(statement)
		conn.commit()
		conn.close()
	
	@staticmethod
	def fetch_user(user_id):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM users WHERE id = ?"
		c.execute(statement, (user_id,))
		user = c.fetchall()
		if len(user) == 0:
			return None
		else:
			if user[0][3] == 'banker':
				return Banker(user[0][0], user[0][1], user[0][2], user[0][3])
			else:
				return Client(user[0][0], user[0][1], user[0][2], user[0][3])
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
				account_list.append(BankAccount(account[0], account[1], account[2], account[3], account[4]))
			return account_list
		conn.close()

	@staticmethod
	def fetch_account_by_name(user_id, account_name):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM bank_accounts WHERE user_id = (?) AND account_name = (?)"
		c.execute(statement, (user_id, account_name,))
		accounts = c.fetchall()
		account_list = []
		if len(accounts) == 0:
			return None
		else:
			for account in accounts:
				account_list.append(BankAccount(account[0], account[1], account[2], account[3], account[4]))
			return account_list[0]
		conn.close()

	@staticmethod
	def fetch_all_accounts():
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM bank_accounts"
		c.execute(statement)
		accounts = c.fetchall()
		account_list = []
		if len(accounts) == 0:
			return None
		else:
			for account in accounts:
				account_list.append(BankAccount(account[0], account[1], account[2], account[3]))
			return account_list
		conn.close()

	@staticmethod
	def deposit(account_id, balance):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "UPDATE bank_accounts SET balance = (?) WHERE id = (?)"
		c.execute(statement, (balance, account_id,))
		conn.commit()
		conn.close()

	@staticmethod
	def withdraw(account_id, balance):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "UPDATE bank_accounts SET balance = (?) WHERE id = (?)"
		c.execute(statement, (balance, account_id,))
		conn.commit()
		conn.close()

	@staticmethod
	def transfer(src_account_id, dest_account_id, src_balance, dest_balance):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "UPDATE bank_accounts SET balance = (?) WHERE id = (?)"
		c.execute(statement, (src_balance, src_account_id,))
		statement = "UPDATE bank_accounts SET balance = (?) WHERE id = (?)"
		c.execute(statement, (dest_balance, dest_account_id,))
		conn.commit()
		conn.close()
