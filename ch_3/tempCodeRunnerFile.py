
#converting string to date
import datetime
string_date="02/03/2004"
date=datetime.datetime.strptime(string_date, "%d/%m/%Y")
print(date)