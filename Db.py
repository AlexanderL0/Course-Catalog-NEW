from multiprocessing import connection
import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

db = sqlite3.connect('CourseC.db')
cursor = db.cursor()

lstCourse = cursor.execute('''select  credits from Course_Info''').fetchall()
db.commit()
print(lstCourse)