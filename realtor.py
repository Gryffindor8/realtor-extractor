import csv
import sys

import requests
from bs4 import BeautifulSoup as bs

try:
    with open('data.csv') as csvfile:
        ader = csv.reader(csvfile)
        zip_code = ([x[0] for x in ader])
        print(zip_code)
except FileNotFoundError:
    with open("data.csv", "w") as my_empty_csv:
        pass
    print("please enter data in csv file!")
    sys.exit(0)
ind = 1
links = set()
for codes in zip_code:
    while True:
        print(ind)
        content = requests.get("https://www.realtor.com/realestateagents/{}/pg-{}".format(codes, ind)).content
        soup = bs(content, "html.parser")
        agent = (soup.find("div", {"id": "agent_list_wrapper"}))
        agent_link = (agent.find_all("div", {"class": "jsx-3970352998 agent-list-card-title-text clearfix"}))
        if len(agent_link) == 0:
            break
        for k in agent_link:
            ref_link = (k.find_all("a", href=True))
            for k1 in ref_link:
                links.add("https://www.realtor.com" + k1["href"])
        ind += 1
        # print(list(links))
print(len(links))
