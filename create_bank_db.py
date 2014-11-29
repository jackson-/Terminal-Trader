import sqlite3

def create_users_table():
	conn = sqlite3.connect('bank.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `users`;''')
	c.execute("""CREATE TABLE `users` (
			`id` INTEGER,
			`username` VARCHAR,
			`password` VARCHAR,
			`permission_level` TEXT, 
			PRIMARY KEY (`id`)
			)""")
	conn.commit()
	conn.close()

def create_bank_accounts_table():
	conn = sqlite3.connect('bank.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `bank_accounts`;''')
	c.execute("""CREATE TABLE `bank_accounts` (
			`id` INTEGER,
			`user_id` INTEGER,
			`account_name` INT,
			`balance` INT,
			`account_number` INT,
			FOREIGN KEY (user_id) REFERENCES users(id),
			PRIMARY KEY (`id`)
			)""")
	conn.commit()
	conn.close()

create_users_table()
create_bank_accounts_table()