import tomllib, random
from pathlib import Path 
from string import ascii_lowercase

QUESTIONS_PATH = Path(__file__).parent/'questions.toml'
NUMBER_QUESTIONS_PER_QUIZ = 5

def prepare_question(path: Path, number_questions):
    questions = tomllib.loads(path.read_text())['questions'] # questions are lists of dictionary.
    number_questions = min(number_questions, len(questions))
    return random.sample(questions, k=number_questions) # return lists of dictionary 

def ask_question_and_get_player_answer(question, requied_choices):
    print(f'{question['question']}?')
    answer_choices = question['correct_answers'] + question['answer_choices']
    list_answer_choices = random.sample(answer_choices, len(answer_choices)) # return a list of answer choices
    dict_answer_choices = dict(zip(ascii_lowercase, list_answer_choices))
    for label, answer in dict_answer_choices.items():
        print(f'{label}. {answer}')

    while True:
        plural_s = ""if requied_choices == 1 else f"s {requied_choices} answers"
        player_answer = input(f'\nChoice{plural_s}: ')
        answers = set(player_answer.replace(',', ' ').split())

        # answers over the correct answers
        if len(answers) != requied_choices:
            plural_s = ""if requied_choices == 1 else"s (seperated by comma)"
            print(f'Please choice {requied_choices} answer{plural_s}!')
            continue     
        # answer not in list label of answer choices
        if any(
            (invalid := answer) not in dict_answer_choices
            for answer in answers
        ):
            print(
                f'{invalid} is not a valid choice'
                f'Please select answer in {', '.join(dict_answer_choices)}'
            )
            continue
        return [dict_answer_choices[answer] for answer in answers]

def compare_answers(question):
    correct_answers = question['correct_answers']
    required_choices = len(question['correct_answers'])

    player_answer = ask_question_and_get_player_answer(question, required_choices)

    if correct := (set(correct_answers) == set(player_answer)):
        print('Correct!')
    else:
        is_or_are = ' is' if len(correct_answers) == 1 else 's are'
        print(f'\n '.join([f'No, the correct answer{is_or_are}:'] + correct_answers))
    
    return 1 if correct else 0

def run_quiz():
    questions = prepare_question(QUESTIONS_PATH, NUMBER_QUESTIONS_PER_QUIZ)

    number_correct = 0
    #questions are lists of dictionary, question is a dictionary.
    for num, question in enumerate(questions, start=1):                                              
        print(f'\nQuestion {num}')
        number_correct += compare_answers(question)
    print(f'You got {number_correct} correct!')
if __name__ == '__main__':
    run_quiz()
