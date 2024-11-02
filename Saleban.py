import requests

# fetch all countries
base_url ='https://restcountries.com/v3.1/all'


# fetch functions
def fetch_all_countries():
    response = requests.get(base_url)
    if response.status_code == 200 :
        country_names = []
        data = response.json()
        # Add your logic to fetch countries here
        for country in data:
            common_name = country['name']['common']
            country_names.append(common_name)
        print(country_names)
        print('Data retrieved')
    else:
        print(f'error in fetcing data, status code: {response.status_code}')

response1 = input('fetch all countries?, type "Y" for yes and "N" for No ').upper()

if response1 not in ["Y", "N"]:
    print("Invalid response. Please type 'Y' for yes or 'N' for no.")
    print('please restart script😢')
else:
    if response1 == "Y":
        print("Fetching all countries...")
        fetch_all_countries()
        
    else:
        print("Operation cancelled. Fetch any other time😁")


        
