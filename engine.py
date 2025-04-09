def run_game(game_logic, description):
    """Общий движок для игр."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)

    for _ in range(3):
        question, correct_answer = game_logic()
        print(f"Question: {question}")

        user_answer = input("Your answer: ")
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
