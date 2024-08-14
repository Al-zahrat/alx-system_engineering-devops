#!/usr/bin/python3
from sys import argv
from requests import get
def number_of_subscribers(subreddit):
    head = {'User-Agent': 'ezzahraElidrissi'}
    count = get('https://www.reddit.com/r/{}/about.json'.format(
    subreddit), headers=head).json()
    try:
        return count.get('data').get('subscribers')
    except:
        return 0
if __name__ == "__main__":
    number_of_subscribers(argv[1])
