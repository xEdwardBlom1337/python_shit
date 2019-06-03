import requests
import re

users = {}

def add_users(number):
    r = requests.get('https://www.karmalb.com/ajax?key=totalkarma&offset=' + str(number))
    names = re.findall(r"^[^<>]+$", r.text, re.MULTILINE)[:-1]
    """ votes = []
    test = re.finditer(r"\>(\d{0,3},)?(\d{3},)?\d{0,3}\w{1}\<", r.text, re.MULTILINE)
    for match in test:
        votes.append(int(match.group()[1:-1].replace(",", ""))) """
    for i in range(10):
        users[names[i]] = 0 # votes[i]

for i in range(400):
    add_users(70000 + i * 10)

result = {}
for key, value in users.items():
    if key[0] == "T" and key[1] == "h":
        result[key] = value

print(result)




# 70000 - 74000
# ^[^<>]+$
# \>(\d{0,3},)?(\d{3},)?\d{0,3}\w{1}\<