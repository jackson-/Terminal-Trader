from models import User, Portfolio, Account, Stock
from views import Views

class Controller(object):

	def sign_in(self):
		Views.sign_in()



c = Controller()
c.sign_in()