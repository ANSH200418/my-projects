def valid_length(time):
    length = len(time)
    if (length != 5):
        return False
    return True

def valid_input(time):
    for i in range(len(time)):
        if(i == 2):
            if(time[i] != ':'):
                return False
        else:
            if(time[i].isnumeric() == False):
                return False
    return True

def valid_numbers(time):
    hour = int(time[0:2])
    minute = int(time[3:5])
    if (hour > 23 or hour < 0) or (minute > 59 or minute < 0):
        return False
    return True

def is_valid(time):
    if(valid_length(time)):
        if(valid_input(time)):
            if(valid_numbers(time)):
                return True
    return False


time = input("Enter time in HH:MM format : ")
if(is_valid(time)):
    hour = int(time[0:2])
    hour = hour%12
    minute = int(time[3:5])
    hour_degree = hour*30
    minute_degree = minute*6
    degree = abs(hour_degree - minute_degree)
    if(degree > 180):
        degree = 360 - degree
    print("angle between hour hand and minute hand is : ", degree)
else:
  print("invalid input")