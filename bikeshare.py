"""
	Project: bikshare 
	Author: Ibrahim Saihati

"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
cago
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Chose one of the following cities: Chicago , New York City or Washington : ').lower()
    while city not in CITY_DATA:
        print("You Entered an Invalid City")
        city = input('Please Enter a Valide City. Chicago , New York City or Washington?: ').lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        print('Enter one of the following months or write all for all months\n january, february, march, april, may, june')
        month = input('\n Your choice: ').lower()
        if month in months or month =='all':
            break
        else:
            print("You have an invalid input, Try again")
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all' , 'monday', 'tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Enter a day (sunday-saturday) write all for all days\n Your Choice: ').lower()
    while day not in days:
        day=input('You Entered an Invalid Day, Tray again ').lower()

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
    #converting start time and end time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    #Making a new hour column.
    df['Hour'] = df['Start Time'].dt.hour
    #Making a new month column.
    df['Month'] = df['Start Time'].dt.month
    #Making a new day column.
    df['Day of week'] = df['Start Time'].dt.weekday_name  
    #filtering by month if applicable               
    if month != 'all':
        # use the index of the months list to get corresponding integer
        month = months.index(month) + 1
                  
        #filter by month to create new dataframe
        df = df[df['Month'] == month]
    
    
    #Filtering day.
    if day != 'all':
        # Filtering by day of week to create the new dataframe
        df = df[df['Day of week'] == day.title()]
 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # extract month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month
    # most common month
    popular_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most Popular Month:', months[popular_month-1])

    # TO DO: display the most common day of week
     
    # extract day of week 
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # most common day 
    popular_day = df['day_of_week'].mode()[0]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('Most Popular Day:', days[popular_day])

    # TO DO: display the most common start hour
    # extract hour from the Start Time 
    df['hour'] = df['Start Time'].dt.hour
    # most common hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Popular Start Station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most Popular End Station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print(pd.DataFrame(df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)).iloc[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Trip Duration:', df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print('Mean Trip Duration:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:    
        gender = df['Gender'].value_counts()
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest year of Birth:', df['Birth Year'].min())
        print('Most Recent year of Birth:', df['Birth Year'].max())
        print('Most Common year of Birth:', df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#Function to display the raw data if requestedd



#Function to display the raw data if requestedd
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame
    
    """
    request = ['yes', 'no']
    show_data = ''
   
    counter = 0
    while show_data not in request:       
        show_data = input('Do you want to view the raw data (yes,no)').lower()
        #the raw data 
        if show_data == "yes":
            print(df.head())
        elif show_data not in request:
            print("You Entered Invalid input")
             
    print('-'*40)


    
months=['january', 'february', 'march' , 'april', 'may', 'june']
def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

       
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
           

if __name__ == "__main__":
	main()
