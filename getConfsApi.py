import requests
import csv
import os
import predict_authorGender
    
cur = '*'
    
while(cur):
    
    response = requests.get('https://api.openalex.org/sources?filter=type:conference&per_page=200&cursor={}'.format(cur))
    cur = response.json()['meta']['next_cursor']
    
    for obj in response.json()['results']:
        
        orginal_name = './conf_data/conference.csv'
        with open(orginal_name,'w',newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow(['Name','Year'])
        
            conf_cur = '*'
            # a conference
            while(conf_cur):
            
                conf_info = requests.get(obj['works_api_url']+'&cursor={}'.format(conf_cur))
                conf_cur = conf_info.json()['meta']['next_cursor']
                
                for conf in conf_info.json()['results']:
                
                    for ele in conf['authorships']:
                        name = ele['author']['display_name']
                        year = conf['publication_year']
                        writer.writerow([name,year])
                        
        
        conference_name = obj['display_name']       
        os.rename(orginal_name,'./conf_data/{}.csv'.format(conference_name))
        graph = predict_authorGender.predictShowGraph(conference_name=conference_name)
        graph.savefig('static/{}.png'.format(conference_name))
        graph.clf()