import requests


def select_all_student() -> None:
    url = "http://localhost:8000/students"

    header = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=header)

        if response.status_code == 200:
            students = response.json()['students']
            print("All students:")
            for student in students:
                print("  student:")
                print(f"    id: {student['id']}")
                print(f"    name: {student['name']}")
                print(f"    age: {student['birthday']}")
                print(f"    grade: {student['class']}", end='\n\n')
        else:
            print("Failed to select all students.", end=' ')
            print(f"Status code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("Error: An error occurred while calling the API.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main() -> None:
    select_all_student()


if __name__ == "__main__":
    main()
