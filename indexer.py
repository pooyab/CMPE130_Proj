import string
import re
from bs4 import BeautifulSoup
import urllib2


# RETURNS: string containing trimmed file
def trim_file(filename): # remove unecessary portions of files
    try:
        f = urllib2.urlopen(filename)
        lowercase = f.read().lower()
        lowercase = lowercase.translate(string.maketrans("",""), string.punctuation)
        lowercase = re.findall(r"[\w']+", lowercase)
        return lowercase
    except urllib2.URLError:
        return

# RETURNS: dictionary containing word frequencies
def count_freq(text): # count the frequency of keywords in a particular text file
    freq = dict()
    f = open("stopwords.txt", 'r')
    stopwords = f.read().split("\n")
    try:
        for word in text:
            if not freq.has_key(word):
                freq[word] = 1
            else:
                freq[word] += 1
        for key in freq.keys():
            if freq[key] == 0 or key in stopwords or key.isdigit():
                freq.pop(key, None)
    except TypeError:
        return
    print "frequency: ", freq
    return freq

# RETURNS: string containing trimmed query
def trim_query(query): # remove unimportant words in the query
    query = query.lower()
    query = query.split(" ")
    f = open("stopwords.txt", 'r')
    stopwords = f.read().split("\n")
    for word in query:
        if word in stopwords:
            query.remove(word)
    print "query: ", query
    return query

# RETURNS: integer containing compiled score
def score_query(query, freq): # compile a score based on the metadata collected on a file and a query provided by the user
    score = 0
    for word in query:
        try:
            score += freq[word]
        except KeyError:
            continue
    print "score: ",  score
    return score

# RETURNS: list containing links to each category page
def find_links(root):
    response = urllib2.urlopen(root)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        link_name = link.get('href')
        if ".html" not in link_name and "mailto" not in link_name:
            links.append("http://textfiles.com/" + link_name)
    return links

# RETURNS: list containing links to each text file with extension '.txt'
def get_textfiles(categories): # collect all the urls of the text files in the webpage; analogous to crawling a webpage and searching for links
    urls = []
    for category in categories:
        try:
            response = urllib2.urlopen(category)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a'):
                if ".txt" in link.get('href'):
                    urls.append(category + '/' + link.get('href'))
        except urllib2.URLError:
            print "???????????????????? TIMED OUT ????????????????????????????"
            continue
    return urls

links = find_links("http://textfiles.com/directory.html")
files = get_textfiles(links)
for file in files:
    print file
    score_query(trim_query("C Programming"), count_freq(trim_file(file)))
    print "\n########################################################################\n"
