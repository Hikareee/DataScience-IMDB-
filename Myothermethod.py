from email.headerregistry import DateHeader
from bs4 import BeautifulSoup
import requests
import pandas as pd

season_no_list = []
episode_name_list = []
episode_airdate_list = []
episode_score_list = [] 
episode_votes_list = []
episode_description_list = []
episode_no_list = []


for season in range(3):
    season_no = season+1
    print("Season:", season_no)
    url = f'https://www.imdb.com/title/tt9335498/episodes?season={season_no}'
    response = requests.get(url)
    season_page = BeautifulSoup(response.content)
    episode_brackets = season_page.findAll('div', attrs={'class':'info'})
    
    for episode in episode_brackets:

        episode_name = episode.strong.a.text
        print("episode name: ", episode_name)
        episode_airdate = episode.find('div', attrs={'class': 'airdate'}).text.strip().replace(',','')
        print("airdate: ", episode_airdate)
        episode_score = episode.find(
            'span',  attrs={'class': 'ipl-rating-star__rating'}).text
        print("Score: ",episode_score)
        episode_votes = episode.find('span',  attrs={'class': 'ipl-rating-star__total-votes'}).text
        print("Vote Amounts: ",episode_votes)
        episode_description = episode.find('div', attrs = {'class':'item_description'}).text
        print("Episode Description: ", episode_description)
       
        season_no_list.append(season_no)
        episode_name_list.append(episode_name)
        episode_airdate_list.append(episode_airdate)
        episode_score_list.append(episode_score)
        episode_votes_list.append(episode_votes)
        episode_description_list.append(episode_description)
df = pd.DataFrame({
    'season_no': season_no_list,
    'episode_name': episode_name_list,
    'episode_airdate': episode_airdate_list,
    'episode_score': episode_score_list,
    'episode_votes':episode_votes_list,
    'episode_desc': episode_description_list
   })
df.to_csv('DemonSlayerEpisodesData.csv', index=False)
