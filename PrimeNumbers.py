
counter = 2
while counter <= 100:
    if counter % 2 == 0:
        print(f'{counter} not a prime number.')
        counter += 1
    else:
        print(f'{counter} is a prime number.')
        counter += 1
print('Done')