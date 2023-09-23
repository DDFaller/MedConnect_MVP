from models import session
from load_db_sql import *
from models.schedule import Schedule

if __name__ =="__main__":
  #Create tables
  res = session.query(Schedule).filter(Schedule.clinic_id == "2").filter(Schedule.schedule_date == "2023-09-25").filter(Schedule.schedule_time == "11:00:00").all()
  print(res)