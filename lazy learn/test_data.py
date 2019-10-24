import pandas as pd

def get_date(date):

    if date == 1:
        date += 5

    elif date == 2:
        date += 10

    elif date == 3:
        date += 15

    elif date == 4:
        date += 20

    elif date == 5:
        date += 25

    elif date == 6:
        date += 30

    elif date == 7:
        date += 35

    elif date == 8:
        date += 40

    elif date == 9:
        date += 45

    elif date == 10:
        date += 50

    elif date == 11:
        date += 55

    elif date == 12:
        date += 60

    elif date == 13:
        date += 65

    elif date == 14:
        date += 70

    elif date == 15:
        date += 75

    elif date == 16:
        date += 80

    elif date == 17:
        date += 85

    elif date == 18:
        date += 90

    elif date == 19:
        date += 95

    elif date == 20:
        date += 100

    elif date == 21:
        date += 105

    elif date == 22:
        date += 110

    elif date == 23:
        date += 115

    elif date == 24:
        date += 120

    elif date == 25:
        date += 125

    elif date == 26:
        date += 130

    elif date == 27:
        date += 55

    elif date == 28:
        date += 135

    elif date == 29:
        date += 140

    elif date == 30:
        date += 145

    elif date == 31:
        date += 150

    else: 
        pass

    return date

def get_month(month):

    if month == 1:
        month += 5

    elif month == 2:
        month += 10

    elif month == 3:
        month += 15

    elif month == 4:
        month += 20

    elif month == 5:
        month += 25

    elif month == 6:
        month += 30

    elif month == 7:
        month += 35

    elif month == 8:
        month += 40

    elif month == 9:
        month += 45

    elif month == 10:
        month += 50

    elif month == 11:
        month += 55

    elif month == 12:
        month += 60

    else:
        pass

    return month

def get_test_row(property_name, room_name, date, month):

    train_row = []

    if str(property_name) == "Perch Arbor Suites":

        _property_name_ = 1

        room_name = str(room_name)

        winsome = room_name.find('Winsome')
        sterling = room_name.find('Sterling')
        classic = room_name.find('Executive')

        if classic == 0: #classic
        
            _room_name_ = 1
            month = get_month(month)

            train_row.append(_property_name_)
            train_row.append(_room_name_)
            train_row.append(month)

        elif winsome == 0: #wins

            _room_name_ = 2
            month = get_month(month)

            train_row.append(_property_name_)
            train_row.append(_room_name_)
            train_row.append(month)

        elif sterling == 0: #sterl

            _room_name_ = 3
            month = get_month(month)

            train_row.append(_property_name_)
            train_row.append(_room_name_)
            train_row.append(month)

        else:
            pass

    elif str(property_name) == "Perch Arbor- Golf Course Road":

        _property_name_ = 2
        room_name = str(room_name)

        winsome = room_name.find('Winsome')
        sterling = room_name.find('Sterling')
        executive = room_name.find('Executive')

        if executive == 0: #executive

            _room_name_ = 1
            month = get_month(month)
            train_row.append(_property_name_)
            train_row.append(_room_name_)
            train_row.append(month)

        elif winsome == 0: #winsome

            _room_name_ = 2
            month = get_month(month)
            train_row.append(_property_name_)
            train_row.append(_room_name_)
            train_row.append(month)

        elif sterling == 0: #sterling

            _room_name_ = 3
            month = get_month(month)
            train_row.append(_property_name_)
            train_row.append(_room_name_)
            train_row.append(month)

        else:
            pass

    else:
        pass

    return train_row
