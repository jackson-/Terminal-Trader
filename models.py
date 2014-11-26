import sqlite3
from random import randint
import markit_wrapper

# default values
db = "trader.db"
markit = markit_wrapper.Markit()

class User(object):

	def __init__(self, user_id, username, password, first_name, last_name):
		self.id = user_id
		self.username = username
		self.password = password
		self.first_name = first_name
		self.last_name = last_name

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


class Account(object):
	def __init__(self, account_id, username, balance, account_name, account_number):
		self.id = account_id
		self.balance = balance
		self.username = username
		self.account_name = account_name
		self.account_number = account_number

	def delete_self(self):
		DB_API.delete_account(self.account_name, self.username)

	def deposit(self, amount):
		self.balance = int(self.balance) + int(amount)
		DB_API.deposit(self.account_name, self.username, self.balance)

	def withdraw(self, amount):
		self.balance = int(self.balance) - int(amount)
		DB_API.deposit(self.account_name, self.username, self.balance)

class Portfolio(object):

	def __init__(self, portfolio_id, username, portfolio_name, account_name):
		self.id = portfolio_id
		self.username = username
		self.portfolio_name = portfolio_name
		self.account_name = account_name

	def change_account(self, account_id, username, portfolio_id):
		DB_API.change_portfolio_account(account_id, username, portfolio_id)

	def buy_stock(self, ticker, amount):
		quote = markit.get_quote(ticker)
		if quote == None:
			return None
		buy_price = int(quote['LastPrice'])
		company_name = quote['Name']
		deductable = buy_price * int(amount)
		account = DB_API.fetch_account_by_name(self.account_name, self.username)
		account_balance = account[0][2]
		print(account_balance)
		new_balance = account_balance - deductable
		if new_balance < 0:
			print('went false')
			return False
		else:
			print('went thru')
			DB_API.withdraw(self.account_name, self.username, new_balance)
			DB_API.add_stock(self.id, ticker, company_name, buy_price, amount)

	def sell_stock(self, ticker, buy_price, amount):
		stock = DB_API.fetch_stock(self.id, ticker, buy_price)
		print(stock)


class Stock(object):

	def __init__(self, stock_id, ticker, company_name, buy_price, portfolio_id):
		self.id = stock_id
		self.ticker = ticker
		self.company_name = company_name
		self.buy_price = buy_price
		self.portfolio_id = portfolio_id


class DB_API:

	@staticmethod
	def create_user(username, password, first_name, last_name):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO users(username, password, first_name, last_name) VALUES (?, ?, ?, ?)"
		c.execute(statement, (username, password, first_name, last_name,))
		conn.commit()
		conn.close()

	@staticmethod
	def create_account(account_name, account_number, balance, username):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO accounts(account_name, account_number, balance, username) VALUES (?, ?, ?, ?)"
		c.execute(statement, (account_name, account_number, balance, username,))
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
	def add_stock(portfolio_id, ticker, company_name, buy_price, amount):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO stocks(portfolio_id, ticker, company_name, buy_price, amount) VALUES (?, ?, ?, ?, ?)"
		c.execute(statement, (portfolio_id, ticker, company_name, buy_price, amount,))
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
			return user
		conn.close()

	@staticmethod
	def fetch_accounts(username):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM accounts WHERE username = (?)"
		c.execute(statement, (username,))
		account_list = c.fetchall()
		if len(account_list) == 0:
			return None
		else:
			return account_list
		conn.close()

	@staticmethod
	def fetch_account_by_name(account_name, username):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM accounts WHERE account_name = (?) AND username = (?)"
		c.execute(statement, (account_name, username,))
		account = c.fetchall()
		if len(account) == 0:
			return None
		else: 
			return account
		conn.close()

	@staticmethod
	def fetch_account_by_portfolio(portfolio_name, username):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT account_name FROM portfolios WHERE portfolio_name = (?) AND username = (?)"
		c.execute(statement, (portfolio_name, username,))
		account = c.fetchall()
		if len(account) == 0:
			return None
		else: 
			return account
		conn.close()

	@staticmethod
	def fetch_portfolios(username):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM portfolios WHERE username = (?)"
		c.execute(statement, (username,))
		portfolio_list = c.fetchall()
		if len(portfolio_list) == 0:
			return None
		else:
			return portfolio_list
		conn.close()

	@staticmethod
	def fetch_portfolio_by_name(username, portfolio_name):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM portfolios WHERE username = (?) AND portfolio_name = (?)"
		c.execute(statement, (username, portfolio_name,))
		portfolio = c.fetchall()
		if len(portfolio) == 0:
			return None
		else:
			return portfolio
		conn.close()

	@staticmethod
	def fetch_portfolio_inventory(username, portfolio_name):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT id FROM portfolios WHERE portfolio_name = (?) AND username = (?)"
		c.execute(statement, (portfolio_name, username,))
		portfolio_id = c.fetchone()
		statement = "SELECT * FROM stocks WHERE portfolio_id = (?)"
		c.execute(statement, (portfolio_id[0],))
		stocks = c.fetchall()
		if len(stocks) == 0:
			return None
		else:
			return stocks
		conn.close()

	@staticmethod
	def fetch_stock(portfolio_id, ticker, buy_price):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM stocks WHERE portfolio_id = (?), ticker = (?), buy_price = (?)"
		c.execute(statement, (portfolio_id, ticker, buy_price,))
		stocks = c.fetchall()
		if len(stocks) == 0:
			return None
		else:
			return stocks
		conn.close()

	@staticmethod
	def deposit(account_name, username, new_balance):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "UPDATE accounts SET balance = (?) WHERE username = (?) AND account_name = (?)"
		c.execute(statement, (new_balance, username, account_name,))
		conn.commit()
		conn.close()

	@staticmethod
	def withdraw(account_name, username, new_balance):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "UPDATE accounts SET balance = (?) WHERE username = (?) AND account_name = (?)"
		c.execute(statement, (new_balance, username, account_name,))
		conn.commit()
		conn.close()

	@staticmethod
	def delete_account(account_name, username):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "DELETE FROM accounts WHERE account_name = (?) AND username = (?)"
		c.execute(statement, (account_name, username,))
		conn.commit()
		conn.close()

	@staticmethod
	def change_username(old_username, new_username):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "UPDATE users SET username = (?) WHERE username = (?)"
		c.execute(statement, (new_username, old_username,))
		statement = "UPDATE portfolios SET username = (?) WHERE username = (?)"
		c.execute(statement, (new_username, old_username,))
		statement = "UPDATE accounts SET username = (?) WHERE username = (?)"
		c.execute(statement, (new_username, old_username,))
		conn.commit()
		conn.close()

	@staticmethod
	def change_password(username, new_password):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "UPDATE users SET password = (?) WHERE username = (?)"
		c.execute(statement, (new_password, username,))
		conn.commit()
		conn.close()

	@staticmethod
	def change_first_name(username, new_first_name):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "UPDATE users SET first_name = (?) WHERE username = (?)"
		c.execute(statement, (new_first_name, username,))
		conn.commit()
		conn.close()

	@staticmethod
	def change_last_name(username, new_last_name):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "UPDATE users SET last_name = (?) WHERE username = (?)"
		c.execute(statement, (new_last_name, username,))
		conn.commit()
		conn.close()

	@staticmethod
	def change_portfolio_account(account_id, username, portfolio_id):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "UPDATE portfolios SET account_id = (?) WHERE username = (?) AND portfolio_id = (?)"
		c.execute(statement, (account_id, username, portfolio_id,))
		conn.commit()
		conn.close()