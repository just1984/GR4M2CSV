import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def extract_XXX_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    meta_description = soup.find('meta', attrs={'property': 'og:description'})['content']
    meta_title = soup.find('meta', attrs={'property': 'og:title'})['content']
    date_string = meta_description.split(" on ")[1].split(":")[0]
    date_formatted = datetime.strptime(date_string, '%B %d, %Y').strftime('%Y-%m-%d')
    likes = meta_description.split(" likes, ")[0]
    comments = meta_description.split(" likes, ")[1].split(" comments")[0]
    content = meta_title.split("on XXX:")[1].split("#")[0].replace('\n', ' ').strip()
    hashtags = " ".join([tag for tag in meta_title.split() if tag.startswith("#")])
    return date_formatted, content, hashtags, likes, comments, url


with open('urls.txt', 'r', encoding='utf-8-sig') as file:
    urls = [line.strip() for line in file.readlines()]

data = {
    "Datum": [],
    "Inhalt": [],
    "Keywords": [],
    "Likes": [],
    "Kommentare": [],
    "Link": []
}

for url in urls:
    date, content, keywords, likes, comments, link = extract_XXX_data(url)
    data["Datum"].append(date)
    data["Inhalt"].append(content)
    data["Keywords"].append(keywords)
    data["Likes"].append(likes)
    data["Kommentare"].append(comments)
    data["Link"].append(link)

df = pd.DataFrame(data)

file_path = 'gr4m_data.csv'
df.to_csv(file_path, index=False)

print(f"Data extracted and saved to '{file_path}'")
