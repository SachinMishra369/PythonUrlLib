import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# # url = input('Enter - ')
# html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html', context=ctx).read()
# # for line in html:
# #     print(line.decode().strip())

# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the anchor tags
# tags = soup('a')
# data=list()
# for tag in tags:
#   # data.append(tag.get('href', None))
#   # print(tag.get('href', None))
#   print('Contents:',tag.contents[0])


# print(data[2])
#  Code: http://www.py4e.com/code3/urllib1.py
# ----------------Assignemnt================

# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#     Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#     Actual data: http://py4e-data.dr-chuck.net/comments_724903.html (Sum ends with 14)


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
html = urlopen('http://py4e-data.dr-chuck.net/comments_724903.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
data=list()
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('span', None))
    # print('Contents:', tag.contents[0])
    data.append(int(tag.contents[0]))

    # print('Attrs:', tag.attrs)
print(sum(data))
