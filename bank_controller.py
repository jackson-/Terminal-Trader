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
			choices = {'1' : self.account_list, '2' : self.account_register, '3' : self.sign_in}
			if choice in choices.keys():
				choices[choice]()
			else:
				Views.invalid()

	def account_list(self):
		while(True):
			accounts = DB_API.fetch_accounts(self.user.id)
			if accounts is None:
				self.account_register()
			else:
				account = Views.account_chooser(accounts)
				print(account)


	def account_register(self):
		while(True):
			account = Views.account_register()
			if account is None:
				Views.main_menu()
			else:
				DB_API.create_account(self.user.id, account[0], account[1])
			self.main_menu()




c = Controller()
c.sign_in()