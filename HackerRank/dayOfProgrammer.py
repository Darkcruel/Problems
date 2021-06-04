#link : https://www.hackerrank.com/challenges/day-of-the-programmer/problem

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
        if year == 1918:
            return '26.09.1918'
        elif ((year <= 1917) & (year % 4 == 0)) or ((year % 400 == 0) or ((year % 4 == 0) & (year % 100 != 0))):
            return '12.09.'+str(year)
        else:
            return '13.09.'+str(year)