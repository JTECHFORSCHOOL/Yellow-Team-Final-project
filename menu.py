import customer_related_functions, reservation_related_functions, ride_related_functions, payment_related_functions, rating_related_functions

print ("Welcome to zTrip!")
print ('\nTO exit the program at any point, hit CTRL + C')

while True:
    print('\nMenu')
    print('1. User Information')
    print('2. Booking')
    print('3. Ride Tracking')
    print('4. Payment')
    print('5. Ratings')

    while True:
        choice = input('Please select menu option: ')
        if not choice.isdigit() or len(choice) > 1 or choice not in '12345':
            print('The option you have selected is not valid. Please try again.')
        else:
            break
        
        if choice == '1':
            while True:
                print('n\1. Add new user')
                print('2. View user information')
                print('3. Update user information')
                print('4. Back')

        while True:
            choice = input('Please select menu option: ')
            if not choice.isdigit() or len(choice) > 1 or choice not in '12345':
                print('The option you have selected is not valid. Please try again.')
            else:
                break

            if choice == '1':
                customer_related_functions.ADD()
            elif choice == '2':
                customer_related_functions.VIEW()
            elif choice == '3':
                customer_related_functions.UPDATE()
            elif choice == '4':
                customer_related_fucntions.DELETE()
            else:
                break

        if choice == '2':
            while True:
                print('\n1. Create new reservation')
                print('2. View current reservation')
                print('3. Cancel reservation')
                print('4. Back')

        while True:
            choice = input('Please select menu option:')
            if not choice.isdighit() or len(choice) > 1 or choice not in '1234':
                    print('The option you have selected is not valid. Please try again.')
            else:
                break

            if choice == '1':
                reservation_related_functions.new_resveration()
            elif choice == '2':
                reservation_related_functions.viewall()
            elif choice == '3':
                reservation_related_functions.close_reservation()
            else:
                break
        
        if choice == '3':
            while True:
                print('\n.1 Add Ride')
                print('2. View Ride')
                print('3. Change Ride')
                print('4. Delete Ride')
                print('5. Back')
        while True:
            choice = input('Please select menu option:')
            if not choice.isdighit() or len(choice) > 1 or choice not in '1234':
                    print('The option you have selected is not valid. Please try again.')
            else:
                break

            if choice == '1':
                ride_related_functions.add_ride()
            elif choice == '2':
                ride_related_functions.view_ride()
            elif choice == '3':
                ride_related_functions.change_ride()
            elif choice == '4':
                ride_related_functions.delete_ride()
            else:
                break
        if choice == '4':
            while True:
                print('\n.1 Add Payement Method')
                print('2. View Payment Method')
                print('3. Change Method')
                print('4. Delete Payment Method')
                print('5. Back')
        while True:
            choice = input('Please select menu option:')
            if not choice.isdighit() or len(choice) > 1 or choice not in '1234':
                    print('The option you have selected is not valid. Please try again.')
            else:
                break

            if choice == '1':
                payment_related_functions.add_payment()
            elif choice == '2':
                payment_related_functions.view_payment()
            elif choice == '3':
                payment_related_functions.change_payment()
            elif choice == '4':
                payment_related_functions.delete_payment()
            else:
                break
        if choice == '5':
            while True:
                print('\n.1 Add Rating')
                print('2. View Rating')
                print('3. Back')
        while True:
            choice = input('Please select menu option:')
            if not choice.isdighit() or len(choice) > 1 or choice not in '1234':
                    print('The option you have selected is not valid. Please try again.')
            else:
                break

            if choice == '1':
                rating_related_functions.add_rating()
            elif choice == '2':
                rating_related_functions.view_rating()
            else:
                break
        else:
            print('\nProgram End')
            break

    print('Thank you for using our program, have a great day!')
