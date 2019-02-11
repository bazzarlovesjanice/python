import random
def get_question_from_user(friend):
    print("{} {} what is your question?".format("hello", friend))
    question =raw_input()

    print("Your question is:{}".format(question))

def generate_random_number():
    random_number = random.randint(0,4)
    return random_number

friend = "Vivian"
answer_list = ["yes", "no", "maybe", "ask again", "no chance"]

get_question_from_user(friend)
random_number = generate_random_number()
answer = answer_list[random_number]

if answer =="ask again":
    print(answer)
    get_question_from_user(friend)
    random_number = generate_random_number()
    answer = answer_list[random_number]
    print(answer)
else:
    print(answer)
