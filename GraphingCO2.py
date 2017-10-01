# Mauna Loa CO2 graph

import matplotlib.pyplot as plt
import csv

x = []
y = []

file = open("co2.csv", "r")
iterator = 0
for line in file:
    iterator+=1
    if iterator == 1:
        pass
    else:
        all_data = line.split(',')
        year = float(all_data[1])
        co2_level = all_data[2]
        co2_level = co2_level[:-2]
        co2_level = float(co2_level)
        if co2_level<100:
            pass
        else:
            x.append(year)
            y.append(co2_level)

print(x)
print(y)

plt.plot(x, y, label='CO2 in micrograms')
plt.xlabel('Year')
plt.ylabel('CO2 Level')
plt.title('Mauna Loa CO2 Levels')
plt.legend()
plt.show()
