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
      weight = input("What is your weight (kg): ")
      if not weight.isnumeric():
        print('Invalid weight. Enter a whole number.')
        weight = ''
        continue
      else:
        weight = float(weight)
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
      answer = self.askQuestion().lower()
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

car = Node('How many times a week do you do cardio?\nExamples: running, swimming, cycling\na:Never\nb:Once or twice\nc:Three or four\nd:Five or more')

w0 = car.insertNode('How many times a week do you do strength training like weight lifting?\na:Never\nb:Once or twice\nc:Three or four\nd:Five or more', 'a')
w1 = car.insertNode('How many times a week do you do strength training like weight lifting?\na:Never\nb:Once or twice\nc:Three or four\nd:Five or more', 'b')
w2 = car.insertNode('How many times a week do you do strength training like weight lifting?\na:Never\nb:Once or twice\nc:Three or four\nd:Five or more', 'c')
w3 = car.insertNode('How many times a week do you do strength training like weight lifting?\na:Never\nb:Once or twice\nc:Three or four\nd:Five or more', 'd')

ex00 = w0.insertNode('How many times a week do you do light exercise?\nExamples: walking, yoga, stretching\na:Never\nb:Once or twice\nc:Three or four\nd:Five or more', 'a')
ex01 = w0.insertNode('How many times a week do you do light exercise?\nExamples: walking, yoga, stretching\na:Never\nb:Once or twice\nc:Three or four\nd:Five or more', 'b')
w0.insertNode(1.3, 'c')
w0.insertNode(1.5, 'd')

ex00.insertNode(1, 'a')
ex00.insertNode(1.05, 'b')
ex00.insertNode(1.1, 'c')
ex00.insertNode(1.15, 'd')

ex01.insertNode(1.1, 'a')
ex01.insertNode(1.15, 'b')
ex01.insertNode(1.2, 'c')
ex01.insertNode(1.25, 'd')

w1.insertNode(1.2, 'a')
w1.insertNode(1.3, 'b')
w1.insertNode(1.5, 'c')
w1.insertNode(1.7, 'd')

w2.insertNode(1.5, 'a')
w2.insertNode(1.6, 'b')
w2.insertNode(1.8, 'c')
w2.insertNode(2, 'd')

w3.insertNode(1.75, 'a')
w3.insertNode(1.85, 'b')
w3.insertNode(2, 'c')
w3.insertNode(2.2, 'd')

goal = Node('What is your goal?\na:Lose weight\nb:Maintain weight\nc:Gain muscle mass')

time0 = goal.insertNode('Over what timespan?\na:6 months or less\nb:Over 6 months', 'a')
goal.insertNode(1, 'b')
time2 = goal.insertNode('Over what timespan?\na:6 months or less\nb:Over 6 months', 'c')

time0.insertNode(0.8, 'a')
time0.insertNode(0.9, 'b')

time2.insertNode(1.2, 'a')
time2.insertNode(1.1, 'b')

def split(calories):
    protein = round((calories * 0.4)/4,2)
    carbs = round((calories * 0.4)/4,2)
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
