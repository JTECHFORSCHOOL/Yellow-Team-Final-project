from datetime import date, timedelta
import customer_related_functions
import reservation_related_functions
import mysql.connector

def VIEWONE():
    '''To view the details of a specific ride'''
    mycon = mysql.connector.connect(host='localhost', database= 'ride_bookings')
    mycursor = mycon.cursor(buffered=True)
    
    R_id = input('Please enter your ride ID: ').upper()
    sql = 'Select * from reservation where r_id="%s"' % R_id
    mycursor.execute(sql)
    data = mycursor.fetchall()
    print()
    header = ['PICKUP LOCATION', 'DESTINATION LOCATION', 'CAR SIZE', 'STATUS']

    if mycursor.rowcount:
        data = data[0]
        status = {'I' : 'Inactive', 'A' : 'Active'}
        for i in range(8):
            if i in (0, 1, 4, 5):
                print('{:^19s}:{:^50s}'.format(header[i], data[i]))
            elif i in (2, 3, 6):
                print('{:^19s}:{:^50d}'.format(header[i], data[i]))
            else:
                print('{:^19s}:{:^50s}'.format(header[i], status[data[i]]))
    else:
        print('Ride ID entered is invalid. Please try again.')

        mycon.close()