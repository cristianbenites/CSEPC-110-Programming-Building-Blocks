class LifeExpectancies:
    def __init__(self) -> None:
        self.countries = []
        self.initials = []
        self.years = []
        self.life_expectancies = []
        self.system_is_running = True
    
    def add_new_data(self, filepath):
        with open(filepath) as life_expectancy_dataset:
            next(life_expectancy_dataset)
            for line in life_expectancy_dataset:
                country, initial, year, life_expectancy_avg = line.strip().split(',')
                self.countries.append(country)
                self.initials.append(initial)
                self.years.append(int(year))
                self.life_expectancies.append(float(life_expectancy_avg))

    def keys_where(self, arr, search_value):
        new_array = []

        for i, value in enumerate(arr):
            if search_value == value:
                new_array.append(i)
        return new_array

    def max_value_index(self, arr):
        max_index = 0;
        max_value = arr[0];

        for i, value in enumerate(arr):
            if value > max_value:
                max_value = value
                max_index = i

        return [ max_index, max_value ]

    def min_value_index(self, arr):
        min_index = len(arr) - 1;
        min_value = arr[-1];

        for i, value in enumerate(arr):
            if value < min_value:
                min_value = value
                min_index = i

        return [ min_index, min_value ]


    def get_max_life_expectancy(self, life_expectancies, countries, years):
        index, life_expectancy = self.max_value_index(life_expectancies)
        country = countries[index]
        year = years[index]

        return [ country, year, life_expectancy ]

    def get_min_life_expectancy(self, life_expectancies, countries, years):
        index, life_expectancy = self.min_value_index(life_expectancies)
        country = countries[index]
        year = years[index]

        return [ country, year, life_expectancy ]

    def show_overall_data(self):
        max_country, max_year, max_life_expectancy = self.get_max_life_expectancy(self.life_expectancies, self.countries, self.years)
        min_country, min_year, min_life_expectancy = self.get_min_life_expectancy(self.life_expectancies, self.countries, self.years)

        print(
            f"\nThe overall max life expectancy is: {max_life_expectancy} "
            f"from {max_country} in {max_year}")
        print(
            f"The overall min life expectancy is: {min_life_expectancy} "
            f"from {min_country} in {min_year}")
    
    def get_menu_action(self):
        print("\nSelect one of the following:\n"
            "1. Show by year of interest\n"
            "2. Search by country\n"
            "3. Quit\n")
        return input("Please, enter an action: ")

    def search_by_year(self):
        try:
            searched_year = int(input("Enter the year of interest: "))
        except:
            print("Please, enter a correct year.")
            return

        indexes = self.keys_where(self.years, searched_year)

        if len(indexes) == 0:
            print("No year was found.\n\n")
            return

        life_expectancies = [ self.life_expectancies[i] for i in indexes ]
        countries = [ self.countries[i] for i in indexes ]
        years = [ self.years[i] for i in indexes ]

        life_expectancy_avg = sum(life_expectancies) / len(life_expectancies)

        max_country, _, max_life_expectancy = self.get_max_life_expectancy(life_expectancies, countries, years)
        min_country, _, min_life_expectancy = self.get_min_life_expectancy(life_expectancies, countries, years)

        print(f"\nFor the year {searched_year}:")
        print(f"The average life expectancy across all countries was {life_expectancy_avg:.2f}")
        print(f"The max life expectancy was in {max_country} with {max_life_expectancy}")
        print(f"The min life expectancy was in {min_country} with {min_life_expectancy}")

    def search_by_country(self):
        searched_country = input("Enter the country name: ")
        searched_country = searched_country.capitalize()

        indexes = self.keys_where(self.countries, searched_country)

        if len(indexes) == 0:
            print("No country with this name was found.\n\n")
            return

        life_expectancies = [ self.life_expectancies[i] for i in indexes ]
        countries = [ self.countries[i] for i in indexes ]
        years = [ self.years[i] for i in indexes ]

        life_expectancy_avg = sum(life_expectancies) / len(life_expectancies)

        _, max_year, max_life_expectancy = self.get_max_life_expectancy(life_expectancies, countries, years)
        _, min_year, min_life_expectancy = self.get_min_life_expectancy(life_expectancies, countries, years)

        print(f"\nFor {searched_country}:")
        print(f"The average life expectancy was {life_expectancy_avg:.2f}")
        print(f"The max life expectancy was in {max_year} with {max_life_expectancy}")
        print(f"The min life expectancy was in {min_year} with {min_life_expectancy}")

    def quit(self):
        print("Thank you. Goodbye.")
        self.system_is_running = False

    def run_next_step(self, action):
        match action:
            case "1":
                return self.search_by_year()
            case "2":
                return self.search_by_country()
            case "3":
                return self.quit()
            case _:
                print("Invalid option.")

    def run(self):
        filepath = input("Insert the path to the dataset: ")
        self.add_new_data(filepath)

        self.show_overall_data()

        while(self.system_is_running):
            action = self.get_menu_action()
            self.run_next_step(action)

data_analizer = LifeExpectancies()
data_analizer.run()
