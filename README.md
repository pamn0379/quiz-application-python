# quiz-application-python
A quiz application written by Python:
- Using questions.toml to store the meta data about the questions.
- Using pipenv to create a virtual environment.
- Install toml package.
- How to build the quiz application:
    + Step 1: Load the list of questions from the meta data file and shuffle them. 
    (questions.toml, prepare_question())
    + Step 2: Load the correct answers and answer choices from the meta data and shuffle them.
    (ask_question_and_get_player_answer)
    + Step 3: Build the answer choices under type a. answer1, b.answer2.
    (ask_question_and_get_player_answer)
    + Step 4: Based on the number of correct answers, force the player types the responsive answers.
    (ask_question_and_get_player_answer)
    + Step 5: Compare correct answers and answers from the player, keep track the correct answers.
    (compare_answers)