#!/usr/bin/env python3

'''This is an idea I had to scrape websites and gather all of the anchor tags
from a given html page and make a python dictionary item with the key being the
scraped site and the value being a list object that was created from the anchor
tags gathered.'''
# project still in progress

# import the necessary module components
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from time import sleep
import ssl

# dictionary object for scraped anchor tags
site_scrape_tags = {}

# define the site scraper function
def soup_scrape():
    # while loop keeps the script going as long as the user doesn't opt to terminate
    while True:
        # if there is anything in 'site_scrape_tags', print the contents
        if len(site_scrape_tags.keys()) > 0:
            print(f'Here is the site\'s anchor tag array so far:\n{site_scrape_tags}\n')
        # ignore SSL cert errors when connecting to url
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        # ask for the user's input to establish what site will be scraped
        url = input('Please enter the address of the site you wish to scrape for anchor links.\n>> ')
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        links = []

        # retrieve anchor tags and loop through, adding each tag to our 'links' list object
        # and making sure to filter out the local files referenced in the site
        tags = soup('a')
        for tag in tags:
            if 'http' not in tag:
                continue
            links.append(tag.get('href', None))
        # url entered becomes the key and the list of anchor tags becomes the associated value
        site_scrape_tags[url] = links[:]
        links = []

        # ask for user input if they wish to terminate at this time
        question = input('Do you wish to continue running the script for other sites?(Y/N)\n>> ')
        question = question.upper()
        if question != 'Y':
            break
    #
    print('Alright, thanks for using me for all your web-scraping needs!\n')
    sleep(3)
    final = input('Would you like to print the final site tag array now?(Y/N)\n>> ')
    final = final.upper()
    if final == 'Y':
        print(f'Final site tag array:\n\n{site_scrape_tags}\n\n')
        return site_scrape_tags
    else:
        return site_scrape_tags

if __name__ == '__main__':
    tags = soup_scrape()
