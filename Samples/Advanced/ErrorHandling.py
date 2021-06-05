while True:
    try:
        age = int(input('what is your age? '))
        10/age
        #raise ValueError('manual')
        #raise Exception('manual')
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you')
        break
    finally:
        print('Try Again')
