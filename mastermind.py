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

