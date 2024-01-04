import pickle
import pandas as pd
import matplotlib.pyplot as plt
import csv

Pkl_Filename = "Pickle_RL_Model.pkl" 

with open(Pkl_Filename, 'rb') as file:  
    Pickled_LR_Model = pickle.load(file)

Pickled_LR_Model

def predictShowGraph(conference_name):

    with open(f'./conf_data/{conference_name}.csv','r') as csvinput:
        with open(f'./conf_data/predict_{conference_name}.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            
            row = next(reader)
            
            writer.writerow(['Name','Year','Gender'])
            
            for row in reader:
                name = row[0]
                year = row[1]
                gender = Pickled_LR_Model.predict([name])[0]
                writer.writerow([name,year,gender])


    df = pd.read_csv(f'./conf_data/predict_{conference_name}.csv')

    # drop duplicate lines
    df.drop_duplicates(subset=None, inplace=True)

    df1 = df.groupby(['Year', 'Gender']).size().reset_index(name='Counts')

    # separate the data into two dataframes based on gender
    df_female = df1[df1['Gender'] == 'F']
    df_male = df1[df1['Gender'] == 'M']

    # plot the data
    plt.plot(df_female['Year'], df_female['Counts'], label='Female', color='red')
    plt.plot(df_male['Year'], df_male['Counts'], label='Male', color='blue')

    # add the title and labels
    plt.title(f'Gender Counts by Year of {conference_name}')
    plt.xlabel('Year')
    plt.ylabel('Counts')

    # add the legend
    plt.legend()
    
    return plt