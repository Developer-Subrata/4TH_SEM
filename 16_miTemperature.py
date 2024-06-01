import matplotlib.pyplot as plt
date = ["25/12", "26/12", "27/12"]
temp = [8.5, 10.5, 6.8]
plt.bar(date, temp, color='blue', label='Temperature')
plt.scatter(date, temp, color='red', label='Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variation')
plt.legend()
plt.show()