#Reference
# print([] is [])

# object1 = {'value':10}
# object2 = object1
# object3 = {'value':10}
# print(object1 is object2)
# print(object1 is object3)
# print(object1['value'] is object3['value'])

# object1['value'] = 15
# print(object2['value'])
# print(1 is 1)
#Context vs scope

def b():
	a = 4


#Instantiation
class Player:
	def __init__(self, name, type):
		print(self)
		self.type = type
		self.name = name

	def introduce(self) :
		print(f"Hi im {self.name}, Im a {self.type}")
		
class Wizard(Player):
	def __init__(self, name, type):
		super(Wizard, self).__init__(name, type)

	def play(self):
		print(f"WEEEE Im a {self.type}")

wizard1 = Wizard('Shelly', 'Healer')
wizard2 = Wizard('Shawn', 'Dark Magic')
wizard1.introduce()