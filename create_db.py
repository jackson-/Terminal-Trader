import sqlite3

def create_users_table():
	conn = sqlite3.connect('trader.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `users`;''')
	c.execute("""CREATE TABLE `users` (
			`id` INTEGER,
			`username` VARCHAR,
			`password` VARCHAR,
			`first_name` TEXT,
			`last_name` TEXT,
			PRIMARY KEY (`id`)
			)""")
	conn.commit()
	conn.close()


def create_accounts_table():
	conn = sqlite3.connect('trader.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `accounts`;''')
	c.execute("""CREATE TABLE `accounts` (
			`id` INTEGER,
			`username` VARCHAR,
			`balance` INT,
			`account_name` VARCHAR,
			`account_number` INT,
			PRIMARY KEY (`id`),
			FOREIGN KEY (username) REFERENCES users(username)
			)""")
	conn.commit()
	conn.close()


def create_portfolios_table():
	conn = sqlite3.connect('trader.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `portfolios`;''')
	c.execute("""CREATE TABLE `portfolios` (
			`id` INTEGER,
			`username` VARCHAR,
			`account_name` VARCHAR,
			`portfolio_name` VARCHAR,
			PRIMARY KEY (`id`),
			FOREIGN KEY (username) REFERENCES users(username),
			FOREIGN KEY (account_name) REFERENCES accounts(account_name)
			)""")
	conn.commit()
	conn.close()


def create_stocks_table():
	conn = sqlite3.connect('trader.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `stocks`;''')
	c.execute("""CREATE TABLE `stocks` (
			`id` INTEGER,
			`portfolio_id` INTEGER,
			`ticker` VARCHAR,
			`company_name` TEXT,
			`buy_price` INT,
			`amount` INT,
			`timestamp` VARCHAR,
			FOREIGN KEY (portfolio_id) REFERENCES portfolios(id),
			PRIMARY KEY (`id`)
			)""")
	conn.commit()
	conn.close()

create_portfolios_table()
create_stocks_table()
create_users_table()
create_accounts_table()