from bs4 import BeautifulSoup
import requests

with open('testsample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lmxl')
