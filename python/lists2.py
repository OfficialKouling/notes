cars = ['bmw', 'lada', 'seat', 'skoda']

for car in cars:
    print(car.upper())

mynumber_list = list(range(0,10))
print(mynumber_list)

for x in mynumber_list:
    x = x * 2
    print(x)
print("Max number is: " + str(max(mynumber_list)))
print("Min number is: " + str(min(mynumber_list)))
print("Sum number is: " + str(sum(mynumber_list)))

mycars = cars[1:3]
print(mycars)
mycars = cars[:4]
print(mycars)
