import argparse
import re
from pathlib import Path


class PythonCodeBuilderAI:
    """Generates working Python code for common beginner project ideas."""

    def generate(self, prompt: str) -> str:
        text = prompt.lower()

        if "calculator" in text:
            return self._calculator_code()
        if "guess" in text or "game" in text:
            return self._guessing_game_code()
        if "password" in text:
            return self._password_checker_code()
        if "todo" in text or "task" in text:
            return self._todo_list_code()
        if "budget" in text:
            return self._budget_tracker_code()
        if "file" in text:
            return self._file_reader_code()
        if "hello" in text or "greet" in text:
            return self._hello_world_code()

        return self._generic_code(prompt)

    @staticmethod
    def _hello_world_code() -> str:
        return '''def greet_user():
    name = input("What is your name? ")
    print(f"Hello, {name}! Welcome to Python!")


greet_user()
'''

    @staticmethod
    def _calculator_code() -> str:
        return '''def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose (+, -, *, /): ")

if operation == "+":
    print("Answer:", add(num1, num2))
elif operation == "-":
    print("Answer:", subtract(num1, num2))
elif operation == "*":
    print("Answer:", multiply(num1, num2))
elif operation == "/":
    print("Answer:", divide(num1, num2))
else:
    print("Invalid operation.")
'''

    @staticmethod
    def _guessing_game_code() -> str:
        return '''import random

secret_number = random.randint(1, 10)
tries = 0

while True:
    guess = int(input("Guess a number from 1 to 10: "))
    tries += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {tries} tries.")
        break
'''

    @staticmethod
    def _password_checker_code() -> str:
        return '''def is_strong_password(password):
    if len(password) < 8:
        return False
    if password == password.lower():
        return False
    if password == password.upper():
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True


password = input("Create a password: ")

if is_strong_password(password):
    print("Strong password accepted.")
else:
    print("Password is too weak. Use at least 8 characters, uppercase, lowercase, and a number.")
'''

    @staticmethod
    def _todo_list_code() -> str:
        return '''tasks = []

while True:
    choice = input("Add task (a), view tasks (v), or quit (q): ").lower()

    if choice == "a":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == "v":
        print("Your tasks:")
        for task in tasks:
            print(f"- {task}")
    elif choice == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
'''

    @staticmethod
    def _budget_tracker_code() -> str:
        return '''budget = 1000

income = float(input("How much money did you earn? "))
expense = float(input("How much did you spend? "))

budget = budget + income - expense
print(f"Your final budget is: ${budget:.2f}")
'''

    @staticmethod
    def _file_reader_code() -> str:
        return '''filename = input("Enter a file name: ")

with open(filename, "r", encoding="utf-8") as file:
    contents = file.read()

print(contents)
'''

    @staticmethod
    def _generic_code(prompt: str) -> str:
        cleaned = prompt.strip() or "create a small Python app"
        safe_name = re.sub(r"[^a-zA-Z0-9_ ]", "", cleaned).strip()
        name = re.sub(r"\s+", "_", safe_name).lower() or "project"

        return f'''def {name}():
    print("This is a Python program for: {cleaned}")
    value = input("Type something: ")
    print(f"You entered: {{value}}")


{name}()
'''


def main():
    parser = argparse.ArgumentParser(description="AI that builds Python code from a prompt.")
    parser.add_argument("prompt", nargs="*", help="Describe the Python program you want built.")
    parser.add_argument("-o", "--output", help="Optional filename to save the generated Python code.")
    args = parser.parse_args()

    prompt_text = " ".join(args.prompt).strip()
    if not prompt_text:
        prompt_text = input("Describe the Python program you want me to build: ")

    ai = PythonCodeBuilderAI()
    code = ai.generate(prompt_text)

    print("Generated Python code:")
    print("-" * 50)
    print(code)
    print("-" * 50)

    if args.output:
        output_path = Path(args.output)
        if not output_path.suffix:
            output_path = output_path.with_suffix(".py")
        output_path.write_text(code, encoding="utf-8")
        print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()
