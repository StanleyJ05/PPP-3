def my_list_sorter(the_list):
  new_list = list()
  for item in the_list:
    if type(item) == list:
      new_list = new_list + my_list_sorter(item)
    else:
      new_list.append(item)
  return sorted(new_list)

print(my_list_sorter([4, [3, [12, 14], 5, 7, [50, 20]], 2, 1]))

# How does this solution ensure data immutability?
# It returns a new list instead of changing the original

# Is this solution a pure function? Why or why not?
#Yes, it only depends on the input and nothing outside of itself

# Is this solution a higher order function? Why or why not?
#No, it does not accept or return a higher order function.

# Would it have been easier to solve this problem using a different programming style?
#Not on something as foundational as a list.

# Why in particular is functional programming a helpful paradigm when solving this problem?
#This function only has one job to focus on

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.

class Podracer:
    def init(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
# Define a repair() method that will update the condition of the podracer to "repaired".
def repair(self):
    self.condition = "repaired"
def set_condition(self, condition):
    self.condition = condition
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
    def init(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

        def boost(self):
            self.max_speed *= 2
# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def init(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
  def flame_jet(self,other):
    other.condition = "trashed"

    pod = Podracer(4, 'trashed', 20000)
    pod.repair()
    print(pod.condition)

new_pod = AnakinsPod(2, 'perfect', 10000)
new_pod.boost()
print(new_pod.max_speed)

third_pod = SebulbasPod(2, 'perfect', 25000)
third_pod.flame_jet(third_pod)   
print(third_pod.condition)

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# Encapsulation - Information about one thing, bundled up into one object. So doing OOP without encapsulation doesn't seem possible.
# Inheritance - The repair method was inherited to the other classes as well as setting the self attributes.


# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
#No, even at this small amount, I think OOP was easiest 

# How in particular did Object Oriented Programming assist in the solving of this problem? 
# OOP seems particularly useful when representing something in the real world.

