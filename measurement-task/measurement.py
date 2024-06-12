import requests
import time
import psycopg2
from datetime import datetime

urls = [
    "http://worldtimeapi.org/api/timezone/Europe/Berlin",
    "http://www.google.com/",
    "http://www.youtube.com/"
    ]

insert_querry = """
    INSERT INTO public.responsetimes (url, measuretime, responsetime) VALUES (%s, %s, %s)  
    """

CONNECTION = "postgres://postgres:password@localhost:5432/sampledata"
conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()

for i in range(50):
    for url in urls:
        response = requests.get(url)
        responsetime = response.elapsed.total_seconds() * 1000000
        measuretime = datetime.now()
        print(url, measuretime, responsetime)
        cursor.execute(insert_querry, (url, measuretime, responsetime))
        conn.commit()
    time.sleep(0.2)


# cursor.close()
# conn.close()