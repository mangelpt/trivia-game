from trivia import trivia
import asyncio


async def get_questions(ammount=1):
    questions = await trivia.question(amount=ammount,
                                      category=10,
                                      difficulty='easy',
                                      quizType='multiple')
    return questions


def print_question(questions):
    question = questions.get("question")
    correct_answer = questions.get("correct_answer")
    incorrect_answers = questions.get("incorrect_answers")
    all_answers = incorrect_answers + [correct_answer]

    print(f"Question {question}")
    print("select the number of the correct alternative and press enter:")

    for count, answers in enumerate(all_answers):
        print(f"{count + 1} {answers}")

    user_answer = input()
    return [user_answer, correct_answer, all_answers]


def validate_user_answer(user_answer, correct_answer, all_answers):
    if int(user_answer) > 4:
        print("error try again")
        return

    answer_is_rigth = all_answers[int(user_answer) - 1] == correct_answer

    if answer_is_rigth:
        print(
            f"\x1b[6;30;42m great you did it !! { correct_answer} is correct answer congratulations \x1b[0m \n"
        )
    else:
        print(
            f"\033[91m incorrect the correct answer is  { correct_answer} \x1b[0m \n"
        )

    return answer_is_rigth


def main():
    print("welcome to trivia")
    name = input("enter your name: \n")
    ammount = int(input(f"I {name} enter amnount of questions:\n"))
  
    data = asyncio.run(get_questions(ammount))
    i = 0
    points = 0
    while i < ammount:
        user_answer, correct_answer, all_answers = print_question(data[i])
        answer_is_rigth = validate_user_answer(user_answer, correct_answer,
                                               all_answers)
        if answer_is_rigth:
            points += 10
        i += 1
    print(
        f"\033[92m you have {points} points thanks for playing my trivia game \033[92m"
    )


main()
