import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
citys = ('chicago', 'new york city', 'washington')
months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please select the city to analyze it\'s data from chicago, new york city, washington: ').lower()
    while True:
        if city not in CITY_DATA.keys():
            print('\nInvalid input, Please try again\n')
            city = input('Please select the city to analyze it\'s data from chicago, new york city, washington: ').lower()
        else:
            print('\nCity selected is {}\n'.format(city))
            break
    # get user input for month (all, january, february, ... , june)
    month = input('Please select a month from all, january, february, march, april, may, june: ').lower()
    while True:
        if month not in months:
            print('\nInvalid input, Please try again\n')
            month = input('Please select a month from all, january, february, march, april, may, june: ').lower()
        else:
            print('\nMonth: {}\n'.format(month))
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please select a day of the week from all, monday, tuesday, wednesday, thursday, friday, saturday, sunday: ').lower()
    while True:
        if day not in days:
            print('\nInvalid input, Please try again\n')
            day = input('Please select a day of the week from all, monday, tuesday, wednesday, thursday, friday, saturday, sunday: ').lower()
        else:
            print('\nDay: {}\n'.format(day))
            break
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    #Convert start time column to datetime and creating month ,weekday and hour columns
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['Month']=df['Start Time'].dt.month
    df['Week Day']=df['Start Time'].dt.day_name()
    df['Hour']=df['Start Time'].dt.hour
    #Filtering by Month:
    if month != 'all':
        month = months.index(month)
        df = df[df['Month'] == month]
    #Filter by Day:
    if day != 'all':
        df = df[df['Week Day'].str.startswith(day.title())]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['Month'].mode()[0]
    print('The most common month is {}'.format(most_common_month))
    # display the most common day of week
    most_common_day = df['Week Day'].mode()[0]
    print('\nThe most common day is {}'.format(most_common_day))
    # display the most common start hour
    most_common_hour = df['Hour'].mode()[0]
    print('\nThe most common hour is {}'.format(most_common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is {}'.format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nThe most common end station is {}'.format(common_end_station))
    # display most frequent combination of start station and end station trip
    df['Trips'] = df['Start Station']+ " to " + df['End Station']
    common_trip = df['Trips'].mode()[0]
    print('\nThe most common trip is {}'.format(common_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = int(df['Trip Duration'].sum())
    print('Total time traveled is: {}\n'.format(travel_time))
    # display mean travel time
    mean_time = int(df['Trip Duration'].mean())
    print('Mean time traveled is: {}'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types: {}\n'.format(user_types))

    # Display counts of gender
    if city != 'washington':
        gender_count = df['Gender'].value_counts()
        print('Gender Counts: {}\n'.format(gender_count))
    # Display earliest, most recent, and most common year of birth
        min_year = int(df['Birth Year'].min())
        print('Earliest year of birth: {}\n'.format(min_year))
        max_year = int(df['Birth Year'].max())
        print('Most recent year of birth: {}\n'.format(max_year))
        common_year = int(df['Birth Year'].mode()[0])
        print('Most common year of birth: {}'.format(common_year))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays Raw data of BikeShare if user requests."""
    rows = 0
    raw_data= input('To view raw data type yes else type no : ').lower()
    while True:
        if raw_data == 'no':
            break
        elif raw_data == 'yes':
            print(df[rows:rows+5])
            rows +=5
            raw_data= input('To view next 5 columns type yes else type no : ').lower()
        else:
            raw_data = input('\nInvalid input, To view raw data type yes else type no : ').lower()
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart != 'yes':
            break

if __name__ == "__main__":
	main()
