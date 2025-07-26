a = [1,2,3,5,6,76,2,5,78,9]

# indexing

print(a[0]) 
print(a[5]) 

#slicing

print(a[0:9:3]) #start end before step
print(a[1:])
print(a[0:])
print(a[-4:])
print(a[1:3])
print(a[0:4])

#access list

num = a[-1]
print(num)

fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado'
print(fruits) # chanage the value

exist = 'orange' in fruits
print(exist)

#append

fruits.append('lime')
print(fruits)  # adds at last


fruits.insert(2,"watermelon")
print(fruits)  # inserts value to the given index

fruits.remove("lime")
print(fruits)  # removes the value


fruits.pop()
print(fruits)  #takes out the last item

del fruits[3]
print(fruits)  #deletes based on index


fruits_copy = fruits.copy()
fruits_copy

#sorting

age = [23,34,23,56,52,45,75,27,13,46,86]
age.sort()
print(age)

age = [23,34,23,56,52,45,75,27,13,46,86]
age.sort(reverse=True)
print(age)