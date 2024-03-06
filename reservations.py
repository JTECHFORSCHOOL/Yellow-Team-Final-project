from datetime import date, timedelta
from customer import C_ADD
import psycopg2

mycon = psycopg2.connect(database = 'rides', user = 'char')
mycursor = mycon.cursor()
mycursor.execute(""" CREATE TABLE users(
                 r_id SERIAL PRIMARY KEY,
                 pickup_location VARCHAR (50) NOT NULL,
                 destination_location VARCHAR (50) NOT NULL,
                 car_size VARHAR (3) NOT NULL
)""")

mycon = psycopg2.connect(database = 'users', user = 'char')
mycursor = mycon.cursor()

mycon.commit
mycursor.close()
mycon.close

def R_ADD():
    '''To make a new ride reservation'''
    mycon = psycopg2.connect(database = 'users', user = 'char')
    mycursor = mycon.cursor(buffered=True)

    mycursor = mycon.cursor()
    mycursor.execute ('Select r_id from rides order by length(r_id),r_id')
    cgen = mycursor.fetchall()
    if mycursor.rowcount:
        cgen = int(cgen[-1][0][1:])
        r_id = 'R' + str(cgen +1)
    else:
        r_id = 'R1'

    while True:
        ask_exisitng = input('Do you have an account with us? [y/n]: ').upper()
        if ask_exisitng in ('Y', 'N'):
            break
        else:
            print('Response entered is invalid. Please try again.')

        while True:
            c_id = input('Please enter your customer ID: ').upper()
            mycursor.execute("SELECT user_name from usere where c_id = '%s'" % c_id)
            rows = mycursor.fetchall()
            mycon.commit()
            mycon.close()
            for row in rows:
                print(row)
                a = mycursor.rowcount
                if a == 0:
                    print('Sorry, cutsomer does not exist.')
                else:
                    print('Please continue creating reservation.')
                    
                pickup_location = input('Please enter you current location: %s').upper()
                destination_location = input('Please enter your destination location: %s').upper()
                car_size = input('Please select the car size you would like [s/m/l]. Small cars seat 1, medium seat 4, and large seat up to 6: %s').upper()

            print("\nThese are the selections you have made for your current ride reservation:\n")

            mycursor.execute ("Select * from rides where pickup location = '%s' and destination location = '%s' and car size = '%s'") % (pickup_location, destination_location, car_size)
            mycursor.execute()
            mycursor.fetchall()

            mycursor = mycon
            mycursor.execute("INSERT INTO rides (r_id), (pickup_location), (destination_location), (car_size) VALUES ('%s', '%s', '%s')")

            mycon.commit()
            mycursor.close()
            mycon.close()
        
            print('\nYour ride has successfully been booked!')
            print('Your ride ID is ', r_id)
    
            return c_id

while True:
    Booking_respoonse = input('Do you wish to continue with this ride booking? [y/n]').upper()
    if Booking_respoonse not in ['Y', 'N']:
        print('Response entered is invalid. Please try again.')
    else:
        break
    if Booking_respoonse == 'Y':
        break

def R_UPDATE():
    '''To update ride details'''
    mycon = psycopg2.connect(database = 'rides', user = 'char')
    mycursor = mycon.cursor(buffered=True)

    R_id = input('Please enter your ride ID: ')

    mycursor = mycon.cursor()
    mycursor.execute("SELECT pickup_location, destination_location, car_size from rides where r_id = '%s'" % R_id)
    rows = mycursor.fetchall()
    mycon.commit()
    mycon.close()
    for row in rows:
        print(row)

    a = mycursor.rowcount

    if a == 0:
        print('Sorry, cutsomer does not exist.')
    else:
        data = data[0]
        pickup_location, destination_location, car_size = data

        while True:
            print()
            print('What ride information do you wish to change?')
            print('1. Pickup location')
            print('2. Destination location')
            print('3. Car size')
            print('4. Save Changes')

            while True:
                choice = input('Please select menu option: ')
                if len(choice) !=1 or not choice.isdigit() or choice not in "1234":
                    print('The option you have selected is not valid. Please try again.')
                else:
                    break

                if choice == "1":
                    while True:
                            pick_up_location = input('Please enter your new pickup location: %s').upper()
                            break
                elif choice == "2":
                    while True:
                            destination_location = input('Please enter your new destination location: %s').upper()
                            break
                elif choice == '3':
                    while True:
                            car_size = input('Please enter your new car size [s/m/l]: %s ').upper()
                            break

                mycursor = mycon.cursor()
                mycursor.execute("UPDATE rides SET pickup_location = '%s' WHERE r_id = '%s")
                mycursor.execute("UPDATE rides SET destination_location = '%s' WHERE r_id = '%s'")
                mycursor.execute("UPDATE users SET car_size = '%s' WHERE r_id = '%s")
                mycon.commit()
                mycon.close()

                print('Your ride has been updated.')
      
    def R_DELETE():
        '''To delete ride reservations'''
    mycon = psycopg2.connect(database = 'users', user = 'char')
    mycursor = mycon.cursor(buffered=True)

    R_id = input('Please enter your ride ID: ')

    mycursor = mycon.cursor()
    mycursor.execute("SELECT pickup_location, destination_location, car_size from rides where r_id = '%s'" % R_id)
    rows = mycursor.fetchall()
    mycon.commit()
    mycon.close()
    for row in rows:
        print(row)

        b = mycursor.rowcount

        if b == 0:
            print('Sorry, ride does not exist.')
        else:
            while True:
                c = input("Do you want to remove '%s' from system?: [Y/N] " %data[0][1]).upper()
                if c not in ('Y', 'N'):
                    mycon.commit()
                    print('The ride has successfully been deleted from the system.')

                    while True:
                        choice = input('Do you want to delete another ride? [Y/N]').upper()
                        if choice not in ('Y', 'N'):
                            print('Choice entered was invalid. Please try again.')
                            continue
                        break

                    if choice == 'N':
                        break

                mycursor = mycon.cursor()
                mycursor.execute("DELETE from rides WHERE r_id = '%s")
                mycon.commit()
                mycon.close()
