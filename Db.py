from multiprocessing import connection
import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

db = sqlite3.connect('CourseCatalog.db')
cursor = db.cursor()

lstCourse = cursor.execute('''select name, subject from Catalog''').fetchall()
db.commit()
print(lstCourse)