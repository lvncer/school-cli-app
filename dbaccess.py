from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import datetime
import mysql.connector

app = FastAPI()


class Student(BaseModel):
    id: int = None
    name: str
    birthday: datetime.date
    clazz: str = None


# MySQLに接続
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="school"
)


# 全ての生徒情報を取得するAPI
@app.get("/students")
def find_all():
    sql = "SELECT * FROM student ORDER BY id"

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()

    return {"students": results}


# 指定されたIDの生徒情報を取得するAPI
@app.get("/students/{student_id}")
def find_one(student_id: int, response: Response):
    sql = "SELECT * FROM student WHERE id = %s"
    value = (student_id, )

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql, value)
    result = cursor.fetchone()

    if result is not None:
        return {"student": result}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Student not found"}


# 学生登録
@app.post('/students', status_code=201)
def register(student: Student):
    sql = """
    INSERT INTO student (id, name, birthday, class)
    VALUES (%s, %s, %s, %s)
    """
    values = (student.id, student.name, student.birthday, student.clazz)

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql, values)
    mydb.commit()

    return {"message": "Student created successfully"}


# 学生更新
@app.put('/students/{student_id}', status_code=204)
def update(student_id: int, student: Student, response: Response):
    if is_student_id_exists(student_id):
        sql = """
        UPDATE student
        SET name = %s, birthday = %s, class = %s WHERE id = %s
        """
        values = (student.name, student.birthday, student.clazz, student_id)

        cursor = mydb.cursor(dictionary=True)
        cursor.execute(sql, values)
        mydb.commit()

        return {"message": "Student updated successfully"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Student not found"}


# 学生削除
@app.delete('/students/{student_id}', status_code=204)
def delete(student_id: int, response: Response):
    if is_student_id_exists(student_id):
        sql = "DELETE FROM student WHERE id = %s"
        value = (student_id,)

        cursor = mydb.cursor(dictionary=True)
        cursor.execute(sql, value)
        mydb.commit()

        return {"message": "Student deleted successfully"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Student not found"}


# 学生検索
@app.get('/students/')
def search(name: str):
    sql = "SELECT * FROM student WHERE name LIKE %s"
    value = ('%' + name + '%',)

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql, value)
    results = cursor.fetchall()

    return {"students": results}


# IDの存在をチェックする
def is_student_id_exists(student_id: int):
    sql = "SELECT * FROM student WHERE id = %s"
    value = (student_id,)

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql, value)
    result = cursor.fetchone()

    return result is not None
