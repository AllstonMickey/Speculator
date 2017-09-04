from delorean import Delorean, move_datetime_day
from datetime import datetime as dt

def date_to_delorean(year, month, day):
    """
    Creates a Delorean object in UTC from a date.

    year: 1 <= year <= 9999
        type: integer
    month: 1 <= month <= 12 
        type: integer
    day: 1 <= day <= 31
        type: integer

    return: UTC date
        type: Delorean
    """
    return Delorean(datetime=dt(year, month, day), timezone='UTC')

def date_to_epoch(year, month, day):
    """
    Creates a Delorean object then gets its epoch in UTC from a date.

    year: 1 <= year <= 9999
        type: integer
    month: 1 <= month <= 12 
        type: integer
    day: 1 <= day <= 31
        type: integer

    return: UTC epoch
        type: integer
    """
    return int(date_to_delorean(year, month, day).epoch)

def now_delorean():
    return Delorean(timezone='UTC')

def shift_epoch(delorean, direction, unit, num_shifts):
    """
    Gets the resulting epoch after a shift of a Delorean
    
    delorean: Holds initial datetime
        type: Delorean
    direction: 'last' (move backwards in time) or
               'next' (move forwards in time)
        type: string
    unit: 'second', 'minute', 'hour', 'day', 'week', 'month', 'year'
        type: string
    num_shifts: Number of shifts by unit in direction
        type: integer

    return: shifted epoch
        type: integer
    """
    return int(delorean._shift_date(direction, unit, num_shifts).epoch)

def generate_epochs(delorean, direction, unit, num_shifts):
    """
    Generates a list of epochs from the data of
    a Delorean to some units in some direction.
    
    delorean: Holds initial datetime
        type: Delorean
    direction: 'last' (move backwards in time) or
               'next' (move forwards in time)
        type: string
    unit: 'second', 'minute', 'hour', 'day', 'week', 'month', 'year'
        type: string
    num_shifts: Number of shifts by unit in direction
        type: integer

    return: epochs within a range of shifts from the initial Delorean
        type: list of integers
    """
    return [int(delorean._shift_date(direction, unit, shift).epoch)
            for shift in range(num_shifts)]
