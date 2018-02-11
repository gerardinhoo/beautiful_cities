# Make a list to hold onto our team
beautiful_cities = []

# print out instructions on how to use the app
print("What are some of your favorites in the world you know of?")
print("Enter 'DONE' to stop adding cities")

while True:
# ask for new item
    new_city = input("> ")

#add 'DONE' to be able to quit the apps
    
    if new_city == 'DONE':
        break


 # add new items to our list
    beautiful_cities.append(new_city)

    
# print out the list
print("Here are the list of some of your favorites cities in the world!")

for city in beautiful_cities:
    print(city)
     
       

   



