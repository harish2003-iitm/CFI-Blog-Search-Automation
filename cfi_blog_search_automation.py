# -*- coding: utf-8 -*-
"""CFI Blog Search Automation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KfdcB1bWlNGpq68NM7Jhd8XN4JXaQcGK

Beautiful Soup
"""

import requests
from bs4 import BeautifulSoup

def search_cfi_blogs(search_query, tag_filter, club_filter):

    with requests.Session() as session:

        search_url = f"https://cfi.iitm.ac.in/blog"

        response = session.get(search_url)

        soup = BeautifulSoup(response.text, 'html.parser')

        blog_entries = soup.find_all('div', class_='card')

        matching_blogs = []
        for entry in blog_entries:

            title = entry.find('h5', class_='card-title').text

            tags = [tag.text.strip() for tag in entry.find_all('span', class_='badge')]

            club_name = entry.find('p', class_='card-text').text.strip()

            tag_matched = not tag_filter or any(tag in tags for tag in tag_filter)
            club_matched = not club_filter or club_name == club_filter

            if tag_matched and club_matched:
                blog_link = entry.find('a')['href']
                matching_blogs.append((title, blog_link))

        return matching_blogs

search_query = input("Enter the blog search query: ")
tag_filter_input = input("Enter tags to filter (comma-separated, leave empty for none): ")
tag_filter = [tag.strip() for tag in tag_filter_input.split(',') if tag.strip()]
club_filter = input("Enter the club filter (leave empty for none): ").strip()

matching_blogs = search_cfi_blogs(search_query, tag_filter, club_filter)

if matching_blogs:
    print("Matching blogs found:")
    for title, blog_link in matching_blogs:
        print(f"- {title}: https://cfi.iitm.ac.in{blog_link}")
else:
    print("No matching blogs found.")