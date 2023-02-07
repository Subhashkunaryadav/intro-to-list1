#simple example of list
bicycles = ['trek', 'redline', 'cannondale', 'specialized']
print(bicycles)

#Accessing elements in a list
bicycles = ['trek', 'redline', 'cannondale', 'specialized']
print(bicycles[1])

#redline is capitalized
print(bicycles[1].title())

#index positions start at 0 not 1
bicycles = ['trek', 'redline', 'cannondale', 'specialized']
print(bicycles[1])
print(bicycles[2])
print(bicycles[-1])

#using individual value from list
bicycles = ['trek', 'redline', 'cannondale', 'specialized']
message = ' My first bicycles was ' + bicycles[1].title() + "."
print(message)

#changing element in list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#adding element in list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

#adding items in empty list
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#inserting element in list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#Removing elements from list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#removing item by value
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove ( 'yamaha')
print(motorcycles)

#message
motorcycles = ['honda', 'yamaha', 'suzuki']
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print  (" \nA " + too_expensive.title()+ " is too expensive for me.")

#sorting list
cars = ['bmw', 'audi', 'volvo', 'tata']
cars.sort()
print(cars)

#reversing
cars = ['bmw', 'audi', 'volvo', 'tata']
cars.sort(reverse=True)
print(cars)

#sorting list temporarily
cars = ['bmw', 'audi', 'volvo', 'tata']
print("Here is the original list")
print(cars)

print("Here is the sorted list")
print(sorted(cars))

print("Here is the original list again")
print(cars)

#printing in reverse order
cars =['bmw', 'audi', 'tata', 'volvo']
cars.reverse()
print(cars)

#finding length of the list
cars = ['tata', 'bmw', 'audi', 'volvo']
len(cars)
print(len(cars))

fruits = ['apple', 'orange', 'banana', 'grapes']
print("original list: ", fruits)
fruits.append('watermelon')
print(fruits)
fruits.remove('apple')
print("Removed fruit: ",fruits)
len(fruits)
print("Length of list: ", len(fruits))
print("Second element: ", fruits[1])


letters = ['a', 'b', 'c', 'd']
print("Original list:", letters)
letters.remove('b')
print("Removed letters: ",letters)
letters.append('z')
print("Adding new letter: ", letters)
len(letters)
print("length of the letters: ", letters)
letters.remove('a')
print("Removed letters: ", letters)
