from math import floor

def ConvertSecToSortTime(GivenSeconds):
    year = GivenSeconds // (12 * 30 * 24 * 3600)
    GivenSeconds = GivenSeconds % (12 * 30 * 24 * 3600)

    month = GivenSeconds // (30 * 24 * 3600)
    GivenSeconds = GivenSeconds % (30 * 24 * 3600)

    day = GivenSeconds // (24 * 3600)
    GivenSeconds = GivenSeconds % (24 * 3600)

    hour = GivenSeconds // 3600
    GivenSeconds %= 3600

    minute = GivenSeconds // 60
    GivenSeconds %= 60

    second = int(GivenSeconds)

    millisecond = int(str(round((GivenSeconds - int(GivenSeconds)),2))[2:])

    if(year != 0):
        return f'''{int(floor(year))} year'''
    elif(year == 0 and month != 0):
        return f'''{int(floor(month))} month'''
    elif(year == 0 and month == 0 and day != 0):
        return f'''{int(floor(day))} day'''
    elif(year == 0 and month == 0 and day == 0 and hour != 0):
        return f'''{int(floor(hour))} hour'''
    elif(year == 0 and month == 0 and day == 0 and hour == 0 and minute != 0):
        return f'''{int(floor(minute))} min'''
    elif(year == 0 and month == 0 and day == 0 and hour == 0 and minute == 0 and second != 0):
        return f'''{int(floor(second))} sec'''
    else:
        return f'''{int(floor(millisecond))} ms'''

def ConvertSecToFullTime(GivenSeconds):
    year = GivenSeconds // (12 * 30 * 24 * 3600)
    GivenSeconds = GivenSeconds % (12 * 30 * 24 * 3600)

    month = GivenSeconds // (30 * 24 * 3600)
    GivenSeconds = GivenSeconds % (30 * 24 * 3600)

    day = GivenSeconds // (24 * 3600)
    GivenSeconds = GivenSeconds % (24 * 3600)

    hour = GivenSeconds // 3600
    GivenSeconds %= 3600

    minute = GivenSeconds // 60
    GivenSeconds %= 60

    second = int(GivenSeconds)

    millisecond = int(str(round((GivenSeconds - int(GivenSeconds)),2))[2:])

    if(year != 0):
        return f'''{year} year - {month} month - {day} day - {hour} hour : {minute} minute : {second} second : {millisecond} millisecond'''
    elif(year == 0 and month != 0):
        return f'''{month} month - {day} day - {hour} hour : {minute} minute : {second} second : {millisecond} millisecond'''
    elif(year == 0 and month == 0 and day != 0):
        return f'''{day} day - {hour} hour : {minute} minute : {second} second : {millisecond} millisecond'''
    elif(year == 0 and month == 0 and day == 0 and hour != 0):
        return f'''{hour} hour : {minute} minute : {second} second : {millisecond} millisecond'''
    elif(year == 0 and month == 0 and day == 0 and hour == 0 and minute != 0):
        return f'''{minute} minute : {second} second : {millisecond} millisecond'''
    elif(year == 0 and month == 0 and day == 0 and hour == 0 and minute == 0 and second != 0):
        return f'''{second} second : {millisecond} millisecond'''
    else:
        return f'''{millisecond} millisecond'''