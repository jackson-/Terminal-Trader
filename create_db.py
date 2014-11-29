import sqlite3

def create_users_table():
	conn = sqlite3.connect('trader.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `users`;''')
	c.execute("""CREATE TABLE `users` (
			`id` INTEGER,
			`username` VARCHAR,
			`password` VARCHAR,
			PRIMARY KEY (`id`)
			)""")
	conn.commit()
	conn.close()


def create_portfolio_accounts_table():
	conn = sqlite3.connect('trader.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `portfolio_accounts`;''')
	c.execute("""CREATE TABLE `portfolio_accounts` (
			`id` INTEGER,
			`user_id` INTEGER,
			`balance` INT,
			`account_name` VARCHAR,
			PRIMARY KEY (`id`),
			FOREIGN KEY (user_id) REFERENCES users(id)
			)""")
	conn.commit()
	conn.close()


def create_portfolios_table():
	conn = sqlite3.connect('trader.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `portfolios`;''')
	c.execute("""CREATE TABLE `portfolios` (
			`id` INTEGER,
			`user_id` INTEGER,
			`account_id` INTEGER,
			`portfolio_name` VARCHAR,
			PRIMARY KEY (`id`),
			FOREIGN KEY (user_id) REFERENCES users(id),
			FOREIGN KEY (account_id) REFERENCES accounts(id)
			)""")
	conn.commit()
	conn.close()


def create_purchases_table():
	conn = sqlite3.connect('trader.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `purchases`;''')
	c.execute("""CREATE TABLE `purchases` (
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
create_purchases_table()
create_users_table()
create_portfolio_accounts_table()