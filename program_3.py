#Week 7, Program 3 - US_Population
#Caiden Heinrichs
#03/07/26


def sumPopulationForYear(dataList, year):
    totalPopulation = 0
    for data in dataList:
        if data[0] == year:
            totalPopulation += data[2]

    return totalPopulation


def main():
    dataList = []

    for i in range(3):
        #Creates a list to store data
        data = []

        #Collects data from user
        year = input("Enter year: ")
        state = input("Enter state: ")
        population = int(input("Enter population: "))

        #Updates list of data
        data.append(year)
        data.append(state)
        data.append(population)

        #Updates list of lists
        dataList.append(data)

    selectedYear = input("What year would you like to find the total population for? ")
    totalPopulationForSelectedYear = sumPopulationForYear(dataList, selectedYear)
    print(f'The total population for {selectedYear} is {totalPopulationForSelectedYear}.')


if __name__ == '__main__':
    main()
