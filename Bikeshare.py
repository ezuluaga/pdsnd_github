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

    while True:
        city = input("Please print name of city Washington, New York City, or Chicago: ").lower()
        if city not in CITY_DATA:
            print("Please try again not a valid answer")
            continue
        else:
            break
    while True:
        time = input("You can filter by month, day, all or none: ").lower()

        if time == 'month':
            month = input("Please print which month: January, Feburary, March, April, May or June?: ").lower()
            day = 'all'
            break

        elif time == 'day':
            day = input("Please print which day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?: ").lower()
            month = 'all'
            break

        elif time == 'all':
#            month = input("Which month? January, Feburary, March, April, May or June?: ").lower()
#            month = {'January', 'Feburary', 'March', 'April', 'May', 'June'}
            month = 'all'
#            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday: ").lower()
#            day = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
            day = 'all'
            break

        elif time == 'none':
            month = 'none'
            day = 'none'
            break

        else:
            input("Invalid input please provide month, day, all or none")
            break

    print(city)
    print(month)
    print(day)
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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name

    if month != 'all' and month != 'none':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all' and day != 'none':
        df = df[df['day_of_week'] == day]

    return df





def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()
    print(common_month)

    df['day_of_week'] = df['Start Time'].dt.week
    common_day_of_week = df['day_of_week'].mode()
    print(common_day_of_week)

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start = df['Start Station'].mode()
    print(common_start)


    common_end = df['End Station'].mode()
    print(common_end)


    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()
    print(common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel = df['Trip Duration'].sum()
    print(total_travel)

    mean_travel = df['Trip Duration'].mean()
    print(mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(user_types)

    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("There is no gender information in this city.")


    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print(earliest)
        recent = df['Birth_Year'].max()
        print(recent)
        common_birth = df['Birth Year'].mode()[0]
        print(common_birth)

    else:
        print("There is no birth year information in this city.")

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
