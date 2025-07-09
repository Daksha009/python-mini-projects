questions = [
    ["What is the capital of France?", "A) Paris", "B) London", "C) Berlin", "D) Madrid", "A"],

    ["What is the largest planet in our solar system?", "A) Earth", "B) Jupiter", "C) Saturn", "D) Mars", "B"],

    ["Who wrote 'To Kill a Mockingbird'?", "A) Harper Lee", "B) Mark Twain", "C) F. Scott Fitzgerald", "D) Ernest Hemingway", "A"],

    ["What is the chemical symbol for gold?", "A) Au", "B) Ag", "C) Pb", "D) Fe", "A"],

    ["What is the smallest prime number?", "A) 0", "B) 1", "C) 2", "D) 3", "C"],

    ["What is the capital of Japan?", "A) Beijing", "B) Seoul", "C) Tokyo", "D) Bangkok", "C"],

    ["What is the largest mammal?", "A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus", "B"],

    ["What is the boiling point of water?", "A) 50°C", "B) 75°C", "C) 100°C", "D) 150°C", "C"],

    ["Who painted the Mona Lisa?", "A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet", "C"],

    ["What is the hardest natural substance on Earth?", "A) Gold", "B) Diamond", "C) Iron", "D) Quartz", "B"]
]

prizes = [
    "$100", "$200", "$300", "$500", "$1,000", "$2,000", "$4,000", "$8,000", "$16,000", "$32,000"]

i = 0
print("Welcome to 'Who Wants to be a Millionaire'!")
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    #check whether the answer is correct or not
    a = str(input("Enter your answer (a/b/c/d): "))
    if (question[5].lower() == a.lower()):
        print("Correct answer!")
    else:
        print("Wrong answer!")
        print(f"The correct answer is: {question[5]}")
        break
    #if the answer is correct, print the prize

    print(f"You have won {prizes[i]}")
    i =+ 1

  
    
    
