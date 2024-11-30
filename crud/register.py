import requests
import datetime


def register_student(
        student_id: int,
        name: str,
        birthday: datetime.date,
        class_: str) -> int:
    url = "http://localhost:8000/students"

    register_data = {
        "id": student_id,
        "name": name,
        "birthday": birthday,
        "clazz": class_
    }

    header = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=register_data, headers=header)

        if response.status_code == 201:
            print("Student registerd successfully.")
        else:
            print("Failed to update student.", end=' ')
            print(f"Status code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("Error: An error occurred while calling the API.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def validate_int(prompt: str) -> int:
    while True:
        num = input(prompt)
        try:
            num = int(num)
            break
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")
            continue
    return num


def validate_date(prompt: str) -> datetime.date:
    while True:
        str = input(prompt)
        try:
            datetime.datetime.strptime(str, "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid input. ", end='')
            print("Please enter a date in the format. [ % Y-%m-%d]")
            continue
        break

    return str


def main() -> None:
    student_id = validate_int(
        "Please Enter the student-id you want to register!: ")
    name = input("Please enter the name: ")
    birthday = validate_date("Please enter the birthday: ")
    class_ = input("Please enter the class: ")

    register_student(student_id, name, birthday, class_)


if __name__ == "__main__":
    main()
