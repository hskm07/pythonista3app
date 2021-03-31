import ui
import appex
import requests

class ExchangeRates (ui.View):
	def getExchangeRates(self):
		# web site url
		url = 'https://api.exchangeratesapi.io/latest?base=USD'
		# rate情報をjson形式で取得
		data = requests.get(url).json()
		
		for k, v in data['rates'].items():
			self.desc += k + ':' + str(v) + '\n'
			
		self.jpy = 'JPY : ' + str(data['rates']['JPY'])
		
		return len(data['rates'])
		
	def __init__(self):
		self.desc = ''
		self.jpy = ''
		self.content = ui.Label()
		self.bounds = (0,0,300,430)
		num = self.getExchangeRates()
		self.content.number_of_lines = num
		self.add_subview(self.content)
	
	def layout(self):
		if self.height >= 200:
			self.content.font = ('Arial Hebrew', 12)
			self.content.text = self.desc
			self.bounds = (0,0,300,430)
			self.content.bounds = (0,0,300,430)
			self.content.center = (150,215)
			
		else :
			self.content.font = ('Arial Hebrew', 24)
			self.content.text = '為替レート\n\n' + self.jpy
			self.bounds = (0,0,300,180)
			self.content.bounds = (0,0,300,180)
			self.content.center = (150,90)
		
appex.set_widget_view(ExchangeRates())
