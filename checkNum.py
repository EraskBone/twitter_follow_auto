import json
import re
import requests
from typing import Dict

from bs4 import BeautifulSoup

class SocialMedias():

    @classmethod
    def get_statuses(cls) -> Dict:
        statuses = {}

        statuses['instagram'] = cls.__get_instagram_statuses('https://www.instagram.com/nyakuro/')
        statuses['twitter'] = cls.__get_twitter_statuses('https://twitter.com/nyakuro')
        return statuses

    @classmethod
    def __get_twitter_statuses(cls, url: str) -> Dict:
        statuses = {}

        # ToDo: error handling
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        # get follow count
        content = cls.__get_element_by_class(soup, 'ProfileNav-item--following')
        statuses['following_count']\
            = int(cls.__get_element_by_class(content, 'ProfileNav-value').string.replace(',', ''))

        # get follower count
        content = cls.__get_element_by_class(soup, 'ProfileNav-item--followers')
        statuses['follower_count']\
            = int(cls.__get_element_by_class(content, 'ProfileNav-value').string.replace(',', ''))

        return statuses


    @classmethod
    def __get_instagram_statuses(cls, url: str) -> Dict:
        statuses = {}

        # ToDo: error handling
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'lxml')
        js = soup.find("script", text=re.compile("window._sharedData")).text
        data = json.loads(js[js.find("{"):js.rfind("}")+1]);

        statuses['following_count'] = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']['count']
        statuses['follower_count'] = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count']

        return statuses


    @staticmethod
    def __get_element_by_class(soup: BeautifulSoup, class_name: str) -> BeautifulSoup:
        return soup.find(attrs={'class': re.compile('^' + class_name + '$')})


social_medias = SocialMedias()
print(social_medias.get_statuses())