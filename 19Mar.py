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