from models import User, Portfolio, Account, Stock, DB_API
from views import Views
import re

class Controller(object):

	def sign_in(self):
		while(True):
			self.username = Views.sign_in()
			print(self.username)
			self.user = DB_API.fetch_user(self.username)
			print(self.user)
			if self.user == None:
				Views.clear()
				return self.user_registration()
			else:
				Views.clear()
				self.id = self.user[0][0]
				self.password = self.user[0][1]
				self.first_name = self.user[0][2]
				self.last_name = self.user[0][3]
				password_attempt = Views.user_prompt("What is your password?:  ")
				if password_attempt != self.password:
					Views.clear()
					print("I'm sorry that was the wrong password?")
					continue
				else:
					Views.clear()
					return self.main_menu()

	def user_registration(self):
		while(True):
			choice = Views.user_prompt("You don't seem to have an account with us. Would you like to register? Y/N?: ")
			if choice == "y" or choice == "Y":
				self.first_name = Views.user_prompt("What is your first name?:  ")
				self.last_name = Views.user_prompt("What is your last name?:  ")
				self.password = Views.user_prompt("What is your password?:  ")
				DB_API.create_user(self.username, self.password, self.first_name, self.last_name)
				self.user = DB_API.fetch_user(self.username)
				self.id = self.user[0][0]
				self.password = self.user[0][1]
				self.first_name = self.user[0][2]
				self.last_name = self.user[0][3]
				return self.main_menu()
			elif choice == "n" or choice == "N":
				return self.sign_in()

	def main_menu(self):
		while(True):
			choice = Views.main_menu()
			if choice == "1":
				account_list = DB_API.fetch_accounts(self.user.id)
				if accounts_list == None:
					account_name = Views.account_register():
					init_balance = Views.user_prompt("What will be the initial balance?: ")
				else:
					Views.accounts_list(account_list)
			


c = Controller()
c.sign_in()