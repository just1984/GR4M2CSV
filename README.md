### GR4M Data Scraper
Overview The #GR4M Data Scraper is a Python script designed to extract specific information from social media posts on the #GR4M platform. It retrieves details such as the post date, content text, hashtags, likes, comments and the link to the post. The extracted data is then saved into a CSV file for further analysis or reporting.

## Features
- Extracts post details including date, content, hashtags, likes, comments, and image URLs.
- Reads URLs from a text file within the same directory.
- Saves the extracted data in CSV format.

## Requirements
- Python 3.x
- Libraries: requests, BeautifulSoup, pandas
    
## How to Run
Install Dependencies: Make sure to install the required libraries by running:

```bash
pip install requests
pip install beautifulsoup4
pip install pandas
```

Prepare URLs File: Create a text file named urls.txt in the same directory as the script Add the URLs of the #GR4M posts you want to scrape, one URL per line.

## Run the Script
Execute the script by running the following command in your terminal:
```bash
python gr4m_scraper.py
``` 
## Check the Output
The extracted data will be saved in a CSV file named gr4m_data.csv in the same directory as the script. You can open this file with any CSV reader to view the data.

## Note
Please ensure that you comply with the terms of service of the #GR4M platform when using this script. The script is intended for educational purposes and personal use only.
