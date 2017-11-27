# Steemit Manuel Arama Aparatý

Steemit arama için Google'ý kullanýyor. Ve bu her zaman saðlýklý sonuç vermiyor.
Steemit Manuel Arama Aparatý, son bir haftadaki tüm yazýlarýn baþlýklarýnda arama yapar.

---

### Kurulum

* https://www.python.org/downloads/ adresinden Ýþletim sistemize uygun Python 2.7+ indiriniz. 
(Tüm testler Python 2.7+ ile yapýlmýþtýr. Python 3.6+ daha yeni/daha iyidir diyerek onu indirdiðinizde çalýþma garantisi yoktur. 
Python 2.7 ve Python 3.6 ayrý derleyiciler olarak düþünün)

* Kurulum esnasýnda **Path** ve diðer kutucuklar **seçili halde** kurulum yapýnýz.

* Baþlat'a **cmd** yazýp enter'a basarak, konsolu açýnýz.

* [Resimdeki gibi](https://steemitimages.com/0x0/https://steemitimages.com/DQmeJUVjL7ykRt2NRXq3s6WfyPsLD8SYJgJRuQAmcsUrJB8/pip-install.jpg)
aþaðýdaki kütüphaneleri kurunuz.

pip install time

pip install re

pip install os

pip install requests

pip install selenium

pip install datetime


* https://sites.google.com/a/chromium.org/chromedriver/downloads adresinden ChromeWebDriver indirin. 
Zip içinden çýkararak, proje dosyalarýnýn olduðu klasöre çýkartýn. 

---

### Çalýþtýrma

10_Arama.py dosyasýný içindeki

<code>
bakilacakEtiket = u'tr' 

arananKelime = u'ethereum'
</code>

satýrlarýna, ilgili etiketi ve aramak istediðiniz kelimeyi girin.
