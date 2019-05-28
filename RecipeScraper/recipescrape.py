#!/usr/bin/env python

"""
Comments
Author: TylerR
Purpose: To scrape recipes from desired webpage and collect them into a .csv file
"""

# import libraries needed
import csv
import requests
from bs4 import BeautifulSoup

# Collect the URL and Parse the webpage from here
page = requests.get('https://cookieandkate.com/category/food-recipes/entrees/')


# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Remove bottom Links Clean up
# last_links = soup.find(class_='div a')
# last_links.decompose()

# Create a file to write to, add header rows
# file = csv.writer(open('RecipeScrape.csv', 'w'))
# file.writerow(['Name', 'Link'])


# Pull all links from class lcp_catlist_item
food_list = soup.find(class_='lcp_catlist')

# Pull text from all instances of <a> tag within lcp_catlist div
food_list_items = food_list.find_all('a')

# Create for loop to iterate food_list and print out all food recipe links

for food_list in food_list_items:
    print(food_list.prettify())


    # Add each food lists name and link to a row
    # file.writerow([food_list])