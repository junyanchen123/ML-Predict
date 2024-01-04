import requests
import csv
import os

orginal_name = 'conference.csv'
with open(orginal_name,'w',newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Name','Year'])
    
    cur = '*'
    
    while(cur):
        # get all data in a conference using cursor method
        response = requests.get(f'https://api.openalex.org/works?filter=host_venue.id:S4306417753&cursor={cur}')
        cur = response.json()['meta']['next_cursor']
        
        # for loop each work in the conference
        for obj in response.json()['results']:
            # for loop the information of each author
            for ele in obj['authorships']:
                name = ele['author']['display_name']
                year = obj['publication_year']
                writer.writerow([name,year])
            
    response = requests.get(f'https://api.openalex.org/works?filter=host_venue.id:S4306417753&cursor=*')
    conference_name = response.json()['results'][0]['host_venue']['display_name']       
    os.rename(orginal_name,f'{conference_name}.csv')