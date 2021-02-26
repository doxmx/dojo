# Implement functions here
def template(arg):
    result = f"Doing something with {arg}"
    return result

def is_leap_year(year):
    if not isinstance(year, int):
        return False
    if not year%400 :
        return True
    if not year%4 and year%100 :
        return True

    return False
