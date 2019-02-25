# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
import scraperwiki
import lxml.html

#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
html = scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")
print(html)
#
# Find something on the page using css selectors
root = lxml.html.fromstring(html)
#Change "li p a" to a different CSS selector to grab something else
#Look for an a tag inside a p tag inside an li tag
#Store the matches in 'matchedlinks'
matchedlinks = root.cssselect("li p a")
#print that
print(matchedlinks)
#create a dictionary to store what we find
record = {}
#We start from 3416 beacuse 3417 rows were saved before error
'''
for li in matchedlinks[3416:]:
        #This next line is uncommented because it caused a problem
        #print(li.text_content())
        #This next line is the troubleshooted version
        print(li.text_content().encode('utf-8').strip())
        record['address'] = li.text_content()
        record['postcode'] = li.text_content().split(" ")[-2]+" "+li.text_content().split(" ")[-1]
        record['postcode district'] = li.text_content().split(" ")[-2]
        detaillink = "https://www.sdlauctions.co.uk"+li.attrib['href']
        record['link'] = detaillink
        #record['date'] = scrapedetail(detaillink)
        scraperwiki.sqlite.save(['address'],record, table_name='sdlauctions')
'''
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
'''
