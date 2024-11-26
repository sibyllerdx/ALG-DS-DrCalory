def bmr():
  height = ''
  weight = ''
  age = ''
  while True:
    if not height:
      height = input("What is your height (cm): ")
      if not height.isnumeric():
        print('Invalid height. Enter a whole number.')
        height = ''
        continue
      else:
        height = float(height)
    if not weight:
      try:
        weight = float(input("What is your weight (kg): "))
      except ValueError:
        print('Invalid weight. Enter a whole number.')
        weight = ''
        continue
    if not age:
      age = input("What is your age: ")
      if not age.isnumeric():
        print('Invalid age. Enter a whole number.')
        age = ''
        continue
      else:
        age = float(age)
    gender = input("What is your gender (M/F): ")
    if not gender.upper() in ['M', 'F']:
      print('Invalid input. Enter M or F')
      gender = ''
      continue
    break
  if gender.upper() == "M":  # Added .upper() to handle lowercase input
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
  else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age)
  return bmr

class Node():
  def __init__(self, value):
    self.value = value
    self.adjacencyList = {}

  def traversal(self):
    if self.adjacencyList == {}:
      return self.value
    else:
      answer = self.askQuestion()
      if answer in self.adjacencyList:
        return self.adjacencyList[answer].traversal()
      else:
        print('Invalid response! Please try again')
        return self.traversal()

  def insertNode(self, value, key):
    node = Node(value)
    self.adjacencyList[key]=node
    return node

  def askQuestion(self):
    return input('\n'+self.value+'\n  --->  ')

car = Node('How many times a week do you do cardio?\nExamples: running, swimming, cycling\n0:Never\n1:Once or twice\n2:Three or four\n3:Five or more')

w0 = car.insertNode('How many times a week do you do strength training like weight lifting?\n0:Never\n1:Once or twice\n2:Three or four\n3:Five or more', '0')
w1 = car.insertNode('How many times a week do you do strength training like weight lifting?\n0:Never\n1:Once or twice\n2:Three or four\n3:Five or more', '1')
w2 = car.insertNode('How many times a week do you do strength training like weight lifting?\n0:Never\n1:Once or twice\n2:Three or four\n3:Five or more', '2')
w3 = car.insertNode('How many times a week do you do strength training like weight lifting?\n0:Never\n1:Once or twice\n2:Three or four\n3:Five or more', '3')

ex00 = w0.insertNode('How many times a week do you do light exercise?\nExamples: walking, yoga, stretching\n0:Never\n1:Once or twice\n2:Three or four\n3:Five or more', '0')
ex01 = w0.insertNode('How many times a week do you do light exercise?\nExamples: walking, yoga, stretching\n0:Never\n1:Once or twice\n2:Three or four\n3:Five or more', '1')
w0.insertNode(1.3, '2')
w0.insertNode(1.5, '3')

ex00.insertNode(1, '0')
ex00.insertNode(1.05, '1')
ex00.insertNode(1.1, '2')
ex00.insertNode(1.15, '3')

ex01.insertNode(1.1, '0')
ex01.insertNode(1.15, '1')
ex01.insertNode(1.2, '2')
ex01.insertNode(1.25, '3')

w1.insertNode(1.2, '0')
w1.insertNode(1.3, '1')
w1.insertNode(1.5, '2')
w1.insertNode(1.7, '3')

w2.insertNode(1.5, '0')
w2.insertNode(1.6, '1')
w2.insertNode(1.8, '2')
w2.insertNode(2, '3')

w3.insertNode(1.75, '0')
w3.insertNode(1.85, '1')
w3.insertNode(2, '2')
w3.insertNode(2.2, '3')

goal = Node('What is your goal?\n0:Lose weight\n1:Maintain weight\n2:Gain muscle mass')

time0 = goal.insertNode('Over what timespan?\n0:Short term\n1:Long term', '0')
goal.insertNode(1, '1')
time2 = goal.insertNode('Over what timespan?\n0:Short term\n1:Long term', '2')

time0.insertNode(0.8, '0')
time0.insertNode(0.9, '1')

time2.insertNode(1.2, '0')
time2.insertNode(1.1, '1')

def split(calories):
    protein = round((calories * 0.24)/4,2)
    carbs = round((calories * 0.56)/4,2)
    fat = round((calories * 0.2)/9,2)
    print(f'\nHere is your daily split:\n')
    print(f'Total Calories: {round(calories,2)}')
    print(f'Proteins: {protein} grams')
    print(f'Carbs: {carbs} grams')
    print(f'Fat: {fat} grams')

def main():
    BMR = bmr()
    multiplier = car.traversal()
    percentage = goal.traversal()
    calories = BMR * multiplier * percentage
    split(calories)

main()
