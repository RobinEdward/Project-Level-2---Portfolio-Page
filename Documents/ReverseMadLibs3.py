# THIS IS ROBIN'S second ATTEMPT AT REVERSE MAD LIBS GAME
EASY = ["___1__"," is the core of computer science.", "A ","__2__", "can do anything, i.e., it can be programmed to do any computation.","__3__", "is a high-level general-purpose programming language.",
"We need to create languages to program computers to overcome the","__4__", "problem that exists in natural languages."]
Answer = ["Programming", "computer", "Python", "ambiguity" ]
Question =  ["Please enter keyword answer for the blank:"]
correct_msg = "Good job! Please continue to next question."
error_msg = "That's incorrect. Please try again."

count = 0
index = 1
	
while count < len(Answer):
        user_response= raw_input("Please enter keyword: ")
	for A in Answer:
        
                if user_response == Answer[count]:
                        return correct_msg
                else:
                        return error_msg
count += 1
index += 1


