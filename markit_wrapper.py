import requests

class Markit:
	def __init__(self):
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

	def company_search(self, string):
		result = requests.get(self.lookup_url + string).json()
		if len(result) == 0:
			return(False)
		else:
			return(result)

	def get_quote(self,string):
		result = requests.get(self.quote_url + string).json()
		if 'Message' in result:
			return(False)
		else:
			return(result)


# markit = Markit()
# markit.company_search("AAPL")