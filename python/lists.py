cities = ['New York', 'Kyiv', 'Simferopol', 'Toronto']
print(cities)
print(len(cities))

print(cities[0])
print(cities[-2])
print(cities[2].upper())
cities.append('moscow')
print(cities[-1].upper())
cities.insert(2, 'Zurich')
print(cities)

del cities[-1]
print(cities)
cities.remove('Simferopol')
print(cities)

deleted_city = cities.pop()
print("Deleted city is: " + deleted_city)
print(cities)
cities.sort(reverse=True)
print(cities)

cities.reverse()
print(cities)
