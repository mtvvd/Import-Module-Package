from application.db.people import *
from application.salary import *
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now())
    get_employees()
    print(datetime.now())
    calculate_salary()