def exam_scores():

    # Exam score and grades

    print("Welcome to the exam score  for your Maths,Science and English subjects ")

    print("enter your marks and view your scores")

    name=raw_input ('What is you name: ')

    maths_score=input ("Enter your Maths Marks" )
    science_score=input ("Enter your Science Marks")
    english_score= input (" Enter your English marks:")
   
score=[english_score, maths_score, science_score]

    for x in score:
        if  x>= 95:
            grade="A"
        elif  x >= 75 and x < 95:
            grade="B"

        elif x >60 and x <75  
            grade="C"

        elif x>45 and x<60
            grade="D"

          else: 
            grade "F"  
       
        print("you got grade {0} for score {1}".format(grade,x))

        Average=

        Total=
        
