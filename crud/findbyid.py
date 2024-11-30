import requests


def findbyid_student(student_id: int) -> None:
    url = f"http://localhost:8000/students/{student_id}"

    header = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=header)

        if response.status_code == 200:
            response_json = response.json()
            student = response_json['student']
            print()
            print("student:")
            print(f"  id: {student['id']}")
            print(f"  name: {student['name']}")
            print(f"  age: {student['birthday']}")
            print(f"  grade: {student['class']}", end='\n\n')
        else:
            print("Failed to select the student.", end=' ')
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


def main() -> None:
    student_id = validate_int(
        "Please Enter the student-id you want to find!: ")

    findbyid_student(student_id)


if __name__ == "__main__":
    main()
