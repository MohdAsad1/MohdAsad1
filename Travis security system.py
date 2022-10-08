list=["Anas","Asad","Ali","Nagina","Sadaf"]
while True:
    print("Hi my name is travis! ")
    name=input("whats is your name? ").strip().capitalize()
    if name in list:
        print("hello {}".format(name))
        remove=input("hey do you want to remove from the system? (y/n) ").strip().lower()
        if remove=="y":
            list.remove(name)
        elif remove=="n":
            print("The System will kept your Information")
    else:
        print("your name is not in our system! ")
        add=input("hey are you like to keep in our System? (y/n)").strip().lower()
        if add=="y":
            list.append(name)
        elif add=="n":
            print("Enjoy your day ",name)
