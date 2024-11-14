import requests


def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    
    
    response = requests.get(url)
    
    
    if response.status_code != 200:
        print("Failed to retrieve data. Please check the country name.")
        return None
    
   
    data = response.json()
    
    
    return data[0]


def main():
    
    country_name = input("Enter the name of the country you want information about: ")
    
   
    user_country = str(country_name)  
    is_valid_country = bool(user_country) 
    
   
    if not is_valid_country:
        print("Country name is required. Exiting script.")
        return
    
    
    country_info = get_country_info(user_country)
    
   
    if country_info is None:
        return
    
    
    country_name = country_info.get("name", {}).get("common", "Unknown Country")
    capital = country_info.get("capital", ["No capital available"])[0]
    population = country_info.get("population", "Unknown population")
    languages = country_info.get("languages", {})

    
    print(f"Country: {country_name}")
    print(f"Capital: {capital}")
    print(f"Population: {population}")

    
    print("Languages spoken:")
    for code, language in languages.items():
        print(f" - {language}")
    
   
    for i in range(3):
        print(f"Loop iteration {i + 1}: This is a sample loop.")
    
   
    if capital:
        print(f"The capital of {country_name} is {capital}.")

# Ensure the script runs only if executed directly
if __name__ == "__main__":
    main()
