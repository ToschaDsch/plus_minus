import random

def get_a_simple_example_study_2(n_max: int=20) -> tuple[str, int]:
    """the function return answer and a string
            for example "4+10"
            for +, and -
            the summe is < n_max
            the answer are allways between 0 and 20
        """
    sign = random.choice(['+', '-'])
    n1 = random.randint(0, n_max)
    n2 = 0
    answer = 0
    match sign:
        case '+':
            n2 = random.randint(0, n_max - n1)
            answer = n1 + n2
        case '-':
            n2 = random.randint(0, n1)
            answer = n1 - n2
    string_ = f"{n1} {sign} {n2} "
    return string_, answer

def get_a_simple_example(n_max: int=20) -> tuple[str, int]:
    """the function return answer and a string
        for example "4+10"
        for +, and -
        the summe is < n_max
        the example are simple, there are not 9+7, or 12-5
        the answer are allways between 10 and 20
    """
    sign = random.choice(['+', '-'])
    n1 = random.randint(0, n_max-10)
    n2 = 0
    answer = 0
    match sign:
        case '+':
            n2 = random.randint(0, n_max-n1-10)
            answer = n1 + n2 + 10
            if random.randint(0, 1) == 0:   # first or second element + 10
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
        return False
    return answer == answer_input

def start_the_function():
    string_, answer = get_a_simple_example_study_2()
    print(string_, end="")
    while not check_the_answer(answer):
        print("falsch :(")
    print("richtig! :)")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(10):
        print("Nr.", i+1)
        start_the_function()
    print("Gut gemacht!")
    input()


