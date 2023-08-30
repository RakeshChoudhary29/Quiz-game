
import os
import random





apj_abdul_kalam_quiz =  [
        (
            "What does 'APJ' stand for in APJ Abdul Kalam's name?: ",
            "Which missile was developed under Dr. Kalam's leadership and is named after a mythical bird?: ",
            "What is the title of Dr. Kalam's autobiography?: ",
            "Before becoming President, what was Dr. Kalam's primary area of expertise?: ",
            "In which year did Dr. Kalam become the President of India?"
        ),
        (
            ("A. Avul Pakir Jainulabdeen", "B. Abdul Parvez Javed", "C. Abhinav Prakash Janardhan", "D. Arvind Prasad Joshi"),
            ("A. Agni", "B. Trishul", "C. Nag", "D. Akash"),
            ("A. Wings of Fire", "B. Ignited Minds", "C. My Journey", "D. India 2020"),
            ("A. Economics", "B. Medicine", "C. Aeronautics", "D. Political Science"),
            ("A. 2001", "B. 2002", "C. 2003", "D. 2004")
        ),
        ("A", "C", "A", "C", "D")
    ]




sports_quiz = [
        (
            "Which sport is known as the 'king of sports'?: ",
            "In which country did the modern Olympic Games originate?: ",
            "Which cricketer is known as the 'Master Blaster'?: ",
            "Which Indian hockey legend is known as the 'Wizard'?: ",
            "Who is the current captain of the Indian cricket team?"
        ),
        (
            ("A. Football (Soccer)", "B. Tennis", "C. Cricket", "D. Basketball"),
            ("A. France", "B. Greece", "C. Italy", "D. United Kingdom"),
            ("A. Rahul Dravid", "B. Sachin Tendulkar", "C. Virat Kohli", "D. Virender Sehwag"),
            ("A. Dhyan Chand", "B. Balbir Singh Sr.", "C. Milkha Singh", "D. P. T. Usha"),
            ("A. Rohit Sharma", "B. Virat Kohli", "C. Ravindra Jadeja", "D. Shikhar Dhawan")
        ),
        ("C", "B", "B", "A", "B")

]


science_quiz = [
        (
            "What is the chemical symbol for the element Oxygen?: ",
            "Which planet is known as the 'Red Planet'?: ",
            "What is the process by which plants make their own food?: ",
            "Which force keeps objects on the Earth's surface?: ",
            "What is the smallest unit of matter?"
        ),
        (
            ("A. O2", "B. Ox", "C. Oxide", "D. O"),
            ("A. Jupiter", "B. Saturn", "C. Mars", "D. Venus"),
            ("A. Respiration", "B. Photosynthesis", "C. Digestion", "D. Fermentation"),
            ("A. Magnetic force", "B. Gravitational force", "C. Friction", "D. Electrostatic force"),
            ("A. Atom", "B. Molecule", "C. Cell", "D. Proton")
        ),
        ("D", "C", "B", "B", "A")
    ]



indian_gk_quiz = [
        (
            "Which city is known as the 'Pink City' of India?: ",
            "Which river is known as the 'Ganga of the South'?: ",
            "Which famous monument is located in Agra, India?: ",
            "What is the national flower of India?: ",
            "Who was the first Prime Minister of India?"
        ),
        (
            ("A. Jaipur", "B. Kolkata", "C. Delhi", "D. Mumbai"),
            ("A. Yamuna", "B. Brahmaputra", "C. Godavari", "D. Kaveri"),
            ("A. Qutub Minar", "B. Red Fort", "C. India Gate", "D. Taj Mahal"),
            ("A. Rose", "B. Lotus", "C. Sunflower", "D. Jasmine"),
            ("A. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. Sardar Patel", "D. Rajendra Prasad")
        ),
        ("A", "D", "D", "B", "A")
    ]








mathematician_quiz =  [
        (
            "Who is known for his contributions to number theory, modular forms, and infinite series, and is often called the 'Man Who Knew Infinity'?: ",
            "Which Indian mathematician made substantial contributions to mathematical analysis, number theory, infinite series, and continued fractions?: ",
            "Who was a pioneering mathematician and computer scientist, known for his work in breaking the Enigma code during World War II?: ",
            "Who developed the concept of 'zero' and the decimal system, revolutionizing mathematics and its applications?: ",
            "Who authored the treatise 'Lilavati' in the 12th century and is often referred to as the 'Greatest Mathematician of India'?"
        ),
        (
            ("A. Aryabhata", "B. Bhaskara II", "C. Brahmagupta", "D. Srinivasa Ramanujan"),
            ("A. Srinivasa Ramanujan", "B. Aryabhata", "C. Brahmagupta", "D. Bhaskara II"),
            ("A. Alan Turing", "B. Albert Einstein", "C. Isaac Newton", "D. Galileo Galilei"),
            ("A. Aryabhata", "B. Al-Khwarizmi", "C. Brahmagupta", "D. Fibonacci"),
            ("A. Aryabhata", "B. Bhaskara II", "C. Brahmagupta", "D. Srinivasa Ramanujan")
        ),
        ("D", "D", "A", "A", "B")
    ]





quiz=[apj_abdul_kalam_quiz ,sports_quiz ,science_quiz ,indian_gk_quiz ,mathematician_quiz ]


number_array=[0,1,2,3,4]


flag=True



while(True):

    if(flag):
        x = input("Do You want To Play Quiz Game type (yes or no): ")
        flag=False
        if (x == "NO" or x=="no"):
            break


    random_number = random.choice(number_array)
    number_array.remove(random_number)

    if(len(number_array)== 0):
        break


    questions = quiz[random_number][0]

    options = quiz[random_number][1]

    answers = quiz[random_number][2]
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("----------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1



    print("----------------------")
    print("       RESULTS        ")
    print("----------------------")

    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)

    print(f"Your score is: {score}%")

    x = input("Do You want To Play Quiz Game  again type (yes or no): ")
    if (x == "NO" or x == "no"):
        break



print("Quiz Finished")


















