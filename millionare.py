questions = [
    ["Who is Shah Rukh khan ?","WWE wrestler", "Actor", "Astronaut", "Plumber", 2],
    ["What is the capital of france ?", "Rome", "london", "paris", "Berlin", 3],
    ["Which planet is known as the red planet ?","Earth", "Jupiter", "Venus", "Mars", 4],
    ["What is the largest mammal ?", "Elephant", "Blue Whale", "Giraffee", "Shark", 2],
    ["Who wrote romeo and juliet ?", "Charles Dickens", "William Shakesphere", "Jane Austin", "Homer",1],
    ["Which country is known as the wrising sun ?", "China", "Japan", "South korea", "India", 2],
    ["Which ocean is the largest ?", "Atlantic ocean", "Indian ocean", "Artic ocean", "Pacific ocean", 4]
]

prices = [10000, 320000, 500000, 10000000, 2000000, 2500000, 300000]
sum = 0
for question in questions:
    i = 0
   
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

#check whether the answer is correct or not

    a = int(input("Enter your answer : \n 1 for a, 2 for b, 3 for c, 4 for d \n"))

    if question[5] == a:
        print("Correct answer")
    else:
        print(f"Incorrect. The correct answer was = {question[5]}")
        print("Better luck next time ")
        break
   
    print(f"You won {prices[i]}")
    i += 1


