import requests # allows us to use HTTP requests! like axios/ajax

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20] #API response data JSON

for year in last_twenty_years:
    display_width = year["value"] // 10_000_000 # we can use underscores when dealing with large numbers to make them more readable
    print(f'{year["date"]}: {year["value"]}:', "=" * display_width) # this is what makes our silly little bar graph down below

