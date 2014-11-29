from bank_models import BankAccount, User, Client, Banker, DB_API
from bank_views import Views

class Controller:

	def sign_in(self):
		while(True):
			username = Views.sign_in()
			self.user = DB_API.fetch_user(username)
			# if the user doesn't exist then register them. if they do verify their password
			if self.user == None:
				self.user_register()
			else:
				self.user_verify()

	def user_register(self):
		while(True):
			## this gathers the user info
			username = Views.user_register()
			password = Views.password_prompt()
			permission_level = Views.permission_prompt()
			## i create an object of choices here
			choices = {'banker': DB_API.create_user, 'client': DB_API.create_user, None : self.sign_in}
			# id the persons choice is not in the object above keys then we throw an error. If it is fire of the function inside
			if permission_level is None:
				choices[permission_level]
			else:
				choices[permission_level](username, password, permission_level)
				self.user = DB_API.fetch_user(username)
				self.main_menu()

	def user_verify(self):
		while(True):
			# if verification check returns pass send to main menu. if not throw error
			check = Views.verify_password(self.user)
			choices = {'pass' : self.main_menu, None : self.sign_in}
			choices[check]()

	def main_menu(self):
		while(True):
			choice = Views.main_menu()
			choices = {'1' : self.account_list, '2' : self.account_register, '3' : self.account_delete, '4' : self.sign_in}
			if choice in choices.keys():
				choices[choice]()
			else:
				Views.invalid()

	def account_list(self):
		while(True):
			if self.user.permission_level == 'banker':
				accounts = DB_API.fetch_all_accounts()
			else:
				accounts = DB_API.fetch_accounts(self.user.id)
			if accounts is None:
				self.account_register()
			else:
				account = Views.account_chooser(accounts)
				self.account_manager(account)

	def account_register(self):
		while(True):
			account = Views.account_register()
			DB_API.create_account(self.user.id, account[0], account[1])
			self.main_menu()

	def account_manager(self, account):
		while(True):
			choice = Views.account_manager(account)
			choices = {'1': self.account_deposit, '2' : self.account_withdraw, '3': self.account_transfer, '4' : self.main_menu}
			if choice == '4':
				choices[choice]()
			else:	
				choices[choice](account)

	def account_deposit(self, account):
		while(True):
			amount = Views.account_deposit(account)
			account.deposit(amount)
			self.account_manager(account)

	def account_withdraw(self, account):
		while(True):
			amount = Views.account_withdraw(account)
			account.withdraw(amount)
			self.account_manager(account)

	def account_delete(self):
		pass

	def account_transfer(self, account):
		accounts = DB_API.fetch_all_accounts()
		dest_account = Views.account_transfer(account, accounts)
		amount = Views.transfer_amount(account)
		new_dest_balance = dest_account.balance + amount
		account.transfer(account.id, dest_account.id, amount, new_dest_balance)

c = Controller()
c.sign_in()