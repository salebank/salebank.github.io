import requests

# Function to fetch country information from the REST Countries API
def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    
    # Make the API request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve data. Please check the country name.")
        return None
    
    # Parse the JSON response
    data = response.json()
    
    # Return the first result (assuming it’s the most relevant)
    return data[0]

# Main function
def main():
    # Get user input
    country_name = input("Enter the name of the country you want information about: ")
    
    # Variable examples
    user_country = str(country_name)  # String variable
    is_valid_country = bool(user_country)  # Boolean variable
    
    # If statement to check if input is valid
    if not is_valid_country:
        print("Country name is required. Exiting script.")
        return
    
    # Make the API call
    country_info = get_country_info(user_country)
    
    # Check if we received valid data
    if country_info is None:
        return
    
    # Parse information (dictionary parsing)
    country_name = country_info.get("name", {}).get("common", "Unknown Country")
    capital = country_info.get("capital", ["No capital available"])[0]
    population = country_info.get("population", "Unknown population")
    languages = country_info.get("languages", {})

    # Display country details
    print(f"Country: {country_name}")
    print(f"Capital: {capital}")
    print(f"Population: {population}")

    # Iterate over languages (list and dictionary parsing)
    print("Languages spoken:")
    for code, language in languages.items():
        print(f" - {language}")
    
    # Loop example: Print a message three times
    for i in range(3):
        print(f"Loop iteration {i + 1}: This is a sample loop.")
    
    # If statement example
    if capital:
        print(f"The capital of {country_name} is {capital}.")

# Ensure the script runs only if executed directly
if __name__ == "__main__":
    main()
