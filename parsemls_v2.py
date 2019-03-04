'''
Написать код программы для парсинга email-адресов с сайта. На входе файл с URL (URLs) для парсинга, на выходе csv-файл с емейлами.
'''

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
# import re


def write_csv(data):
    with open('emails.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data])


def kill_duplicates():
    df = pd.read_csv('emails.csv')
    df.drop_duplicates(subset=None, inplace=True)
    df.to_csv('emails.csv', index=False)



def get_html(url):
    r = requests.get(url)
    return r.text


def get_emails(html):
    soup = BeautifulSoup(html, 'lxml')
    clean_mails = []
    for i in soup.select("a[href^='mailto:']"):
        dirty_mails = []
        dirty_mails.append(i['href'])
        # print(dirty_mails)
        for mail in dirty_mails:
            dirty_mails = mail.split('?')
            demails = []
            demails.append(dirty_mails[0])
            for mail in demails:
                emails = []
                clean = mail.split(':')
                emails.append(clean[1])
                # print(emails)
                str_emails = ''.join(emails)
                print(str_emails)
                write_csv(str_emails)


    # emails = soup.find_all(text=re.compile('/@/'))
    # for i in emails:
    #     print(i.text)


def main():
    urls = []
    with open ('urls.txt', 'r') as file:
        for line in file:
            urls.append(line.rstrip())

    for url in urls:
        get_emails(get_html(url))

    kill_duplicates()


if __name__ == '__main__':
    main()
