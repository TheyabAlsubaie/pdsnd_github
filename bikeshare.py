import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
genderAndBirthStat = False              
city = None
month = None
day = None
 
def displayData():
    """Displays 5 rows of data at a time until the user decides to stop."""
    global city
    startLocation = 0
    optionSelected = 'Yes'
    df = pd.read_csv(CITY_DATA[city])
    while True:
        if optionSelected == 'Yes':
            print(df.iloc[startLocation:startLocation + 5])  # Display 5 rows of data from the current index

        # Prompt the user to continue or stop
        choice = input("Would you like to see 5 more rows of data? Enter 1 - Yes or 2 - No: ")
        
        if choice == '1':
            startLocation += 5  # Move to the next set of 5 rows only if the user wants to continue
            optionSelected = 'Yes'
        elif choice == '2':
            print("Exiting data display. ")
            break
        else:
            print("Invalid input. Please enter 1 for Yes or 2 for No. ")
            optionSelected = None


def convertSeconds(seconds):
    """Converts time of seconds into a more readable format (days, hours, minutes, seconds)."""
    # Calculate how many days in variable "seconds"
    days = seconds // (24 * 60 * 60)        # 24 hours, 60 minutes, 60 seconds in a day.
    seconds %= 24 * 60 * 60                 # remove the calculated days from the time value
    
    # Calculate how many hours in variable "seconds"
    hours = seconds // ( 60 * 60)           # 60 minutes, 60 seconds in an hour
    seconds %= (60 * 60)                    # remove the calculated hours from the time value
    
    ## Calculate how many minutes in variable "seconds"
    minutes = seconds // 60                 #60 seconds in a minute
    seconds %= 60                           # remove the calculated minutes from the time value

    return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    global city, month, day, genderAndBirthStat
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        print("Choose a city by typing the corresponding number:")
        print("1 - Chicago")
        print("2 - New York City")
        print("3 - Washington")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            city = 'chicago'
            genderAndBirthStat = True
            break
            
        elif choice == '2':
            city = 'new york city'
            genderAndBirthStat = True
            break
            
        elif choice == '3':
            city = 'washington'
            break
            
        else:
            print("Invalid input. Please enter 1, 2, or 3. ")

    print(f"You selected: {city}\n")
    
    while True:
        print("Would you like to filter by Month, Day, or no filtering\nChoose the corresponding number:")
        print("1 - filter by month")
        print("2 - filter by day")
        print("3 - no filtering")
 

        choice = input("Enter your choice (1, 2, 3 for none): ")

        if choice == '1':
            filterType = 'Month'
            break
            
        elif choice == '2':
            filterType = 'Day'
            break
            
        elif choice == '3':
            filterType = 'none'
            break
            
        else:
            print("Invalid input. Please enter a number between 1 and 3. ")

    print(f"You selected: {filterType}\n")
    
    if filterType == 'Month':
    # get user input for month (all, january, february, ... , june)
        while True:
            print("Choose a month by typing the corresponding number:")
            print("1 - January")
            print("2 - February")
            print("3 - March")
            print("4 - April")
            print("5 - May")
            print("6 - June")
            print("7 - All")

            choice = input("Enter your choice (1, 2, 3, 4, 5, 6, or 7 for all): ")

            if choice == '1':
                month = 'January'
                break
                
            elif choice == '2':
                month = 'February'
                break
                
            elif choice == '3':
                month = 'March'
                break
                
            elif choice == '4':
                month = 'April'
                break
                
            elif choice == '5':
                month = 'May'
                break
                
            elif choice == '6':
                month = 'June'
                break
                
            elif choice == '7':
                month = 'all'
                break
                
            else:
                print("Invalid input. Please enter a number between 1 and 7. ")
                
        day = 'all'
        print(f"You selected: {month}\n")

    
    if filterType == 'Day':
    # get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            print("Choose a day by typing the corresponding number:")
            print("1 - Monday")
            print("2 - Tuesday")
            print("3 - Wednesday")
            print("4 - Thursday")
            print("5 - Friday")
            print("6 - Saturday")
            print("7 - Sunday")
            print("8 - All")

            choice = input("Enter your choice (1, 2, 3, 4, 5, 6, 7, or 8 for all): ")

            if choice == '1':
                day = 'Monday'
                break
                
            elif choice == '2':
                day = 'Tuesday'
                break
                
            elif choice == '3':
                day = 'Wednesday'
                break
                
            elif choice == '4':
                day = 'Thursday'
                break
                
            elif choice == '5':
                day = 'Friday'
                break
                
            elif choice == '6':
                day = 'Saturday'
                break
                
            elif choice == '7':
                day = 'Sunday'
                break
                
            elif choice == '8':
                day = 'all'
                break
                
            else:
                print("Invalid input. Please enter a number between 1 and 8.")
                
        month = 'all'
        print(f"You selected: {day}\n")
        

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
        # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df
    
    return #df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    startTime = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if month == 'all':
        df['month'] = df['Start Time'].dt.month
        mostCommonMonth = df['month'].mode()[0]
        mostCommonMonthName = calendar.month_name[mostCommonMonth]
        print("Most Common Month is:", mostCommonMonthName)

    # display the most common day of week
    if day == 'all':
        df['day_of_week'] = df['Start Time'].dt.weekday
        mostCommonDay = df['day_of_week'].mode()[0]
        mostCommonDayName = calendar.day_name[mostCommonDay]
        print("Most Common Day of the Week:", mostCommonDayName)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    mostCommonHour = df['hour'].mode()[0]
    print("Most Common Start Hour:", mostCommonHour)

    print("\nThis took %s seconds." % (time.time() - startTime))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    startTime = time.time()

    # display most commonly used start station
    mostCommonStartStation = df['Start Station'].mode()[0]
    print("Most Common Start Station:", mostCommonStartStation)

    # display most commonly used end station
    mostCommonEndStation = df['End Station'].mode()[0]
    print("Most Common End Station:", mostCommonEndStation)

    # display most frequent combination of start station and end station trip
    df['tripCombination'] = df['Start Station'] + " (TO) " + df['End Station']
    mostCommonTrip = df['tripCombination'].mode()[0]
    print("Most Common Trip combination from Start to End:", mostCommonTrip)

    print("\nThis took %s seconds." % (time.time() - startTime))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    startTime = time.time()

    # display total travel time
    totalTravelTime = df['Trip Duration'].sum()
    readableTotalTime = convertSeconds(totalTravelTime)
    print("Total Travel Time:", readableTotalTime)

    # display mean travel time
    averageTravelTime = df['Trip Duration'].mean()
    readableAverageTravelTime = convertSeconds(averageTravelTime)
    print("Average Travel Time:", readableAverageTravelTime)

    print("\nThis took %s seconds." % (time.time() - startTime))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    global genderAndBirthStat
    print('\nCalculating User Stats...\n')
    startTime = time.time()

    # Display counts of user types
    userTypes = df['User Type'].value_counts()
    print(userTypes)
    
    print()

    # Display counts of gender
    if genderAndBirthStat == True:
        genders = df['Gender'].value_counts()
        print(genders)
        print()

    # Display earliest, most recent, and most common year of birth
        earliestBirthYear = int(df['Birth Year'].min())
        print("Earliest Year of Birth:", earliestBirthYear)
        
        mostRecentBirthYear = int(df['Birth Year'].max())
        print("Most Recent Year of Birth:", mostRecentBirthYear)
        
        mostCommonBirthYear = int(df['Birth Year'].mode()[0])
        print("Most Common Year of Birth:", mostCommonBirthYear)

    print("\nThis took %s seconds." % (time.time() - startTime))
    print('-'*40)


def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            choice = input("Would you like to see 5 rows of data? type 1 - Yes or 2 - No: ")
            if choice == '1':
                displayData()
                break
            elif choice == '2':
                break
            else:
                print("Invalid input. Please type 1 or 2.")
        
        
        while True:
            choice = input("Would you like to see other statistics? Enter 1 - Yes, 2 - No: ")
            if choice == '1':
                restart = 'Yes'
                break
                
            elif choice == '2':
                restart = 'No'
                break
            
            else:
                print("Invalid input. Please type 1 or 2.")
            
        if restart == 'No':
            break


if __name__ == "__main__":
	main()
