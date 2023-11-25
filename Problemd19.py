#January, February, march, April, May, June, July, August, September, October, November,December
months = [31,29,31,30,31,30,31,31,30,31,30,31]
days = 2
sundays = 0

def leap_year(year):
    if year%100 ==0:
        if year%400 == 0:
            return True
    elif year%4 == 0:
        return True
    return False


for month in range(len(months)):
    for m in range(months[month]):
        if days == 7:
            days= 0
        days+=1

for year in range(1901,2001):
    months[1] = 28
    if leap_year(year):
        months[1] = 29

    for month in range(len(months)):
        for m in range(months[month]):
            if days == 7:
                days= 0
            elif m == 0 and days==1 :
                sundays +=1
            days+=1
print(sundays)