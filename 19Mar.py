while True:
    text = input("Enter a string: ")
    if text == "":
        print("Thanks for playing!")
        break
    print("1)", text.capitalize())
    print("2)", text.lower())
    print("3)", text.title())
    print("4)", text.upper())


    num_dict = {}
    for i in range(1, 4):
     num_dict[i] = str(i)


some_string = "apple banana apple orange banana apple"
split = some_string.split()
counter = {}
for word in split:
    if word not in counter:
        counter[word] = 1
    else:
        counter[word] += 1
print(counter)



a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = list(set(a) & set(b))
print(common)

