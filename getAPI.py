import requests
import csv


with open('author.csv','w',newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Name','Year'])
    
    cur = '*'
    
    while(cur):
        response = requests.get(f'https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I97018004,publication_year:2010-2020&sort=publication_date:desc&per_page=200&cursor={cur}')
        cur = response.json()['meta']['next_cursor']

        for obj in response.json()['results']:
            name = obj['authorships'][0]['author']['display_name']
            year = obj['publication_year']
            writer.writerow([name,year])