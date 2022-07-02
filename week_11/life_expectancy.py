# Declare the general data
countries_data = []
initials_data = []
years_data = []
life_expectancies_data = []

# Open the file and setup the data
with open("life-expectancy.csv") as life_expectancy_dataset:
    next(life_expectancy_dataset)
    for line in life_expectancy_dataset:
        country, initial, year, life_expectancy_avg = line.strip().split(',')
        countries_data.append(country)
        initials_data.append(initial)
        years_data.append(int(year))
        life_expectancies_data.append(float(life_expectancy_avg))

# Receives an array and a value as parameters, returns a new array with the indexes
def keys_where(arr, search_value):
    new_array = []
    for i, value in enumerate(arr):
        if search_value == value:
            new_array.append(i)
    return new_array

# Returns the index and the max value in an array
def max_value_index(arr):
    max_index = 0;
    max_value = arr[0];

    for i, value in enumerate(arr):
        if value > max_value:
            max_value = value
            max_index = i

    return [ max_index, max_value ]

# Returns the index and the min value in an array
def min_value_index(arr):
    min_index = len(arr) - 1;
    min_value = arr[-1];

    for i, value in enumerate(arr):
        if value < min_value:
            min_value = value
            min_index = i

    return [ min_index, min_value ]

# Receives life_expectancies, countries and years, and returns and array with the max life expectancy
def get_max_life_expectancy(life_expectancies, countries, years):
    index, life_expectancy = max_value_index(life_expectancies)
    country = countries[index]
    year = years[index]

    return [ country, year, life_expectancy ]

# Receives life_expectancies, countries and years, and returns and array with the min life expectancy
def get_min_life_expectancy(life_expectancies, countries, years):
    index, life_expectancy = min_value_index(life_expectancies)
    country = countries[index]
    year = years[index]

    return [ country, year, life_expectancy ]


# Here we get the get the overall max and min values
overall_max_country, overall_max_year, overall_max_life_expectancy = get_max_life_expectancy(life_expectancies_data, countries_data, years_data)
overall_min_country, overall_min_year, overall_min_life_expectancy = get_min_life_expectancy(life_expectancies_data, countries_data, years_data)

# Ask the user for the year their want to search
try:
    searched_year = int(input("Enter the year of interest: "))
except:
    print("Please, enter a correct year.")
    quit()

# Get the filtered values
searched_year_indexes = keys_where(years_data, searched_year)
searched_life_expectancies = [ life_expectancies_data[i] for i in searched_year_indexes ]
searched_countries = [ countries_data[i] for i in searched_year_indexes ]
searched_years = [ years_data[i] for i in searched_year_indexes ]

searched_life_expectancies_average = sum(searched_life_expectancies) / len(searched_life_expectancies)

# Get the searched max and min values
searched_max_country, searched_max_year, searched_max_life_expectancy = get_max_life_expectancy(searched_life_expectancies, searched_countries, searched_years)
searched_min_country, searched_min_year, searched_min_life_expectancy = get_min_life_expectancy(searched_life_expectancies, searched_countries, searched_years)


# Print the results
print(f"\nThe overall max life expectancy is: {overall_max_life_expectancy} "
    f"from {overall_max_country} in {overall_max_year}")

print(f"The overall min life expectancy is: {overall_min_life_expectancy} "
    f"from {overall_min_country} in {overall_min_year}")

print(f"\nFor the year {searched_year}:")
print(f"The average life expectancy across all countries was {searched_life_expectancies_average:.2f}")
print(f"The max life expectancy was in {searched_max_country} with {searched_max_life_expectancy}")
print(f"The min life expectancy was in {searched_min_country} with {searched_min_life_expectancy}")



