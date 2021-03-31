import ui
import console
import math

def add(sender):
	total = int(sender.superview['price'].text)
	val = int(sender.superview['input'].text)
	sender.superview['price'].text = str(total + val)
	sender.superview['input'].text = '0'
	
def calc_A(sender) :
	total = int(sender.superview['price'].text)
	people = int(sender.superview['people'].text)
	result1 = (total // 100) // people * 100
	result2 = total - (result1 * (people - 1))
	console.alert(
		'幹事	:' + str(result2) + '\nメンバー' + str(result1),

		'',
		'OK',
		hide_cancel_button=True)
		
def calc_B(sender) :
	total = int(sender.superview['price'].text)
	people = int(sender.superview['people'].text)
	result1 = math.ceil(total // people / 100) * 100
	result2 = total - (result1 * (people - 1))
	console.alert(
		'幹事	:' + str(result2) + '\nメンバー' + str(result1),
		'',
		'OK',
		hide_cancel_button=True)

v = ui.load_view()
print(v)
v.present('full_screen')
