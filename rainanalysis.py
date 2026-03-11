import matplotlib.pyplot as plt
months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
rain = [120,127,110,98,75,79,80,85,89,79,85,89]
tot_rain = sum(rain)
avg_rain = tot_rain/len(rain)
print("Total Rainfall in the year: ", tot_rain, "mm")
plt.bar(months,rain)
plt.title("Montly Rainfall Analysis")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.show()