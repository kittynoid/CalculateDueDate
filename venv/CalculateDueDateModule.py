import datetime
from datetime import timedelta
import sys

DAY_END_HOUR = 17
DAY_END_MINUTE = 0

def CalculateDueDate(submit_date, turnaround_time):
    submit_day_end = submit_date.replace(hour=DAY_END_HOUR,minute=DAY_END_MINUTE, second=0)
    difference = submit_day_end - submit_date
    turnaround_time_sec = datetime.timedelta(seconds=turnaround_time*3600)

    if turnaround_time_sec <= difference:
        due_date = submit_date + timedelta(seconds=turnaround_time*3600)

    else:
        remainder = turnaround_time_sec - difference
        days = 1
        while remainder > timedelta(seconds = 8*3600):
            remainder -= timedelta(seconds = 8*3600)
            days += 1

        due_date = datetime.datetime.combine(submit_date.date() + timedelta(days=days), (submit_date.replace(hour=9,minute=0,second=0)+remainder).time())

    for i in range(days+2):
        temp_date = submit_date + timedelta(days=i)
        if temp_date.weekday() in (5,6):
            due_date += timedelta(days=1)

    print(due_date)
    return due_date

if __name__ == '__main__':
    try:
        submit_date = sys.argv[1]
        turnaround_time = sys.argv[2]
        date_time_obj = datetime.datetime.strptime(submit_date, "%Y-%m-%dT%H:%M:%S%z")
        if(date_time_obj.hour<9 or date_time_obj.hour>17):
            raise ValueError
        CalculateDueDate(date_time_obj, int(turnaround_time))
    except IndexError:
        print("Missing or incorrect input arguments. Please provide the submit date and the turnaround time of the issue.")
    except ValueError:
        print("Wrong date format or date is out of working hours.")
    except:
        print("Something went wrong...")






