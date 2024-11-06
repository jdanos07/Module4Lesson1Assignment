import text_utils as tu

test_dummy = input('Provide a short blurb for manipulation: ')

manipulator = input('UPPER \nSwApcAsE \nTitle \nReverse \nGo ahead, pick one: ').lower()

if manipulator == 'Upper'.lower():
    tu.upper_str(test_dummy)
elif manipulator == 'SwApcAsE'.lower():
    tu.swapcase_str(test_dummy)
elif manipulator == 'Title'.lower():
    tu.title_str(test_dummy)
elif manipulator == 'Reverse':
    tu.reverse_str(test_dummy)
else:
    print('Unable to perform desired action.')