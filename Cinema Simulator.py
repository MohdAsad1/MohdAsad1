movie={
    "Dabang" : [12,5],
    "Kick" : [15,5],
    "Sultan" : [18,5],
    "Radhe" : [14,5]
      }
while True:
    choice=input("enter the movie you want to watch! ").strip().title()
    if choice in movie:
        age=int(input("how old are you").strip())
                                                                  #checked user age
        if age>=movie[choice][0]:
                                                                  #checked seats
           seats=movie[choice][1]
           if seats>0:
               print("Enjoy the film")
               movie[choice][1]=movie[choice][1]-1
           else:
               print("sorry sold out!")
        else:
            print("you are too young to watch the film")
    else:
        print("we did not have that film! ")

