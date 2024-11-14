import requests

# Function to fetch country data from the API
def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    
    if response.status_code != 200:
        print("Failed to retrieve data. Please check the country name.")
        return None

    country_data = response.json()
    return country_data

# Main function
def main():
    
    country_name = input("Enter the name of a country: ")

    
    user_input = str(country_name)

    
    is_input_provided = bool(user_input)

    
    if not is_input_provided:
        print("Country name is required. Exiting script.")
        return

    
    country_info = fetch_country_data(user_input)

    
    if country_info is None or len(country_info) == 0:
        print("No data found for the specified country.")
        return

    
    country = country_info[0]
    country_name = country.get("name", {}).get("common", "Unknown")
    population = country.get("population", "Unknown")
    capital = country.get("capital", ["Unknown"])[0]
    languages = country.get("languages", {})

    
    print(f"Country: {country_name}")
    print(f"Capital: {capital}")
    print(f"Population: {population}")

    
    print("Languages spoken:")
    for language_code, language in languages.items():
        print(f" - {language}")

    
    for i in range(3):
        print(f"Loop iteration {i + 1}: Example loop running")

    
    if "USA" in country_name.upper():
        print("You entered the United States of America.")

# Ensure the script runs only if executed directly
if __name__ == "__main__":
    main()
