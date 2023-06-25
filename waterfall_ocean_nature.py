#Motivational Speaking Tour Code

#importing necessary libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#setting up tour
tour_locations = ['New York', 'Los Angeles', 'Houston', 'Atlanta', 'Chicago', 'Miami', 'Dallas', 'Philadelphia']
tour_dates = ['April 14', 'April 16', 'April 20', 'April 22', 'April 28', 'April 30', 'May 4', 'May 6']

#creating a dataframe to keep track of tours
tour_df = pd.DataFrame({'Location': tour_locations, 'Date': tour_dates})

#setting up venue information
venue_info = {
    'New York': {'Capacity': 1000, 'Address': '123 Main Street'},
    'Los Angeles': {'Capacity': 500, 'Address': '456 Broadway'},
    'Houston': {'Capacity': 800, 'Address': '789 Main Street'},
    'Atlanta': {'Capacity': 600, 'Address': '111 Broadway'},
    'Chicago': {'Capacity': 400, 'Address': '333 Main Street'},
    'Miami': {'Capacity': 700, 'Address': '222 Broadway'},
    'Dallas': {'Capacity': 900, 'Address': '444 Main Street'},
    'Philadelphia': {'Capacity': 200, 'Address': '999 Broadway'}
}

#adding venue information to tour dataframe
for i in range(len(tour_df)):
    info = venue_info[tour_df.Location[i]]
    tour_df.at[i, 'Capacity'] = info['Capacity']
    tour_df.at[i, 'Address'] = info['Address']

#printing tour dataframe
print(tour_df)

#setting up ticket prices for each location
ticket_prices = {
    'New York': 100.00,
    'Los Angeles': 75.00,
    'Houston': 95.00,
    'Atlanta': 85.00,
    'Chicago': 75.00,
    'Miami': 90.00,
    'Dallas': 80.00,
    'Philadelphia': 75.00
}

#adding ticket prices to tour dataframe
for i in range(len(tour_df)):
    price = ticket_prices[tour_df.Location[i]]
    tour_df.at[i, 'Ticket Price'] = price

#printing tour dataframe
print(tour_df)

#creating dataset of attendees
attendee_names = ['Ryan', 'Gina', 'Jane', 'Mike', 'John', 'Karan', 'Carla', 'Sara']
ticket_purchases = [150, 100, 200, 50, 75, 250, 500, 2]
attendee_info = pd.DataFrame({'Name': attendee_names, 'Ticket Purchases': ticket_purchases})
attendee_info['Revenue'] = attendee_info['Ticket Purchases'] * ticket_prices[attendee_info.Name]

#printing attendee dataframe
print(attendee_info)

#creating plot of ticket purchases by city
sns.catplot(x='Location', y='Ticket Purchases', kind='bar', data=tour_df)
plt.title('Ticket Purchases by City')
plt.savefig('Ticket_Purchases_by_City.png')

#creating plot of revenue by city
sns.catplot(x='Location', y='Revenue', kind='bar', data=attendee_info)
plt.title('Revenue by City')
plt.savefig('Revenue_by_City.png')