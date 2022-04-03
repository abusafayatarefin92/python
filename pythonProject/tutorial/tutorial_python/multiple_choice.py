from Questions import Questions

question_prompts = [
    "What color are apples? \n(a) red/green \n(b) purple \n(c) orange\n\n",
    "What color are bananas? \n(a) teal \n(b) magenta \n(c) yellow\n\n",
    "What color are strawberries? \n(a) yellow \n(b) red \n(c) blue\n\n",
]

question_and_correct_answers = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "c"),
    Questions(question_prompts[2], "b")
]


def run_test(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("Hey you got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(question_and_correct_answers)
