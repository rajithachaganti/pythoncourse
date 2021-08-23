ride = input('select ride from Daily, Rental, Outstation:')
if ride in ['Daily', 'Rental', 'Outstation']:
    print('choose best ride')
else:
    print('redirecting to home page')
if ride == 'Daily':
    ride1 = input('select Daily ride from Auto, Sedan, SUV, Bike:')
    if ride1 == 'Auto':
        print('Rs10 for 1km')
    elif ride1 == 'Sedan':
        print('Rs15 for 1km')
    elif ride1 == 'SUV':
        print('Rs20 for 1km')
    elif ride1 == 'Bike':
        print('Rs25 for 1km')
    else:
        print('u have not selected ur ride')
elif ride == 'Rental':
    print('select rental type')
else:
    print('give outstation details')
