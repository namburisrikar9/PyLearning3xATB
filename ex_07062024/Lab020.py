# In built functions
# functions -> repeat a task - you can use a function
# print(), Input(), type(), format(), max(), min(), id(), sum(), avg()

# String
# len(), range(), get(), next(), tuple(), input(), dict(), open(), int(), id(),

name = "Namburi Srikar"

print(name)

print(type(name))

print(id(name)) # id -> memory Address where it is stored 2331653512304

print(len(name)) # length of the String ( including Spaces)

# upper & lower Case & Count of letters
name = name.lower()
print(name)

name= name.upper()
print(name)

#name = name.count('i')
#print(name)

#name = name.upper().count('i')
#print(name)

print(name[13])

python - Immutable - that cant be change
name[0] ="p" # string object once not support items assignment