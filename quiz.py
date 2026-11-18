import json

with open("questions.json", 'r') as file:
    data = json.loads(file.read())

print("Mini Quizzz \n")
for question in data:
    print(question["question_text"])
    for index,alternative in enumerate(question["alternatives"]):
        print(f"{index+1}-{alternative}")
    user_choice = int(input("Enter your answer : "))
    question["user_answer"] = user_choice


score = 0
for index, question in enumerate(data):
    if question["user_answer"] == question["correct_answer"]:
        result = "correct answer"
        score+=1
    else:
        result = "wrong answer"

    message = f"{index+1}. {result}, your answer:{question['user_answer']}\
    correct answer : {question['correct_answer']}"

    print(message)

score*=50
print()
if score > 50 :
    print(f"horeee ..... your score : {score}")
else:
    print(f"Not bad... your score : {score}")
print()
