## TODO: import all necessary packages and functions
import csv
import time
from collections import Counter
from datetime import datetime
from pprint import pprint

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    city = city.lower()
    if city == 'chicago':
        return chicago
    elif city == 'new york':
        return new_york_city
    elif city == 'washington':
        return washington
    # TODO: handle raw input and complete function


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    if time_period == 'month':
        return get_month()
    elif time_period == 'day':
        return get_day()
    else:
        return 'none'
    # TODO: handle raw input and complete function


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    # TODO: handle raw input and complete function
    month = month.lower()
    valid_months = ['january','february','march','april','may','june']
    if month in valid_months:
        return month
    else:
        print('Invalid Month')
        get_month()

def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as an integer.\n').lower()
    # TODO: handle raw input and complete function
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    if day in days:
        return day
    elif int(day) in range(0,7):
        return days[int(day)]
    else:
        print('Enter a Valid day or the number of day(0-6).')
        get_day()


def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    freq = Counter()
    filename = city_file
    monthList = ['January','February','March','April','May','June']
    with open(filename,newline='\n') as csvfile:
        d = csv.DictReader(csvfile)
        for row in d:
            m = row['Start Time'].split(' ')[0].split('-')[1]
            m = int(m)
            month = monthList[m-1]
            freq[month] += 1
        popMonth = freq.most_common()[0][0]
        rides = freq.most_common()[0][1]
        print('Most popular month is {} with {} rides.'.format(popMonth, rides))



def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    freq = Counter()
    filename = city_file
    with open(filename,newline='\n') as csvfile:
        dic = csv.DictReader(csvfile)
        for row in dic:
            d = row['Start Time'].split(' ')[0].split('-')[2]
            freq[d] += 1
        popDay = freq.most_common()[0][0]
        rides = freq.most_common()[0][1]
    print('Most popular day is {}th with {} rides.'.format(popDay, rides))


def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    freq = Counter()
    filename = city_file
    with open(filename,newline='\n') as csvfile:
        dic = csv.DictReader(csvfile)
        for row in dic:
            d = row['Start Time'].split(' ')[1].split(':')[0]
            freq[d] += 1
        popHour = freq.most_common()[0][0]
        rides = freq.most_common()[0][1]
        print(freq.most_common())
        print('Most popular Hour for travel is [{}] with {} rides.'.format(popHour, rides))


def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    freq = Counter()
    rides=0
    filename = city_file
    totalDur = 0
    with open(filename,newline='\n') as csvfile:
        dic = csv.DictReader(csvfile)
        for row in dic:
            dur = row['Trip Duration']
            if(city_file == 'washington.csv'):
                dur = int(float(dur))
            else:
                dur = int(dur)
            rides+=1
            totalDur += dur
        avgTripDuration = totalDur/rides
        print('There were a total of {} rides, with total trip duration of {}. Average trip duration was {}.'.format(rides, totalDur, avgTripDuration))


def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function
    freq = Counter()
    filename = city_file
    with open(filename,newline='\n') as csvfile:
        d = csv.DictReader(csvfile)
        for row in d:
            ss = row['Start Station']
            es = row['End Station']
            freq[ss] += 1
            freq[es] += 1
        station = freq.most_common()[0][0]
        print('Most popular station is {}.'.format(station))

def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function
    freq = Counter()
    filename = city_file
    with open(filename,newline='\n') as csvfile:
        d = csv.DictReader(csvfile)
        for row in d:
            ss = row['Start Station']
            es = row['End Station']
            trip = ss+'?'+es
            freq[trip] += 1
        station = freq.most_common()[0][0]
        station1 = station.split('?')[0]
        station2 = station.split('?')[1]
        print('Most popular trip is from "{}" to "{}".'.format(station1,station2))



def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    freq = Counter()
    filename = city_file
    with open(filename,newline='\n') as csvfile:
        di = csv.DictReader(csvfile)
        for row in di:
            uType = row['User Type']
            freq[uType] += 1
        d = freq.most_common()
        for item in d:
            print('No of {} is {}.'.format(item[0],item[1]))


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function
    freq = Counter()
    filename = city_file
    with open(filename,newline='\n') as csvfile:
        di = csv.DictReader(csvfile)
        for row in di:
            g = row['Gender']
            freq[g] += 1
        d = freq.most_common()
        print('No of {} is {}.'.format(d[0][0],d[0][1]))
        print('No of NaN is {}.'.format(d[1][1]))
        print('No of {} is {}.'.format(d[2][0],d[2][1]))


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    # TODO: complete function
    freq = Counter()
    filename = city_file
    with open(filename,newline='\n') as csvfile:
        di = csv.DictReader(csvfile)
        for row in di:
            b = row['Birth Year']
            freq[b] += 1
        c = freq.most_common()
        for item in c:
            if item[0] != '':
                print('No of travellers born in the year {} are {}.'.format(int(float(item[0])),item[1]))
            else:
                print('No of travellers with no year specified is {}'.format(item[1]))


def display_data(city_file,limit):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    
    # TODO: handle raw input and complete function
    position = 0
    filename = city_file
    with open(filename,newline='\n') as csvfile:
        di = csv.DictReader(csvfile)
        dataList = list(di)
        si = len(dataList)
        while True:
            display = input('\nWould you like to view individual trip data?'
                            'Type \'yes\' or \'no\'.\n')
            if display == 'yes':
                if position>(si - 5):
                    print('End of file reached')
                    break
                else:
                    for i in range(position,position+5):
                    	print(dataList[i])
                    position += 5
            else:
                break




def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        #TODO: call popular_month function and print the results
        popular_month(city,time_period)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        # TODO: call popular_day function and print the results
        popular_day(city,time_period)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")    

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    popular_day(city,time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    trip_duration(city,time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    popular_stations(city,time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    popular_trip(city,time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    users(city,time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    gender(city,time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    z = display_data(city,4)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()