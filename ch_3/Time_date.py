#current date
import datetime
today=datetime.date.today()
print(today)

#current date ans time
import datetime
today=datetime.datetime.now()
print(today)

print(today.day)
print(today.month)

#custom date
import datetime
my_date=datetime.date(2004,3,2)
print(my_date)

#formating date and time
import datetime
now = datetime.datetime.now()
print(now.strftime("%d/%m/%Y"))

#custom datetime
import datetime
now=datetime.datetime(2004,3,2,6,25,44)
print(now)

#converting string to date
import datetime
string_date="02/03/2004"
date=datetime.datetime.strptime(string_date, "%d/%m/%Y")
print(date)