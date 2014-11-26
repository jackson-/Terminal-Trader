import requests

class Markit:
	def __init__(self):
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

	def company_search(self, string):
		result = requests.get(self.lookup_url + string).json()
		if len(result) == 0:
			return(None)
		else:
			return(result)

	def get_quote(self, ticker):
		result = requests.get(self.quote_url + ticker).json()
		if 'Message' in result:
			return(None)
		else:
			return(result)


markit = Markit()
print(markit.company_search("Amazon.com Inc"))