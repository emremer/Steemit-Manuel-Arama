# -*- coding: utf-8 -*-

#########################################################################
##    Steemit Manuel Arama Aparatı v1 # by Murat Tatar # Kasım 2017
#########################################################################


import re
import os
import time
import requests
import selenium
from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from turkceisler import *

def e():
    exit()


#########################################################################

## Degiskenleri tanimlama

bakilacakEtiket = raw_input(u'Bakılacak Etiket?: ')
arananKelime = raw_input(u'Aranacak Kelime?: ')

bakilacakEtiket = bakilacakEtiket.decode('1254') ; bakilacakEtiket=TRbaglantiYap(bakilacakEtiket)
arananKelime = arananKelime.decode('1254')


yogunluk = raw_input(u'Sayfada ne kadar aşağı inilsin?: ')
yogunluk ==""; yogunluk = 70
yogunluk = int(yogunluk)

#bakilacakEtiket = u'tr'
#arananKelime = u'ethereum'
#yogunluk = 30 # Sayfa sonu için END tuşuna basma sayısı. Yazı yoğunluğuna göre yükseltilmeli.




avatarBoyutu = 60 #pixel cinsinden en-boy


title = bakilacakEtiket + u" etiketindeki '" + arananKelime + u"' kelimesi Arama Sonuçları "

post = u"<strong>"+ bakilacakEtiket +u"</strong> etiketini <strong>ilk</strong> sırada kullanmış yazılar"
post = post +u"arasından\n <h1>başlığında **" + arananKelime + u"** geçen yazılar:</h1> <br><br>"


#################################################################


def Arasi(bas,son,cumle):
    b1 = cumle.split(bas)
    b2 = b1[1].split(son)
    ar = b2[0]
    return ar


#########################################################################
#####   TR etiketli içerikleri Bulma Kismi      #########################

sayfa = web.Chrome("chromedriver.exe")


def Arama():

    url = u'https://steemit.com/created/'+ bakilacakEtiket

    sayfa.get(url)
    sayfa.implicitly_wait(30)
    sayfa.set_window_position(275,5)


    say = yogunluk
    while say > 0:
        bodyElement = sayfa.find_element_by_tag_name('html')
        bodyElement.send_keys(Keys.END) ; print "sayfa sonu", say
        time.sleep(.97)
        say = say - 1


    gelen = bodyElement.get_attribute('innerHTML')

    arabolum = Arasi('PostsList__summaries','</article>":',gelen)
    satirlar = re.findall('articles__summary(.*?)dropdown-arrow', arabolum)

    print len(satirlar)




    ko = open('Karaliste.txt','r'); karaliste = ko.read(); ko.close()

    tablo = '\n\n <table width="100%" border="0" cellpadding="6">'

    uygunYaziSayisi = 0
    tablodakiYaziSayisi = 0
    tekcift = 0
    for i in satirlar:

                etiketLink = '<a href="/trending/'+bakilacakEtiket+'">'+bakilacakEtiket+'</a>'
                
                if etiketLink in i:

                        uygunYaziSayisi = uygunYaziSayisi + 1
                        

                        gonderen = Arasi('<a class="user__link" href="/','">',i)

                        if gonderen in karaliste : continue

                        avatarYol = "https://img.busy.org/"+gonderen+"?s="+str(avatarBoyutu)

                        baslikRaw = Arasi('<h2 class="articles__h2','<!-- /react-text -->',i)

                        baslikYol = Arasi('<a href="/','">',baslikRaw)

                        baslik = baslikRaw.split(' -->'); baslik = baslik[1]

                        baslik = baslik.lower()

                        aranan = arananKelime.lower()

                        #Aranan Kelime Baslik içinde geçiyor mu?
                        if not aranan in baslik: continue

                        tablodakiYaziSayisi = tablodakiYaziSayisi + 1

                        k = tablodakiYaziSayisi%2

                        if k==0: bg="#e8f8f9"
                        else: bg="#f9f3e9"
                        
                        
                        print uygunYaziSayisi, "tr: ", gonderen, baslik


                        tablo = tablo + '<tr bgcolor="'+bg+'">'

                        tablo = tablo + '<td style="padding:7px">' + '<a href="https://steemit.com/'+gonderen +'/">' +'<img src="'+avatarYol+'">' + '</a>' +'<br>'+  '<a href="https://steemit.com/'+gonderen+'/">' + gonderen+ '</a>' + '</td>'
                        tablo = tablo + '<td style="padding:7px">' + '<a href="https://steemit.com/'+baslikYol+'/">' +baslik+ '</a></td>'
                        
                        tablo = tablo + '</tr>'




    tablo = tablo + '</table>\n\n <br><br><br>-- \n\n ' 

    info = u'Karalisteye takılmış yazılar listenmemiş olabilir.<br>\n\n'
    info = info + u'<div style="float:right;margin:10px">Steemit Manuel Arama Aparatı, 2017 @murattatar</div><br>\n\n'
    #info = info + u'Daha fazla bilgiyi Discord üzerinden alabilirsiniz: https://discord.gg/BPPBq28 \n\n'
           

    postex = post + unicode(tablo) + info

    
    


    if tablodakiYaziSayisi > 0 :

        html = u'<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'
        html = html + u'<title>'+ title + u'</title>'
        html = html + u'<style>a{color:#000} a:hover{color:#498f7e}</style><body style="font-family: tahoma; font-size: 16px; color: #151515; margin:75px">'
        html = html + postex
        html = html + u'</body></html>'

        

        ho=open("arama-sonuclari.html","w"); ho.write(html.encode('utf8')); ho.close()

        os.startfile("arama-sonuclari.html")

    else: print u"\n\n =====!Açıklama!========== \n  Arama sonuç döndürmedi"







############# ______Çalıştır_________ #############
 

Arama()




    

