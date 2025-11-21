import random


def get_an_example(n_max: int=10) -> tuple[str, int]:
    sign = random.choice(['+', '-'])
    n1 = random.randint(0, n_max)
    n2 = 0
    answer = 0
    match sign:
        case '+':
            n2 = random.randint(0, n_max-n1)
            i = random.randint(0, 1)
            answer = n1 + n2 + 10
            if i == 0:
                n1+=10
            else:
                n2+=10
        case '-':
            n2 = random.randint(0, n1)
            n1+=10
            answer = n1 - n2
    string_ = f"{n1} {sign} {n2} "
    return string_, answer

def check_the_answer(answer: int) -> bool:
    try:
        answer_input = int(input("= "))
    except ValueError as e:
        print(f"ValueError: {e}")
        return False
    return answer == answer_input

def start_the_function():
    string_, answer = get_an_example()
    print(string_, end="")
    while not check_the_answer(answer):
        print("falsch :(")
    print("richtig! :)")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_the_function()


