from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_column():
    window = get_answer_placeholders()[0]
    if ":" in window:
        passed()
    else:
        failed("Don't forget about column at the end")


def test_window():
    window = get_answer_placeholders()[0]
    if "while " in window:
        passed()
    else:
        failed("Use while loop to iterate")


def test_window1():
    window = get_answer_placeholders()[0]
    if "number" in window:
        passed()
    else:
        failed("Use 'number' variable in while condition")


def test_window2():
    window = get_answer_placeholders()[0]
    if "<" in window and "10" in window:
        passed()
    else:
        failed("Check that 'number' is strictly less than 10 in condition")


def test_output():
    output = get_file_output()
    if "Finished" not in output:
        failed()
    border = output.index("Finished")
    user_squares = output[border + 1:]
    correct_answer = list(map(str, [x * x for x in range(1, 10)]))
    if correct_answer == user_squares:
        passed()
    else:
        failed("Wrong answer")

if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
    test_window2()
    test_column()
    test_output()
