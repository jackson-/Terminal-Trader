import sqlite3
from random import randint
import markit_wrapper
from datetime import datetime

# default values
db = "trader.db"
markit = markit_wrapper.Markit()

class User(object):

	def __init__(self, user_id, username, password):
		self.id = user_id
		self.username = username
		self.password = password

	def create_account(self, account_name, init_balance, bank_account_name):
		DB_API.create_account(account_name, init_balance, self.id, bank_account_name)

	def delete_account(self, account_name):
		DB_API.delete_account(account_name, self.id)


class Account(object):
	def __init__(self, account_id, user_id, balance, account_name, bank_account_name):
		self.id = account_id
		self.balance = balance
		self.user_id = user_id
		self.account_name = account_name
		self.bank_account_name = bank_account_name

	def deposit(self, amount):
		self.balance = int(self.balance) + int(amount)
		DB_API.deposit(self.account_name, self.user_id, self.balance)

	def withdraw(self, amount):
		self.balance = int(self.balance) - int(amount)
		DB_API.withdraw(self.account_name, self.user_id, self.balance)

	def check_inventory(self):
		purchases = DB_API.fetch_inventory(self.id)
		return purchases

	def buy_stock(self, ticker, amount):
		timestamp = datetime.now()
		quote = markit.get_quote(ticker)
		buy_price = float(quote['LastPrice'])
		company_name = quote['Name']
		deductable = buy_price * float(amount)
		new_balance = self.balance - deductable
		DB_API.withdraw(self.account_name, self.user_id, new_balance)
		DB_API.add_stock(self.id, ticker, company_name, buy_price, amount, timestamp)

	def sell_stock(self, purchase, amount):
		new_amount = purchase.amount - int(amount)
		if new_amount == 0:
			DB_API.delete_stock(purchase.id)
			quote = markit.get_quote(purchase.ticker)
			sell_price = float(quote['LastPrice'])
			addition = sell_price * int(amount)
			self.deposit(addition)
		elif new_amount < 0:
			return False
		else:
			DB_API.update_stock(purchase.id, new_amount)
			quote = markit.get_quote(purchase.ticker)
			sell_price = float(quote['LastPrice'])
			addition = sell_price * int(amount)
			self.deposit(addition)

	def change_account(self, account_id, username, portfolio_id):
		DB_API.change_portfolio_account(account_id, username, portfolio_id)

class Purchase(object):

	def __init__(self, stock_id, portfolio_id, ticker, company_name, buy_price, amount, timestamp):
		self.id = stock_id
		self.ticker = ticker
		self.company_name = company_name
		self.buy_price = buy_price
		self.portfolio_id = portfolio_id
		self.amount = amount
		self.timestamp = timestamp

class DB_API:

	@staticmethod
	def create_user(username, password):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO users(username, password) VALUES (?, ?)"
		c.execute(statement, (username, password,))
		conn.commit()
		conn.close()

	@staticmethod
	def create_account(account_name, balance, user_id, bank_account_name):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO portfolio_accounts(account_name, balance, user_id, bank_account_name) VALUES (?, ?, ?, ?)"
		c.execute(statement, (account_name, balance, user_id, bank_account_name,))
		conn.commit()
		conn.close()

	@staticmethod
	def create_portfolio(username, account_name, portfolio_name):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO portfolios(username, account_name, portfolio_name) VALUES (?, ?, ?)"
		c.execute(statement, (username, account_name, portfolio_name,))
		conn.commit()
		conn.close()

	@staticmethod
	def add_stock(portfolio_id, ticker, company_name, buy_price, amount, timestamp):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO purchases(portfolio_id, ticker, company_name, buy_price, amount, timestamp) VALUES (?, ?, ?, ?, ?, ?)"
		c.execute(statement, (portfolio_id, ticker, company_name, buy_price, amount, timestamp,))
		conn.commit()
		conn.close()

	@staticmethod
	def delete_stock(purchase_id):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "DELETE FROM purchases WHERE id = (?)"
		c.execute(statement, (purchase_id,))
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
			user = User(user[0][0], user[0][1], user[0][2], )
			return user
		conn.close()

	@staticmethod
	def fetch_accounts(user_id):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM portfolio_accounts WHERE user_id = (?)"
		c.execute(statement, (user_id,))
		accounts = c.fetchall()
		account_list = []
		if len(accounts) == 0:
			return None
		else:
			for account in accounts:
				account_list.append(Account(account[0], account[1], account[2], account[3], account[4]))
			return account_list
		conn.close()

	@staticmethod
	def fetch_portfolios(user_id):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM portfolios WHERE user_id = (?)"
		c.execute(statement, (user_id,))
		portfolios = c.fetchall()
		portfolio_list = []
		if len(portfolios) == 0:
			return None
		else:
			for portfolio in portfolio_list:
				portfolio_list.append(Portfolio(portfolio[0], portfolio[1], portfolio[2], portfolio[3]))
			return portfolio_list
		conn.close()

	@staticmethod
	def fetch_inventory(portfolio_id):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM purchases WHERE portfolio_id = (?)"
		c.execute(statement, (portfolio_id,))
		purchases = c.fetchall()
		purchase_list = []
		if len(purchases) == 0:
			return None
		else:
			for purchase in purchases:
				purchase_list.append(Purchase(purchase[0], purchase[1], purchase[2], purchase[3], purchase[4], purchase[5], purchase[6]))
			return purchase_list
		conn.close()

	@staticmethod
	def fetch_stock(portfolio_id, ticker, buy_price, timestamp):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM purchases WHERE portfolio_id = (?) AND ticker = (?) AND buy_price = (?) AND timestamp = (?)"
		c.execute(statement, (portfolio_id, ticker, buy_price, timestamp,))
		purchases = c.fetchall()
		if len(purchases) == 0:
			return None
		else:
			return purchases
		conn.close()

	@staticmethod
	def deposit(account_name, user_id, new_balance):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "UPDATE portfolio_accounts SET balance = (?) WHERE user_id = (?) AND account_name = (?)"
		c.execute(statement, (new_balance, user_id, account_name,))
		conn.commit()
		conn.close()

	@staticmethod
	def withdraw(account_name, user_id, new_balance):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "UPDATE portfolio_accounts SET balance = (?) WHERE user_id = (?) AND account_name = (?)"
		c.execute(statement, (new_balance, user_id, account_name,))
		conn.commit()
		conn.close()

	@staticmethod
	def delete_account(account_name, user_id):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "DELETE FROM portfolio_accounts WHERE account_name = (?) AND user_id = (?)"
		c.execute(statement, (account_name, user_id,))
		conn.commit()
		conn.close()

	@staticmethod
	def update_stock(purchase_id, new_amount):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "UPDATE purchases SET amount = (?) WHERE id = (?)"
		c.execute(statement, (new_amount, purchase_id,))
		conn.commit()
		conn.close()


## refactor DB_API to return objects and reduce function count
## decouple bank and stock trading modules/ different DB's/ different files/ independent
## client and banker software
## user can link money bank account to trading account/ both are seperate
## write interface class