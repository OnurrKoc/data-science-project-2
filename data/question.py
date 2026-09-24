import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = '1907'


def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password=password)
    return conn


def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE age > 22')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM courses WHERE category = 'Veritabanı'")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE first_name LIKE 'A%'")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM courses WHERE course_name LIKE '%SQL%'")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students WHERE age BETWEEN 22 AND 24')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT DISTINCT s.first_name, s.last_name FROM students s INNER JOIN enrollments e ON s.student_id = e.student_id ORDER BY s.first_name;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT c.course_name, COUNT(e.student_id) AS student_count FROM courses AS c LEFT JOIN enrollments AS e ON c.course_id = e.course_id WHERE c.category = 'Veritabanı' GROUP BY c.course_id, c.course_name ORDER BY c.course_id")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, i.name AS instructor_name FROM courses c LEFT JOIN course_instructors ci ON c.course_id = ci.course_id LEFT JOIN instructors i ON ci.instructor_id = i.instructor_id ORDER BY c.course_id;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.student_id, s.first_name, s.last_name, s.email, s.age FROM students s LEFT JOIN enrollments e ON s.student_id = e.student_id WHERE e.student_id IS NULL;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, AVG(s.age) AS avg_age FROM courses c INNER JOIN enrollments e ON c.course_id = e.course_id INNER JOIN students s ON e.student_id = s.student_id GROUP BY c.course_name ORDER BY c.course_name ASC;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_11_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.first_name, s.last_name, COUNT(e.course_id) AS total_courses FROM students s LEFT JOIN enrollments e ON s.student_id = e.student_id GROUP BY s.student_id, s.first_name, s.last_name ORDER BY s.student_id;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_12_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT i.name AS instructor_name, COUNT(ci.course_id) AS total_courses FROM instructors i INNER JOIN course_instructors ci ON i.instructor_id = ci.instructor_id GROUP BY i.name HAVING COUNT(ci.course_id) > 1;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_13_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT c.course_name, COUNT(DISTINCT e.student_id) AS unique_students FROM courses c LEFT JOIN enrollments e ON c.course_id = e.course_id GROUP BY c.course_name ORDER BY c.course_name ASC;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_14_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT s.first_name, s.last_name FROM students s INNER JOIN enrollments e1 ON s.student_id = e1.student_id INNER JOIN courses c1 ON e1.course_id = c1.course_id AND c1.course_name = 'SQL Temelleri' INNER JOIN enrollments e2 ON s.student_id = e2.student_id INNER JOIN courses c2 ON e2.course_id = c2.course_id AND c2.course_name = 'İleri SQL';")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_15_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT s.first_name, s.last_name, c.course_name, i.name AS instructor_name, e.enrollment_date FROM enrollments e INNER JOIN students s ON e.student_id = s.student_id INNER JOIN courses c ON e.course_id = c.course_id LEFT JOIN course_instructors ci ON c.course_id = ci.course_id LEFT JOIN instructors i ON ci.instructor_id = i.instructor_id ORDER BY e.enrollment_id;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data