import requests
import numpy as np
import csv
from bs4 import BeautifulSoup



for x in range(20):
    URL = 'https://footyforecaster.com/NRL/Ladder/2020_Round_'
    round = str(x + 1)

    URL += round
    print(URL)

    file = 'ladder_round_'+round
    file += '.csv'
    print(file)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_='bigpadding')
    results = soup.find("tbody")

    headers = ['Position', 'Team', 'M', 'W', 'D', 'L', 'B', 'For', 'Agst', 'Diff', 'Points']
    big_array = []
    num_cols = 11
    num_Teams = 16

    # create 2d list 16x11
    ladder = [[0 for x in range(num_cols)] for i in range(num_Teams)]


    # convert results to an array of stripped_strings
    for string in results.stripped_strings:
        big_array.append(string)

    # start at 0 0 for ladder
    x = 0
    y = 0
    # convert mini array into 2d array
    for i, element in enumerate(big_array):

        # split array every 11 entries - separates rows on the ladder
        if i > 0 and i % 11 == 0:
            y += 1
            x = 0
        ladder[y][x] = element
        x += 1


    print(ladder)
    with open(file, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(ladder)


