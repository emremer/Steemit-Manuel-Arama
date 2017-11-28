# -*- coding: utf-8 -*-

#########################################################################
##    Steemit Manuel Search Tool v1 # by Murat Tatar # November 2017
#########################################################################


import re
import os
import time
import requests
import selenium
from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
from makelink import *

def e():
    exit()


#########################################################################

## Identifying variables

inTag = raw_input(u'In Tag?: ')
searchKey = raw_input(u'Search Key?: ')

#### Localize for non-English language
# inTag = inTag.decode('1254') 
# searchKey = searchKey.decode('1254')

inTag=MakeLink(inTag)


downTimes = raw_input(u'How many times, go down on the page?: ')
if downTimes =="": downTimes = 70
downTimes = int(downTimes)

#inTag = u'tr'
#searchKey = u'ethereum'
#downTimes = 30 # How many times, go down on the page. Bigger for more topSentences.




avatarSize = 60 #pixel 


title = u"For " + searchKey + u"' Search Results " + inTag + u" in tag on Steemit'"

topSentence = u"in <strong>"+ inTag +u"</strong> tag "

topSentence = topSentence + u'<h1>Posts with <span style="color:#14ab8a">**'+ searchKey +'**</span> in the title</h1><br><br>'




#################################################################


def Between(first,last,stringg):
    b1 = stringg.split(first)
    b2 = b1[1].split(last)
    ar = b2[0]
    return ar


#########################################################################
#####   TR etiketli içerikleri Bulma Kismi      #########################

page = web.Chrome("chromedriver.exe")


def Search():

    url = u'https://steemit.com/created/'+ inTag

    page.get(url)
    page.implicitly_wait(30)
    page.set_window_position(275,5)


    count = downTimes
    while count > 0:
        bodyElement = page.find_element_by_tag_name('html')
        bodyElement.send_keys(Keys.END) ; print "page end", count
        time.sleep(.97)
        count = count - 1


    content = bodyElement.get_attribute('innerHTML')

    part = Between('PostsList__summaries','</article>":',content)
    rows = re.findall('articles__summary(.*?)dropdown-arrow', part)

    print len(rows)




    ko = open('BlackList.txt','r'); BlackList = ko.read(); ko.close()

    tablo = '\n\n <table width="100%" border="0" cellpadding="6">'

    okPostCount = 0
    tablePostCount = 0
    for i in rows:

                tagLink = '<a href="/trending/'+inTag+'">'+inTag+'</a>'
                
                if tagLink in i:

                        okPostCount = okPostCount + 1
                        

                        author = Between('<a class="user__link" href="/','">',i)

                        if author in BlackList : continue

                        avatarPath = "https://img.busy.org/"+author+"?s="+str(avatarSize)

                        titleRaw = Between('<h2 class="articles__h2','<!-- /react-text -->',i)

                        titlePath = Between('<a href="/','">',titleRaw)

                        title = titleRaw.split(' -->'); title = title[1]

                        title = title.lower()

                        wanted = searchKey.lower()

                        #wanted Kelime title içinde geçiyor mu?
                        if not wanted in title: continue

                        tablePostCount = tablePostCount + 1

                        k = tablePostCount%2

                        if k==0: bg="#e8f8f9"
                        else: bg="#f9f3e9"
                        
                        
                        print okPostCount, "tr: ", author, title


                        tablo = tablo + '<tr bgcolor="'+bg+'">'

                        tablo = tablo + '<td style="padding:7px">' + '<a href="https://steemit.com/'+author +'/">' +'<img src="'+avatarPath+'">' + '</a>' +'<br>'+  '<a href="https://steemit.com/'+author+'/">' + author+ '</a>' + '</td>'
                        tablo = tablo + '<td style="padding:7px">' + '<a href="https://steemit.com/'+titlePath+'/">' +title+ '</a></td>'
                        
                        tablo = tablo + '</tr>'




    tablo = tablo + '</table>\n\n <br><br><br>-- \n\n ' 

    info = u'Blacklisted posts may not be listed.<br>\n\n'
    info = info + u'<div style="float:right;margin:10px">Steemit Manuel Search Tool, 2017 @murattatar</div><br>\n\n'
    #info = info + u'Daha fazla bilgiyi Discord üzerinden alabilirsiniz: https://discord.gg/BPPBq28 \n\n'
           

    topSentenceex = topSentence + unicode(tablo) + info

    
    


    if tablePostCount > 0 :

        html = u'<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'
        html = html + u'<title>'+ title + u'</title>'
        html = html + u'<style>a{color:#000} a:hover{color:#498f7e}</style><body style="font-family: tahoma; font-size: 16px; color: #151515; margin:75px">'
        html = html + topSentenceex
        html = html + u'</body></html>'

        

        ho=open("Search-Results.html","w"); ho.write(html.encode('utf8')); ho.close()

        os.startfile("Search-Results.html")

    else: print u"\n\n =====!Information!========== \n  Search did not return results"







############# ______Run_________ #############
 

Search()




    

