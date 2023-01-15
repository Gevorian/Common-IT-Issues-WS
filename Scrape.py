import requests
from bs4 import BeautifulSoup
import csv

# list of IT news websites to scrape
websites = ['https://www.cio.com/category/technology/', 'https://www.techradar.com/news/', 'https://www.zdnet.com/topic/tech/']

# categories of IT-related issues
categories = ['Security', 'Artificial Intelligence', 'Cloud Computing', 'Big Data', 'IoT']

# dictionary to store the results
results = {}
for category in categories:
    results[category] = []

# function to categorize an article based on its content
def categorize_article(article):
    for category in categories:
        if category.lower() in article.lower():
            return category
    return 'Other'

# counter for number of requests
request_counter = 0

# loop through the websites
for website in websites:
    if request_counter > 500:
        print("Reached the request limit of 500 per page.")
        break
    try:
        # make a request to the website
        page = requests.get(website)
        request_counter += 1
        # parse the HTML content
        soup = BeautifulSoup(page.content, 'html.parser')
        # find all the articles on the website
        articles = soup.find_all('a')
        # loop through the articles
        for article in articles:
            article_text = article.text
            # categorize the article
            category = categorize_article(article_text)
            # add the article to the appropriate category in the results dictionary
            results[category].append(article_text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

# write the results to a CSV file
with open('it_issues.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    # write the header row
    writer.writerow(categories)
    # write the results
    for category in categories:
        writer.writerow(results[category])
