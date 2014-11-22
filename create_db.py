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
			`user_id` INTEGER,
			`balance` INT,
			`account_name` TEXT,
			`account_number` INT,
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
			`portfolio_name` TEXT,
			PRIMARY KEY (`id`),
			FOREIGN KEY (user_id) REFERENCES users(id),
			FOREIGN KEY (account_id) REFERENCES accounts(id)
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
			FOREIGN KEY (portfolio_id) REFERENCES portfolioss(id),
			PRIMARY KEY (`id`)
			)""")
	conn.commit()
	conn.close()

create_portfolios_table()
create_stocks_table()
create_users_table()
create_accounts_table()