import psycopg2

mycon = psycopg2.connect(database = 'users', user = 'char')
mycursor = mycon.cursor()
mycursor.execute(""" CREATE TABLE users(
                 c_id SERIAL PRIMARY KEY,
                 user_name VARCHAR (50) NOT NULL,
                 phone_number INTG (11) UNIQUE NOT NULL,
                 email VARCHAR (100) UNIQUE NOT NULL,
                 mailing_address VARCHAR (100) NOT NULL
)""")

mycon.commit
mycursor.close()
mycon.close


def C_ADD():
    ''' To add a customer to the users database'''
    mycon = psycopg2.connect(database = 'users', user = 'char')
    mycursor = mycon.cursor(buffered=True)

    mycursor = mycon.cursor()
    mycursor.execute ('Select c_id from users order by length(c_id),c_id')
    cgen = mycursor.fetchall()
    if mycursor.rowcount:
        cgen = int(cgen[-1][0][1:])
        c_id = 'C' + str(cgen +1)
    else:
        c_id = 'C1'

    user_name = input('Please enter your name: ').upper()
    mycursor.execute
    while True:
        try:
            phone_number = int(input('Please enter your phone number: '))
            if len(str(phone_number)) !=11:
                print('Error, number can only have 11 digits.')
                continue
            mycursor.execute ('Select * from users where phone_number = %d' % phone_number)
            mycursor.execute()
            if mycursor.rowcount:
                print('This phone number already exists in our system, please try again.')
                continue
        except:
            print('This phone number is invalid, please try again.')
            continue
        break
    while True:
        email = input('Please enter your email address: ').lower()
        mycursor.execute = ("Select * from users where email='%s" % email)
        mycursor.execute()
        mycursor.fetchall()
        if mycursor.rowcount:
            print('This email address already exisits in our system, please try again.')
            continue
        break
    mailing_address = input('Please enter your mailing address: ').upper()

    mycursor = mycon
    mycursor.execute("INSERT INTO users (c_id), (user_name), (phone_number), (email), (mailing_address) VALUES ('%s', '%s', %d, '%s', '%s', %d, '%s')")

    mycon.commit()
    mycursor.close()
    mycon.close()

    print('\nCustomer profile has been successfully added!')
    print('Your Customer ID is ', c_id)

    return c_id

def C_UPDATE():
    '''To update customer information in the users database'''
    mycon = psycopg2.connect(database = 'users', user = 'char')
    mycursor = mycon.cursor(buffered=True)

    c_id = input('Please enter your cusotmer ID: ')

    mycursor = mycon.cursor()
    mycursor.execute("SELECT user_name, phone_number, email, mailing_address from users where c_id = '%s'" % c_id)
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
        user_name, phone_number, email, mailing_address = data

        while True:
            print()
            print('What profile information do you wish to change?')
            print('1. Cell phone number')
            print('2. Email address')
            print('3. Mailing address')
            print('4. Cancel')

            while True:
                choice = input('Please select menu option: ')
                if len(choice) !=1 or not choice.isdigit() or choice not in "1234":
                    print('The option you have selected is not valid. Please try again.')
                else:
                    break

                if choice == "1":
                    while True:
                        try:
                            phone_number = int(input('Please enter your phone number: '))
                            if len(str(phone_number)) !=11:
                                print('Error, number can only have 11 digits.')
                                continue
                            mycursor.execute ('Select * from users where phone_number = %d' % phone_number)
                            mycursor.execute()
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
                        mycursor.execute = ("Select * from users where email='%s" % email)
                        mycursor.execute()
                        mycursor.fetchall()
                        if mycursor.rowcount:
                            print('This email address already exisits in our system, please try again.')
                        continue
                    break

                elif choice == '3':
                    address = input('Please enter your mailing address: ').upper()
                else:
                    break

                
                mycursor = mycon.cursor()
                mycursor.execute("UPDATE users SET phone_number = '%d' WHERE c_id = '%s")
                mycursor.execute("UPDATE users SET email = '%s' WHERE c_id = '%s'")
                mycursor.execute("UPDATE users SET mailing_address = '%s' WHERE c_id = '%s")
                mycon.commit()
                mycon.close()

                print('Your cusotmer profile has been updated.')

def C_DELETE():
        '''To delete cusotmers from the users data base'''
mycon = psycopg2.connect(database = 'users', user = 'char')
mycursor = mycon.cursor(buffered=True)

c_id = input('Please enter your cusotmer ID: ')

mycursor = mycon.cursor()
mycursor.execute("SELECT user_name, phone_number, email, mailing_address from usere where c_id = '%s'" % c_id)
rows = mycursor.fetchall()
mycon.commit()
mycon.close()
for row in rows:
        print(row)

        b = mycursor.rowcount

        if b == 0:
            print('Sorry, cutsomer does not exist.')
        else:
            while True:
                c = input("Do you want to remove '%s' from system?: [Y/N] ").upper()
                if c not in ('Y', 'N'):
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

                mycursor = mycon.cursor()
                mycursor.execute("DELETE from users WHERE c_id = '%s")
                mycon.commit()
                mycon.close()

def VIEWONE():
    '''To view the details of a specific customer'''
    mycon = psycopg2.connect(database = 'users', user = 'char')
    mycursor = mycon.cursor(buffered=True)

    c_id = input('Please enter your cusotmer ID: ')

    mycursor = mycon.cursor()
    mycursor.execute("SELECT user_name, phone_number, email, mailing_address from usere where c_id = '%s'" % c_id)
    rows = mycursor.fetchall()
    mycon.commit()
    mycon.close()
    for row in rows:
        print(row)
    mycon.close()