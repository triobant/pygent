from functions.run_python import run_python_file


def test():
    result = run_python_file("calculator", "main.py")
    print("Result for 'main.py' content:")
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for 'main.py' content:")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print("Result for 'tests.py' content:")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("Result for '../main.py' content:")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for 'nonexistent.py' content:")
    print(result)

if __name__ == "__main__":
    test()
