import requests
from bs4 import BeautifulSoup

f_handle = open("D:\\iTi-CloudArch\\Python\\file1.html",'r')
soup = BeautifulSoup(f_handle, "html.parser")
print (soup.text)
