from random import choice
question=("why is the sky is blue? :-","where are the Dianosours? :-","why earth is round? :-")
question=choice(question)
answer=input(question).strip().lower()
while (answer!="just becouse"):
    answer=input("why -").strip().lower()

print("okk")