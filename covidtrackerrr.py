'''
-------------------------------------------------------------------------------
                            TRACKORONA (LEVEL 2)
BY : Vishal Das ( CSE 2)  , HARSHIT SHARMA.. ( CSE 3 ) , Gumutch Mishra ( CSE 1 )
-------------------------------------------------------------------------------
'''

# importing the necessary modules
# Plyer module is used to access the features of the hardware and its Notification submodule
# helps to creates a pop up desktop notification
from plyer import notification

# Beautiful Soup is a Python library for pulling data out of HTML and XML files.
# it creates a soup object which internally parses the html / xml codes as
# parse trees and via this object , we can process the website data with ease
from bs4 import BeautifulSoup as bs

# time module syncs with system time and helps perform time manipulating tasks
import time

# requests module again helps us to access data out of  html / xml files
import requests

# Func to Generate Notification using plyer Module's Notification Construct
while True:
    def notify_me(title, message):
        notification.notify(
            title=title,
            message=message,
            app_icon="C:/Users/OK/PycharmProjects/TRACKORONA PROJECT/covid_icon_2_FMC_icon.ico" ,
            timeout=10
        )


    try:
        # Func to get url
        def getdata(url):
            r = requests.get(url)
            return r.text
            # WEB SCRAPPING :
            # accessing website data via soup object and
            # feeding the data as msg to our Notification
            # A string corresponds to a bit of text "within a html tag" , and
            # The split() method splits a string into a list. You can specify the separator,
            # default separator is any whitespace.
            # Beautiful Soup converts html doc into a tree data structure and parses it

            # Sending http Requests


        htmldata = getdata("https://covid-19tracker.milkeninstitute.org/")
        html = getdata("https://www.worldometers.info/coronavirus/country/india")
        html_gov = getdata("https://www.mohfw.gov.in/")

        # creation of soup objects for Web Scrapping
        soup1 = bs(htmldata, "html.parser")
        soup2 = bs(html, "html.parser")
        soup3 = bs(html_gov, "html.parser")

        # WEB SCRAPPING : to find Vaccine Names

        # Some Prints to Check the location in result str containing the Vaccine Names
        # print (result[46:86])
        # printing vaccine names to the console
        # WEB SCRAPPING : to find the No. of Deaths and New Cases
        cases = list(soup2.find("li", {"class": "news_li"}))[0].text.split()[0]
        deaths = list(soup2.find("li", {"class": "news_li"}))[2].text.split()[0]
        # print (deaths )

        # WEB SCRAPPING : to fetch total and recovered cases and recovery %
        tot_cases = list(soup2.find("div", {"class": "maincounter-number"}))[1].text.split()[0]
        tot_recovery = list(soup2.find_all("div", {"class": "maincounter-number"}))[2].text.split()[0]
        # computation of Recovery %
        t1 = float(tot_cases.replace(",", ""))
        t2 = float(tot_recovery.replace(",", ""))
        recovered = t2 * 100 / t1
        # to set the precision as 2 decimal places
        recovered = "{:.2f}".format(recovered)
        # print(type(rec1))

        # Recovery % can also be compute by converting the str data to NUMERICAL VALUE AS :
        # n1=[]
        # i=0
        # rec_num=0
        # for n in recovered:
        #     if n!= ',':
        #        n1.append(int(n))
        # len_rec=(int(len(n1)))
        # len_itration=(len_rec)
        # while i<len_itration:
        #     len_rec -= 1
        #     rec_num+=pow(10,(len_rec))*n1[i]
        #     i+=1

        # WEB SCRAPPING : To find total deaths and Tested Cases in last 24 hrs
        testing_last_24_hour = (soup3.find("span", {"class": "tested"})).text[51:]
        total_death = (soup3.find_all("strong", {"class": "mob-hide"}))[5].text[:6]

        # Converting String into Integer using replace ()
        tdeath = int(total_death.replace(",", " "))
        # print(tdeath)
        ttesting = int(testing_last_24_hour.replace(",", ""))
        case_num = int(cases.replace(",", ""))

        # percentage of total death and new cases (based on daily new cases and cases Tested in Last 24 hrs
        tdeath_per = (tdeath * 100) / t1
        tdeath_per = "{:.2f}".format(tdeath_per)
        new_case_per = (case_num * 100) / ttesting
        new_case_per = "{:.2f}".format(new_case_per)

        # this is a small exception handled : if no deaths are recorded then the string 'India'
        # dynamically comes to index of the list so scrapped ,containing the number of deaths
        # so notified msg will display " NO NEW CASE "
        # list( printed to find the exception ) = [<strong>655 new cases</strong>, ' in ',
        # <strong><a href="/coronavirus/country/india/" style="text-decoration: underline;">India</a></strong>
        # , '\xa0', <span class="source">[<a class="news_source_a" href="https://www.mohfw.gov.in/"
        # target="_blank">source</a>]</span>, '\xa0', <span class="source">[<a class="news_source_a"
        if deaths == 'India':
            deaths = 'NO NEW CASE'

        # Creation of Msgs
        msg1 = " New Cases - " + cases + "\nNew Deaths - " + deaths + "\nTotal Cases - " + tot_cases + "\nRecovered Cases - " + tot_recovery
        msg2 = " RECOVERIES - " + str(recovered) + " % " + "\nDEATHS - " + str(
            tdeath_per) + " % " + "\nNEW CASES - " + str(new_case_per) + " % "
        notify_me("INDIA\nCOVID - 19 UPDATES", msg1)
        notify_me("INDIA\nCOVID-19 STATISTICS", msg2)
        time.sleep(8)

    except:
        print("No Internet Connection")
        tittle = "No INTERNET"
        message = "oops! check you internet"
        notify_me("No Internet Connection", message)
        time.sleep(8)
    from covidui import *
    gui()






