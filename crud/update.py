import requests
import datetime


def update_student(student_id: int, name: str, birthday, class_: str) -> int:
    url = f"http://localhost:8000/students/{student_id}"

    update_data = {
        "id": student_id,
        "name": name,
        "birthday": birthday,
        "clazz": class_
    }

    header = {"Content-Type": "application/json"}

    try:
        response = requests.put(url, json=update_data, headers=header)

        if response.status_code == 204:
            print("Student updated successfully.")
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
            print("Error: Invalid input.", end='')
            print("Please enter a date in the format. [%Y-%m-%d]")
            continue
        break

    return str


def main() -> None:
    student_id = validate_int(
        "Please Enter the student-id you want to update!: ")
    name = input("Please enter the new name: ")
    birthday = validate_date("Please enter the new birthday: ")
    class_ = input("Please enter the new class: ")

    update_student(student_id, name, birthday, class_)


if __name__ == "__main__":
    main()
