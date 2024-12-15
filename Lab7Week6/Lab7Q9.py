#9. Make a word cloud. A word cloud is a visual representation for text data typically used to depict keyword metadata on websites, or to visualise free form text. An example is given below:


#The text of the HTML page is provided below:
#<!DOCTYPE html>
#<html>
#<head lang="en">
#<meta charset="UTF-8">
#<title>Tag Cloud Generator</title>
#</head>
#<body>
#<div style="text-align: center; width: 15%; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">
#** Your SPAN elements should be inserted here **
#</div>
#</body>
#</html>
#The format of a span element is
#<span style="font-size: XXpx"> WORD </span>
#where XX is the size in pixels and WORD is the word being represented.
#So for example, <span style="font-size: 20px"> our </span>
#The first part will be to read the story from the hare_and_tortoise.txt file in brightspace and populate a dictionary using each word as a key,
# and the value equals the frequency of the word. Your dictionary may look something like this:
#{'tortoise': 5, 'hare': 4, 'stopped': 2, …}
#For each word in the dictionary of frequencies you’ll need to write a SPAN tag to your HTML file. The font size will vary depending on the
# frequency of the word – for example if you use count*10 to calculate the words’ size, then words that appear once will be size 10px, words
# that appear twice 20px, etc.
#You should then create the completed HTML page and write it as a .html file. To manipulate html files just use the .html extension to write/read
#a file instead of the usual .txt. For instance: fo = open("output.html", "w"). You can open a html file to test it using a browser of your choice.
#Modify your program to exclude common words from showing in the cloud. You can get a file of stopwords (e.g. a, the, this, there, etc) in brightspace.

import string


def add_word(word, word_count_dict):
   """Update the word frequency: word is the key, frequency is the value"""
   if word in word_count_dict:
       word_count_dict[word] += 1
   else:
       word_count_dict[word] = 1

def process_line(line, word_count_dict):
   """Process the line to get lowercase words to add to the dictionary"""
   line = line.strip()
   word_list = line.split()
   for word in word_list:
       word = word.lower().strip()
       # get comas, periods, and other punctuation as well
       word = word.strip(string.punctuation)
       add_word(word, word_count_dict)


# Create dictionary of frequencies
word_count_dict = {}
file = open("hare_and_tortoise.txt", "r")
for line in file:
   process_line(line, word_count_dict)
print(word_count_dict)

# Create list of stopword
file = open("stopwords.txt", "r")
stopwords = []
for word in file:
    stopwords.append(word.strip())

# Create html file
html = """<!DOCTYPE html><html><head lang="en"><meta charset="UTF-8"><title>Tag Cloud Generator</title></head><body><div style="text-align: center; width: 10%; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">"""

for word, count in word_count_dict.items():
    if word not in stopwords:
        html += f'<span style="font-size: {count*2}px"> {word} </span>'

html += "</div></body></html>"

fo = open("output.html", "w")
fo.write(html)
fo.close()

#print(html, file=fo)





