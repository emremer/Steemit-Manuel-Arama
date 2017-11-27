########################################
## Ay isimlerini Kasim 2017 by Murat Tatar 
## Baglanti fonksiyonu: https://forum.ubuntu-tr.net/index.php?topic=37782.msg453829#msg453829
########################################



def TRbaglantiYap(metin):
    liste = {"ı": "i",
             "I": "i",
             "Ç": "c",
             "ç": "c",
             " ": "-",
             "ş": "s",
             "Ş": "s",
             "Ğ": "g",
             "ğ": "g",
             "Ü": "u",
             "ü": "u",
             "Ö": "o",
             "ö": "o"}

    metin = metin.encode('utf8', 'replace')
    for karakter in liste:
        metin = metin.replace(karakter, liste[karakter])
    return metin.lower()






def TurkceAy(ingAy):

    if   ingAy == "January": trAy=u"Ocak"
    elif ingAy == "February": trAy=u"Şubat"
    elif ingAy == "March": trAy=u"Mart"
    elif ingAy == "April": trAy=u"Nisan"
    elif ingAy == "May": trAy=u"Mayıs"
    elif ingAy == "June": trAy=u"Haziran"
    elif ingAy == "July": trAy=u"Temmuz"
    elif ingAy == "August": trAy=u"Ağustos"
    elif ingAy == "September": trAy=u"Eylül"
    elif ingAy == "October": trAy=u"Ekim"
    elif ingAy == "November": trAy=u"Kasım"
    elif ingAy == "December": trAy=u"Aralık"

    return trAy
