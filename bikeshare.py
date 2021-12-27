import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Please choos a city from Chicago, New-york-city, washington: ').lower()
        if city not in CITY_DATA:
            print('Please choose a valid city')
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month= input('Please enter a month from january to june, or type"all"to display all months: ').lower()
        months = ['january','february','march','april','may','june']
        if month != 'all' and month not in months:
            print('Please enter a full valid month name')
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while true:
        day= input('Please enter a day of the week, or type "all"to display all days: ').lower()
        days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
        if day != 'all' and day not in days:
            print('Please enter a valid day name')
        else:
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
    # load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    #convert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from start time to create new columns
    df['month'] = df['start time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        #use the index of month index of the months list to get corresponding integer
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1

        #filter the month to create new DataFrame
        df = df[df['month'] == month]

    #filter by day of week if applicable
    if day != all:
        #filter by day of week to create the new DataFrame
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['months'].mode()[0] #return the number of months
    print('most common month:',calendar.month_name[common_month]) #using calendar for pulling month name from the number


    # display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour_freq

    common_hour = df['hour'].mode()[0]

    print('most common start hour:', common_hour)
    print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most commonly used Start Station:', common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most commonly used End Station:', common_end)

    # display most frequent combination of start station and end station trip
    common_start_end = (df['Start Stations'] + '-' + df['End Station']).mode()[0]
    print('The most frequent combination of start and end stations:' ,common_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time',total_time,'seconds, or',total_time/3600,'hours')


    # display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Total travel time',avg_time,'seconds, or',avg_time/3600,'hours')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
