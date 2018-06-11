#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
poi_names_file = open('../final_project/poi_names.txt', 'r')


poi_in_file = list()
poi_cnt = 0

#for line in poi_names_file:
    #if line.startswith('(y)'):
#    poi_in_file.append(line[4:].upper().replace(', ', ' ').strip())

# for person in enron_data:
#    print enron_data[person]['email_address']
#     for poi in poi_in_file:
#         print poi
#         if person.startswith(poi):
#             poi_cnt += 1

print('Folk with quantified salary: ', len([p for p in enron_data if enron_data[p]['salary'] != 'NaN']))
print('Known email: ', len([p for p in enron_data if enron_data[p]['email_address'] != 'NaN']))

print('Percentage of folks without total payments: {0}%'.format(len([p for p in enron_data if enron_data[p]['total_payments'] == 'NaN']) * 100 / len(enron_data)))
print('Percentage of POIs without total payments: {0}%'.format(len([p for p in enron_data if enron_data[p]['poi'] and enron_data[p]['total_payments'] == 'NaN']) * 100 / len(enron_data)))
print('People in dataset: {0}'.format(len(enron_data)))
print('People without total payment: {0}'.format(len([p for p in enron_data if enron_data[p]['total_payments'] == 'NaN'])))
print('Number of POIs: {0}'.format(len([p for p in enron_data if enron_data[p]['poi']])))

# print(enron_data['SKILLING JEFFREY K']['total_payments'])
# print(enron_data['SKILLING JEFFREY K']['total_payments'])
# print(enron_data['LAY KENNETH S']['total_payments'])