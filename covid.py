import pandas as pd
import selenium 
import requests
from bs4 import BeautifulSoup 
from colorama import Fore, Back, Style
from colorama import init
import time
import threading
from pyfiglet import figlet_format
from termcolor import cprint

base_url = "https://www.worldometers.info/coronavirus/"
base_html = requests.get(base_url)
soup = BeautifulSoup(base_html.text,"lxml")

class covid():
    def get_most_corona_country(count):
        country = soup.find_all("a",class_="mt_a")
        country_name = country[count-1]
        for a in country_name:
           return a 
    def get_total_cases_of_country(name):
        new_country_url = f"https://www.worldometers.info/coronavirus/country/{name}/"
        country_html = requests.get(new_country_url)
        country_soup = BeautifulSoup(country_html.text,"lxml")
        corona_cases_html = country_soup.find_all("div",class_="maincounter-number")
        soup3  = BeautifulSoup(str(corona_cases_html),"lxml")
        stats = soup3.find_all("span")
        for cases in stats[0]:
            cases = cases
        for deaths in stats[1]:
            deaths = deaths
        for recovered in stats[2]:
            recovered = recovered
        all_stats = [cases,deaths,recovered]
        return all_stats
    def get_total_cases_of_world():
        corona_cases_html = soup.find_all("div",class_="maincounter-number")
        soup3  = BeautifulSoup(str(corona_cases_html),"lxml")
        stats = soup3.find_all("span")
        for cases in stats[0]:
            cases = cases
        for deaths in stats[1]:
            deaths = deaths
        for recovered in stats[2]:
            recovered = recovered
        all_stats = [cases,deaths,recovered]
        return all_stats


print(covid.get_total_cases_of_country("turkey")[0])
    
