'''
-------------------------------------------------------------------------------
                            TRACKORONA GRAPHS  (LEVEL 3)
                BY : Vishal Das , Harshit Sharma  ,  Gumutch Mishra 
-------------------------------------------------------------------------------
'''
from plyer import notification
from tkinter import *
import numpy as np
import matplotlib.pyplot as plot
from bs4 import BeautifulSoup as bs
import requests
# this helps to scrap the Javascript attributes via a Js Object
import json
def gui():

    root = Tk()
    root.title (' TRACKORONA TRENDS ')
    root.iconbitmap ('C:/Users/OK/PycharmProjects/TRACKORONA PROJECT/covid_icon_new_gNa_icon.ico')
    root.configure(background = 'red')
    root.geometry ("400x500")


    def graph () :
        # Web scrapping to get the graph data set
        html_graph = requests.get("https://www.worldometers.info/coronavirus/country/india")
        soup = bs(html_graph.content, "html.parser")
        scripts = list(soup.find_all('script'))
        script = str(scripts[22])

        # getting the graph's x-axis data
        dates = script.split("categories: [", 1)[1].split("]", 1)[0]
        dates = "[" + dates + "]"
        dates = json.loads(dates)
        # print (dates)

        # getting the graph's y-axis data
        data = script.split("data: [", 1)[1].split("]", 1)[0]
        data = "[" + data + "]"
        data = json.loads(data)
        # print (data)

        # plotting the graph
        plot.title(" TOTAL COVID - 19 CASES ( 15 FEB till data ) ")
        plot.ylabel(" NO. OF CASES ( x 10^7 ) ")
        plot.bar(dates[1:], data[1:])
        plot.gca().axes.get_xaxis().set_visible(False)
        plot.show()

    def graph_2 () :
        html_graph = requests.get("https://www.worldometers.info/coronavirus/country/india")
        soup = bs(html_graph.content, "html.parser")
        scripts = list(soup.find_all('script'))
        script2 = str(scripts[23])

        dates1 = script2.split("categories: [", 1)[1].split("]", 1)[0]
        dates1 = "[" + dates1 + "]"
        dates1 = json.loads(dates1)
        # print(dates1)

        data1 = script2.split("data: [", 1)[1].split("]", 1)[0]
        data1 = "[" + data1 + "]"
        data1 = json.loads(data1)
        # print(data1)

        plot.title(" Daily COVID - 19 CASES ( FEB 15 till Date ) ")
        plot.ylabel(" NO. OF CASES ")
        plot.bar(dates1[1:], data1[1:])
        plot.gca().axes.get_xaxis().set_visible(False)
        plot.show()

    def graph_3 () :
        html_graph = requests.get("https://www.worldometers.info/coronavirus/country/india")
        soup = bs(html_graph.content, "html.parser")
        scripts = list(soup.find_all('script'))
        script3 = str(scripts[24])

        dates2 = script3.split("categories: [", 1)[1].split("]", 1)[0]
        dates2 = "[" + dates2 + "]"
        dates2 = json.loads(dates2)
        # print(dates2)

        data2 = script3.split("data: [", 1)[1].split("]", 1)[0]
        data2 = "[" + data2 + "]"
        data2 = json.loads(data2)
        # print(data2)

        plot.title(" ACTIVE COVID - 19 CASES ( FEB 15 till Date ) ")
        plot.ylabel(" NO. OF CASES ( x 10^6 ) ")
        plot.bar(dates2[1:], data2[1:])
        plot.gca().axes.get_xaxis().set_visible(False)
        plot.show()

    def graph_4 () :
        html_graph = requests.get("https://www.worldometers.info/coronavirus/country/india")
        soup = bs(html_graph.content, "html.parser")
        scripts = list(soup.find_all('script'))
        script4 = str(scripts[25])
        # print (scripts)

        dates3 = script4.split("categories: [", 1)[1].split("]", 1)[0]
        dates3 = "[" + dates3 + "]"
        dates3 = json.loads(dates3)
        # print(dates3)

        data3 = script4.split("data: [", 1)[1].split("]", 1)[0]
        data3 = "[" + data3 + "]"
        data3 = json.loads(data3)
        # print(data3)

        plot.title(" TOTAL COVID DEATHS ( FEB 15 till Date ) ")
        plot.ylabel(" NO. OF CASES ")
        plot.bar(dates3[1:], data3[1:])
        plot.gca().axes.get_xaxis().set_visible(False)
        plot.show()

    def graph_5 ():
        html_graph = requests.get("https://www.worldometers.info/coronavirus/country/india")
        soup = bs(html_graph.content, "html.parser")
        scripts = list(soup.find_all('script'))
        script5 = str(scripts[26])

        dates4 = script5.split("categories: [", 1)[1].split("]", 1)[0]
        dates4 = "[" + dates4 + "]"
        dates4 = json.loads(dates4)
        # print(dates4)

        data4 = script5.split("data: [", 1)[1].split("]", 1)[0]
        data4 = "[" + data4 + "]"
        data4 = json.loads(data4)


        plot.title(" DAILY NEW DEATHS ( FEB 15 till Date ) ")
        plot.ylabel(" NO. OF CASES ")
        plot.bar(dates4[6:], data4[6:])
        plot.gca().axes.get_xaxis().set_visible(False)
        plot.show()

    # def growthrate ():
    #     html_graph = requests.get("https://www.worldometers.info/coronavirus/country/india")
    #     soup = bs(html_graph.content, "html.parser")
    #     scripts = list(soup.find_all('script'))
    #     script5 = str(scripts[26])
    #     data4 = script5.split("data: [", 1)[1].split("]", 1)[0]
    #     today = int(data4[-3:])
    #     yesterday = int(data4[-7:-4])
    #     growth = (today) / (yesterday)
    #     msg = "GROWTH RATE : " + str(growth)
    #     if (growth >= 1):
    #         msg = msg + "\nSITUATION IS ALARMING !!!"
    #
    #     notify_me("SITUATION AT GLANCE", msg)

    def graph_6 () :
        html_graph = requests.get("https://www.worldometers.info/coronavirus/country/india")
        soup = bs(html_graph.content, "html.parser")
        scripts = list(soup.find_all('script'))
        script6 = str(scripts[28])

        dates5 = script6.split("categories: [", 1)[1].split("]", 1)[0]
        dates5 = "[" + dates5 + "]"
        dates5 = json.loads(dates5)
        # print(dates5)

        data5 = script6.split("data: [", 1)[1].split("]", 1)[0]
        data5 = "[" + data5 + "]"
        data5 = json.loads(data5)
        # print(data5)

        plot.title(" DEATH RATE ( FEB 15 till Date ) ")
        plot.ylabel(" PERCENT % ")
        plot.bar(dates5[1:], data5[1:])
        plot.gca().axes.get_xaxis().set_visible(False)
        plot.show()

    def vaccine():
        htmldata=requests.get("https://covid-19tracker.milkeninstitute.org/")
        soup = bs(htmldata.text, "html.parser")
        result = str(soup.find_all("div", class_="is_h5-2 is_developer w-richtext"))
        root2 = Tk()
        root2.title( "VACCINE IN PROGRESS")
        root2.geometry ("600x190")
        T = Text(root2, height=100, width=100,font='Times',bg = "Yellow" , fg = "Black")

        T.pack()
        T.insert(INSERT,"NO 1 : " + result[46:86].replace(" ", "")+
                "\nNO 2 : "+result[139:199].replace(" ", "")+
                "\nNO 3 : "+result[279:305].replace(" ", "")+
                "\nNO 4 : " + result[358:374].replace(" ", "") +
                "\nNO 5 : "+result[428:436].replace(" ", ""))
        root2.mainloop()

    def notify_me (title , message) :
        notification.notify (
            title = title ,
            message = message ,
            app_icon = "C:/Users/OK/PycharmProjects/TRACKORONA PROJECT/covid_icon_2_FMC_icon.ico" ,
            timeout = 10
        )

    # linking the graphs' Functioning with the GUI Buttons

    my_button = Button (root , text = " GRAPH 1 " , padx = 40, pady = 10, relief = RAISED , bg = "Yellow" , fg = "Black" , font='Mistral 20 bold', command = graph)
    my_button.grid (row=1, column=0)

    my_button_2 = Button (root , text = " GRAPH 2 " , padx = 40 , pady = 10 , relief = RAISED , bg = "Yellow" , fg = "Black" , font='Mistral 20 bold', command = graph_2)
    my_button_2.grid (row=1 , column=1)

    my_button_3 = Button (root , text = " GRAPH 3 " , padx = 40 , pady = 10 , relief = RAISED , bg = "Yellow" , fg = "Black" , font='Mistral 20 bold', command = graph_3)
    my_button_3.grid (row=2 , column=0)

    my_button_4 = Button (root , text = " GRAPH 4 " , padx = 40 , pady = 10 , relief = RAISED , bg = "Yellow" , fg = "Black" , font='Mistral 20 bold', command = graph_4)
    my_button_4.grid (row=2 , column=1)

    my_button_5 = Button (root , text = " GRAPH 5 " , padx = 40 , pady = 10 , relief = RAISED , bg = "Yellow" , fg = "Black" , font='Mistral 20 bold', command = graph_5)
    my_button_5.grid (row=3 , column=0)

    my_button_6 = Button (root , text = " GRAPH 6 " , padx = 40 , pady = 10 , relief = RAISED , bg = "Yellow" , fg = "Black" , font='Mistral 20 bold', command = graph_6)
    my_button_6.grid (row=3 , column=1)

    my_button_7= Button (root , text = " VACCINE UPDATE " , padx = 100 , pady = 38 , relief = RAISED , bg = "Yellow" , fg = "Black" , font='Mistral 20 bold', command = vaccine)
    my_button_7.place (x = 0 , y = 228)

    # photo = PhotoImage (file = r"C:/Users/OK/Desktop/image2.png")
    my_label = Label (root , text = " TRACKORONA GUI " , padx = 102, pady = 80 , fg = "Black" , font = 'Mistral 20 bold' , compound = LEFT,bg = 'cornflowerblue')
    my_label.place (x = 0 , y = 350)
    # growthrate()

    root.mainloop()
gui()