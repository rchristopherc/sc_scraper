from requests_html import HTMLSession
import json

session = HTMLSession()
r = session.get('https://playoverwatch.com/en-us/career/pc/equanimity-11303/')  # get page

def get_ranks():
    ranks = []
    rank = r.html.find('.competitive-rank-level')
    
    for elem in rank:
        ranks.append(int(elem.text))
        
    ranks = ranks[0:3] # there are 6 instances of competitive-rank-level, only need first 3
    return ranks


sr_list = get_ranks()
rank = {'tank':sr_list[0], 'dps':sr_list[1], 'support':sr_list[2]}

with open("ranks.json", "w") as f:
    json.dump(rank, f)
