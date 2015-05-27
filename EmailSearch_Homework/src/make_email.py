import settings
from database import login_info
import mysql.connector as msc
import datetime

def saveEmail(recipients, starttime, daysout):
    conn = msc.Connect(**login_info)
    curs = conn.cursor()
    
    curs.execute("DROP TABLE IF EXISTS messages")
    conn.commit()
    curs.execute(settings.TABLEDEF)
    conn.commit()
    
    for day in range(settings.DAYCOUNT):
        date_time = settings.STARTTIME + datetime.timedelta(days=day)
        for recipient_name, recipient_address in settings.RECIPIENTS:
            data = ("Test", date_time, "Eddie", "eddie.valv@gmail.com", 
                    recipient_name, recipient_address, "JOTD") 
            curs.execute("""
            INSERT INTO messages (msgMessageID, msgDate, msgSenderName,
            msgSenderAddress, msgRecipientName, msgRecipientAddress, msgText)
            VALUES (%s, %s, %s, %s, %s, %s, %s)""", data
            )
    conn.close()