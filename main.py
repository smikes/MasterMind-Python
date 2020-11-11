from random import randint

def generate_num(answer):
  for i in range(0, len(answer)):
    answer[i] = randint(1,9)
  return answer

def analyze_guess(answer, guess):
  #answer and guess are both int arrays of length 3
  if answer==guess: 
    return "green, green, green"
  else:
    analysis = [""]*3
    copy_guess = guess

    for i in range(0, len(answer)):
      for j in range(0, len(guess)):
        if (answer[i] == copy_guess[j]):
          copy_guess[j] = -1
          #answer[i] = -1
          if (i == j):
            analysis[i] = "green"
          else:
            if (analysis[i] != "green"):
              analysis[i] = "yellow"
    
    if "green" not in analysis and "yellow" not in analysis:
      analysis[0] = "red"

    # print ("Unsorted Analysis: %s" % (analysis))
    analysis.sort()
    analysis_as_string = ""

    for i in range(0, len(analysis)-1):
      if (analysis[i] != ""):
        analysis_as_string += analysis[i] + ", "
    
    analysis_as_string += analysis[ len(analysis)-1 ]
    return analysis_as_string


answer = [-1]*3
guess = [-1]*3

print ("What would you like to do?")
print ("1. Testing Version")
print ("2. Mastermind Game")

choice = (int)(input(""))

if choice==1:
  print ("For answer:")
  answer[0] = (int)(input("What is the first number? "))
  answer[1] = (int)(input("What is the second number? "))
  answer[2] = (int)(input("What is the third number? "))

  while True:
    print("\n")
    print ("For guess:")
    guess[0] = (int)(input("What is your first digit? "))
    guess[1] = (int)(input("What is your second digit? "))
    guess[2] = (int)(input("What is your third digit? "))

    print ( analyze_guess (answer, guess) )

    continue_loop = input("Would you like to continue? ")
    if continue_loop=="no":
      break
else:
  answer = generate_num(answer)
  attempts = 1

  hasWon = False

  while attempts < 11:
    print("\n")
    print ("Guessing:")
    guess[0] = (int)(input("What is your first digit? "))
    guess[1] = (int)(input("What is your second digit? "))
    guess[2] = (int)(input("What is your third digit? "))

    print("")
    print ("Turn %s: Your Guess: %s" % (attempts, str(guess)) )
    #print ("Answer: %s, Your Guess: %s" % (answer, guess))

    analysis = analyze_guess(answer,guess)

    print (analysis)

    if analysis=="green, green, green":
      hasWon = True
      break

    attempts += 1
  
  if hasWon:
    print("You won! The computer's number was %s" % ( str(answer)) )
  else:
    print("You lost. The computer's number was %s" % ( str(answer)) )   


'''
Test Evaluations (Answer is 123):

  Guess		Evaluation			          Attempts
  134		  green, yellow			        1 		//notice no red
  213		  green, yellow, yellow	    2			//notice the green is first, always
  312		  yellow, yellow, yellow		3
  143		  green, green			        4
  300		  yellow				            5
  555		  red				                6			//red will only appear here
  114		  green				              7			//notice that there is no yellow for the second 1
  123 		green,green,green		      7     //correct answer
        
  Computer number is 242
	Guess is 213
	Correct evaluation: Green
  Incorrect Evaluation: Green, Yellow
		
  Computer number is 242
	Guess is 443
  Correct evaluation: Green
  Incorrect Evaluation: Green, Yellow
'''