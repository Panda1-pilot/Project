def quiz():
   
    questions = [
        "What is the capital of France?",
        "Which planet is known as the Red Planet?",
        "What is 5 + 3?",
        "What is the boiling point of water in Celsius?",
        "Who wrote 'Hamlet'?",
        "Which element has the chemical symbol 'O'?",
        "What is the largest mammal?",
        "Which continent is known as the 'Dark Continent'?",
        "How many colors are there in a rainbow?",
        "What is the smallest prime number?",
    ]
    
    options = [
        ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
        ["1. Earth", "2. Mars", "3. Venus", "4. Jupiter"],
        ["1. 5", "2. 8", "3. 9", "4. 7"],
        ["1. 90", "2. 100", "3. 110", "4. 120"],
        ["1. Charles Dickens", "2. J.K. Rowling", "3. William Shakespeare", "4. Mark Twain"],
        ["1. Gold", "2. Oxygen", "3. Osmium", "4. Onyx"],
        ["1. Elephant", "2. Blue Whale", "3. Giraffe", "4. Human"],
        ["1. Asia", "2. Africa", "3. Europe", "4. Australia"],
        ["1. 5", "2. 6", "3. 7", "4. 8"],
        ["1. 0", "2. 1", "3. 2", "4. 3"],
    ]
    
    correct_answers = [3, 2, 2, 2, 3, 2, 2, 2, 3, 3]  
    
    score = 0
    max_score = len(questions) * 5
    
    
    for i in range(len(questions)):
        print(f"Q{i+1}: {questions[i]}")
        for option in options[i]:
            print(option)
        
        
        answer = int(input("Enter your choice (1-4): "))
        
        
        if answer == correct_answers[i]:
            print("Correct!")
            score += 5
        else:
            print("Incorrect!")
            score -= 2
        print()  
    
  
    pass_mark = max_score * 0.6
    print(f"Your total score is: {score}/{max_score}")
    
    if score >= pass_mark:
        print("Congratulations! You passed the quiz!")
    else:
        print("Sorry, you failed. Better luck next time!")


quiz()
