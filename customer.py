import mysql.connector

def ADD():
    ''' To add a customer to the customer table'''
    mycon = mysql.connector.connect(host='localhost', database= 'ride_bookings')
    mycursor = mycon.cursor(buffered=True)

    sql = 'Select c_id from customer order by length(c_id),c_id'
    mycursor.execute(sql)
    cgen = mycursor.fetchall()
    if mycursor.rowcount:
        cgen = int(cgen[-1][0][1:])
        c_id = 'C' + str(cgen +1)
    else:
        c_id = 'C1'

    name = input('Please enter your name: ').upper()
    while True:
        try:
            mob1 = int(input('Please enter your phone number: '))
            if len(str(mob1)) !=8:
                print('Error, number can only have 8 digits.')
                continue
            sql = 'Select * from customer where mobile_1 = %d' % mob1
            mycursor.execute(sql)
            if mycursor.rowcount:
                print('This phone number already exists in our system, please try again.')
                continue
        except:
            print('This phone number is invalid, please try again.')
            continue
        break
    while True:
        email = input('Please enter your email address: ').lower()
        sql = "select * from cusotmer where email='%s" % email
        mycursor.execute(sql)
        mycursor.fetchall()
        if mycursor.rowcount:
            print('This email address already exisits in our system, please try again.')
            continue
        break
    address = input('Please enter your mailing address: ').upper()

    data = (c_id, name, mob1, email, address, 0, 'I')
    sql = "insert into customer values ('%s', '%s', %d, '%s', '%s', %d, '%s')" % data

    mycursor.execute(sql)
    mycon.commit()
    mycon.close()

    print('\nCustomer profile has been successfully added!')
    print('Your Customer ID is ', c_id)

    return c_id

def UPDATE():
    '''To update customer details'''
    mycon = mysql.connector.connect(host='localhost', database= 'ride_bookings')
    mycursor = mycon.cursor(buffered=True)

    c_id = input('Please enter your cusotmer ID: ')

    sql = "select mobile_1, email, addree from customer where c_id = '%s'" % c_id

    mycursor.execute(sql)

    data = mycursor.fetchall()

    b = mycursor.rowcount

    if b == 0:
        print('Sorry, cutsomer does not exist.')
    else:
        data = data[0]
        mob1, email, address = data

        while True:
            print()
            print('What profile information do you wish to change?')
            print('1. Cell phone number')
            print('2. Email address')
            print('3. Mailing address')
            print('4. Save Changes')

            while True:
                choice = input('Please select menu option: ')
                if len(choice) !=1 or not choice.isdigit() or choice not in "1234":
                    print('The option you have selected is not valid. Please try again.')
                else:
                    break

                if choice == "1":
                    while True:
                        try:
                            mob1 = int(input('Please enter your phone number: '))
                            if len(str(mob1)) != 8:
                                raise Exception
                            sql = 'select * from customer where mobile_1 = %id' % mob1
                            mycursor.execute(sql)
                            mycursor.fetchall()
                            if mycursor.rowcount:
                                print('This phone number already exists in our system, please try again.')
                                continue
                        except:
                            print('This phone number is invalid, please try again.')
                            continue
                        break
                elif choice == "2":
                    while True:
                        email = input('Please enter your email address: ').lower()
                        sql = "select email from cusotmer where email='%s" % email
                        mycursor.execute(sql)
                        mycursor.fetchall()
                        if mycursor.rowcount:
                            print('This email address already exisits in our system, please try again.')
                            continue
                        break

                elif choice == '4':
                    address = input('Please enter your mailing address: ').upper()
                else:
                    break

                database = (mob1, email, address, c_id)
                sql = "UPDATE customer SET mobile_1 = %d, emial = '%s', address = '%s', WHERE c_id = '%s'" % database
                mycursor.execute(sql)
                mycon.commit()

                print('Your cusotmer profile has been updated.')

                mycon.close()

    def DELETE():
        '''To delete cusotmers from the table'''
    mycon = mysql.connector.connect(host='localhost', database= 'ride_bookings')
    mycursor = mycon.cursor(buffered=True)

    while True:
        c_id = input('Please enter your cusotmer ID: ').upper()

        sql = "select * from customer where c_id = '%s' " % c_id

        mycursor.execute(sql)

        data = mycursor.fetchall()

        h = mycursor.rowcount

        if h == 0:
            print('Sorry, cutsomer does not exist.')
        else:
            while True:
                a = input("Do you want to remove '%s' from system?: [Y/N] " %data[0][1]).upper()
                if a not in ('Y', 'N'):
                    mycon.commit()
                    print('The customer has successfully been deleted from the system.')

                    while True:
                        choice = input('Do you want to delete another cusotmer? [Y/N]').upper()
                        if choice not in ('Y', 'N'):
                            print('Choice entered was invalid. Please try again.')
                            continue
                        break

                    if choice == 'N':
                        break

                    mycon.close()

def VIEWONE():
    '''To view the details of a specific customer'''
    mycon = mysql.connector.connect(host='localhost', database= 'ride_bookings')
    mycursor = mycon.cursor(buffered=True)
    
    c_id = input('Please enter your customer ID: ').upper()
    sql = 'Select * from customer where c_id="%s"' % c_id
    mycursor.execute(sql)
    data = mycursor.fetchall()
    print()
    header = ['CUSTOMER ID', 'NAME', 'MOBILE NUMBER', 'EMAIL', 'ADDRESS', 'RESERVATION COUNT', 'STATUS']

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
        print('Customer ID entered is invalid. Please try again.')

        mycon.close()