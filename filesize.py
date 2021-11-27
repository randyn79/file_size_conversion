#!/usr/bin/env python3

def file_size_conversion(from_unit, from_value, to_unit):
    file_size_unit = { 'bytes': 0, 'kilobytes': 1, 'megabytes': 2,
                      'gigabytes': 3, 'terabytes': 4}
    
    steps = abs(file_size_unit[from_unit] - file_size_unit[to_unit])
    print(steps)

    if file_size_unit[from_unit] < file_size_unit[to_unit]:
        result = from_value / 1024 ** steps
        return result

    elif file_size_unit[from_unit] > file_size_unit[to_unit]:
        result = from_value * 1024 ** steps
        return result

    elif file_size_unit[from_unit] == file_size_unit[to_unit]:
        result = from_value
        return f'{result} no calculations made, unit specified is the same as unit to be converted'
    

    else:
        print('Invalid Input')

if __name__ == "__main__":
    
    while True:
        print("What unit are you converting from?")
        print("Available options are bytes, kilobytes, megabytes, gigabytes and terabytes")
        from_unit = input().casefold()
        if from_unit == 'b':
            from_unit = 'bytes'
            break
        elif from_unit == 'kb':
            from_unit = 'kilobytes'
            break
        elif from_unit == 'mb':
            from_unit = 'megabytes'
            break
        elif from_unit == 'gb':
            from_unit = 'gigabytes'
            break
        elif from_unit == 'tb':
            from_unit = 'terabytes'
            break
        else:
            print('Invalid Input!!!')
        
            
    print()
    while True:
        from_value = input(f'How many {from_unit} would you like to convert?').casefold()
        if from_value.isnumeric():
            from_value = float(from_value)
            break
        else:
            print('Invalid Input!!!')
            continue
    print()
    while True:
        to_unit = input('What unit are you converting to?').casefold()
        if to_unit == 'b':
            to_unit = 'bytes'
            break
        elif to_unit == 'kb':
            to_unit = 'kilobytes'
            break
        elif to_unit == 'mb':
            to_unit = 'megabytes'
            break
        elif to_unit == 'gb':
            to_unit = 'gigabytes'
            break
        elif to_unit == 'tb':
            to_unit = 'terabytes'
            break
        else:
            print('Invalid Input!!!')
        
    print()
    answer = file_size_conversion(from_unit, from_value, to_unit)
    print()
    print(f'{from_value} {from_unit}s is equivalent to {answer} {to_unit}')

   










