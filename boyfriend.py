#Program flow
#my boyfriend model
print("Welcome to my world,please respond to the questions below")

name =raw_input("whats your name: ")

age =input("whats your age: ")

if age >35:
	print("You are very old for me bambi")
	age =0

elif age <30:
	print("Sorry,you are a little baby for me ,sorry again")
	age =0

else :
	print("Congratulations,you passed this,now proceed to the next level")
	age =1
	
	#height

print("tell me about your height")

height =input("how tall are you in cms")

if height >170:
	print("You got me,lets continue")
	height =1

elif height <170:
	print("sorry,go find much shorter ladies,i love tall men")
	height =0

	#hiv status

hivstatus =("whats your hivstatus: ")