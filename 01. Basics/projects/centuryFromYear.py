# centuryFromYear

'''
Given a year, return the century it is in. 
The first century spans from the year 1 up to and including the year 100, 
the second - from the year 101 up to and including the year 200, etc.
'''

def solution(year):
    if year%100 > 0:
        return (year//100)+1
    else:
        return year//100


# TEST
YEARS = [1, 137, 3623, 1000, 2020, 1904, 100, 1964, 1431, 1234, 2000]
for year in YEARS:
	century = solution(year)
	print('YEAR: {}, CENTURY: {}'.format(year, century))