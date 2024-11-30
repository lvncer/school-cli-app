import requests


def search_student(name: str):

    url = f"http://localhost:8000/students/?name={name}"

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        students = response.json()['students']

        if response.status_code == 200:
            print("All students:")
            for student in students:
                print("  student:")
                print(f"    id: {student['id']}")
                print(f"    name: {student['name']}")
                print(f"    age: {student['birthday']}")
                print(f"    grade: {student['class']}", end='\n\n')
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


def main() -> None:
    name = input("Please enter the name you want to search!: ")

    search_student(name)


if __name__ == "__main__":
    main()
