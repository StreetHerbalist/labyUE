import requests
import argparse

# Task 1
def greet(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"

# Task 2
def multiply_numbers(a: int, b: int) -> int:
    return a * b

# Task 3
def is_even(number: int) -> bool:
    return number % 2 == 0

# Task 4
def sum_greater_or_equal(a: int, b: int, c: int) -> bool:
    return a + b >= c

# Task 5
def value_in_list(lst: list, value: int) -> bool:
    return value in lst

# Task 6
def process_lists(list1: list, list2: list) -> list:
    result = list(set(list1 + list2))  # Combine and remove duplicates
    result = [x**3 for x in result]  # Cube each element
    return result

# Task 7
class Brewery:
    def __init__(self, name, city, state):
        self.name = name
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.name} in {self.city}, {self.state}"

def get_breweries(city=None):
    base_url = "https://api.openbrewerydb.org/breweries"
    params = {"per_page": 20, "by_city": city} if city else {"per_page": 20}

    response = requests.get(base_url, params=params)
    breweries_data = response.json() if response.status_code == 200 else []

    breweries_instances = [
        Brewery(name=brewery["name"], city=brewery["city"], state=brewery["state"])
        for brewery in breweries_data
    ]

    return breweries_instances

# Task 8
def main():
    parser = argparse.ArgumentParser(description="Get breweries information.")
    parser.add_argument("--city", help="Filter breweries by city.")
    args = parser.parse_args()

    breweries = get_breweries(city=args.city)
    for brewery in breweries:
        print(brewery)

if _name_ == "_main_":
    main()