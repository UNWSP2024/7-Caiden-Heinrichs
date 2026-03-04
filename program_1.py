#Week 7, Program 1 - Rainfall
#Caiden Heinrichs
#03/07/26

#Returns all indexes of a list where a specified value is found
def searchList(list, value):
    matchingValues = []
    for i in range(len(list)):
        if list[i] == value:
            matchingValues.append(i)
    return matchingValues


def main():
    #Sets up a list of all months
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    #Sets up a list for collecting rainfall data
    monthlyRainfall = []

    #Collects rainfall data in "monthlyRainfall" list
    for month in range(12):
        monthlyRainfall.append(float(input(f'Enter the total rainfall (in.) for {months[month]}: ')))

    #Calculates total, average, min, and max rainfall for the year
    totalRainfall = round(sum(monthlyRainfall), 4)
    averageRainfall = round(totalRainfall / 12, 4)
    minRainfall = min(monthlyRainfall)
    maxRainfall = max(monthlyRainfall)
    #Finds the months with minimum and maximum rainfall
    minMonths = searchList(monthlyRainfall, minRainfall)
    maxMonths = searchList(monthlyRainfall, maxRainfall)
    #Prints total and average rainfall, and months with least and most rainfall
    print(f'Total rainfall for the year: {totalRainfall} in.')
    print(f'Average monthly rainfall for the year: {averageRainfall} in.')
    print(f'Month(s) with the least rainfall ({minRainfall} in.): {[months[i] for i in minMonths]}')
    print(f'Month(s) with the most rainfall ({maxRainfall} in.): {[months[i] for i in maxMonths]}')


if __name__ == "__main__":
    main()
