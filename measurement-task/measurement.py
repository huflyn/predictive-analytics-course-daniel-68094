import requests
import time
import psycopg2
from datetime import datetime
import pytz

user_timezone = pytz.timezone("Europe/Berlin")

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

while True:
    for url in urls:
        response = requests.get(url)
        responsetime = response.elapsed.total_seconds() * 1000
        measuredate = user_timezone.localize(datetime.now())
        utc_date = measuredate.astimezone(pytz.utc)
        print(url, measuredate, responsetime)
        cursor.execute(insert_querry, (url, measuredate, responsetime))
        conn.commit()
    time.sleep(1)


# cursor.close()
# conn.close()