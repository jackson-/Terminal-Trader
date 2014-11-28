from bank_models import BankAccount, User, Client, Banker, DB_API
from bank_views import Views

class Controller:

	def sign_in(self):
		username = Views.sign_in()
		self.user = DB_API.fetch_user(username)
		if self.user == None:
			self.user_register()
		else:
			self.user_verify()

	def user_register(self):
		self.username = Views.user_register()
		self.password = Views.password_prompt()
		self.permission_level = Views.permission_prompt()
		choices = {'banker': DB_API.create_user(self.username, self.password, self.permission_level), 'client': DB_API.create_user(self.username, self.password, self.permission_level)}
		choices[self.permission_level]



c = Controller()
c.sign_in()