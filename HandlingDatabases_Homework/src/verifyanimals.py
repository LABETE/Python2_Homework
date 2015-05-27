"""
Verifies that every animal eats
at least one food
"""
import mysql.connector

from database import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

cursor.execute("SELECT name, family FROM animal LEFT JOIN food ON animal.id = anid WHERE anid IS NULL")

consult_result=cursor.fetchall()

if not consult_result:
    print("All animals have food") 
else:
    for name, family in consult_result:  
        print("{0} from the {1} family is not being feeded".format(name, family))

