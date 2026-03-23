#x = 10
#print(type(x))

number = 10
if number < 0:
   print("I have a negative number.")
elif number == 0:
   print("I have a zero.")
else:
   print("I have a positive number.")


for x in range(8):
    print ("X =",x)


groceries = ["milk", "bread", "rice", "tomatoes", "potatoes", "chocolate"]
for product in groceries:
 print(product)
 print(f"Я достал из пакета: {product}") # новий варіант з вткористанням f
 print("Я достал из пакета:", product) #старий варіант
