import requests     #importing all the required modules
import json
from tkinter import *
corona=Tk()
corona.title("CORONA  MONITOR")     #title of the application
corona.iconbitmap("icon.ico")
api_data=requests.get("https://api.covid19api.com/summary") # requesting for the data from third party api
data=json.loads(api_data.content)                        #loading data in the variable
global count
count=6                                                    #counter
def monitor():
   date=Label(corona,text=data["Date"],bg="white",fg="black",font="lato 15 bold",padx="5",pady="5",borderwidth=2,relief="groove")#making all the required headings
   date.grid(row=0,column=2,sticky=N+S+E+W)                                                                                       #giving proper font and styling
   TotalConfirmed=Label(corona,text=data["Global"]["TotalConfirmed"],bg="black",fg="orange",font="lato 20 bold",borderwidth=2)
   TotalConfirmed.grid(row=2,column=0,sticky=N+S+E+W)
   TotalDeaths=Label(corona,text=data["Global"]["TotalDeaths"],bg="white",fg="red",font="lato 20 bold",borderwidth=2)
   TotalDeaths.grid(row=2,column=1,sticky=N+S+E+W)
   TotalRecovered=Label(corona,text=data["Global"]["TotalRecovered"],bg="white",fg="green",font="lato 20 bold",borderwidth=2)
   TotalRecovered.grid(row=2,column=2,sticky=N+S+E+W)
def monitor1():
    global count
    for i in range(1,1000):
           if g.get()==data["Countries"][i]["Country"]:            #checking for the data
                TotalConfirmed=Label(corona,text=data["Countries"][i]["Country"],bg="white",fg="purple",font="lato 20 bold",borderwidth=2)# making a new row and desigining it
                TotalConfirmed.grid(row=count,column=0,sticky=N+S+E+W)
                TotalConfirmed=Label(corona,text=data["Countries"][i]["TotalConfirmed"],bg="black",fg="orange",font="lato 20 bold",borderwidth=2)
                TotalConfirmed.grid(row=count,column=1,sticky=N+S+E+W)
                TotalDeaths=Label(corona,text=data["Countries"][i]["TotalDeaths"],bg="white",fg="red",font="lato 20 bold",borderwidth=2)
                TotalDeaths.grid(row=count,column=2,sticky=N+S+E+W)
                TotalRecovered=Label(corona,text=data["Countries"][i]["TotalRecovered"],bg="white",fg="green",font="lato 20 bold",borderwidth=2)
                TotalRecovered.grid(row=count,column=3,sticky=N+S+E+W)
                count=count+1                                   #increasing the row
                break
G=Label(corona,text="GLOBAL",bg="dark blue",fg="white",font="lato 15 bold",padx="5",pady="5",borderwidth=2,relief="groove")
G.grid(row=0,column=0,sticky=N+S+E+W)
date=Label(corona,text="DATE-:",bg="black",fg="white",font="lato 15 bold",padx="5",pady="5",borderwidth=2,relief="groove")
date.grid(row=0,column=1,sticky=N+S+E+W)
TotalConfirmed=Label(corona,text="Total Confirmed Cases",bg="dark blue",fg="white",font="lato 15 bold",padx="5",pady="5",borderwidth=2,relief="groove")
TotalConfirmed.grid(row=1,column=0,sticky=N+S+E+W)
TotalDeaths=Label(corona,text="Total Deaths",bg="dark blue",fg="white",font="lato 15 bold",padx="5",pady="5",borderwidth=2,relief="groove")
TotalDeaths.grid(row=1,column=1,sticky=N+S+E+W)
TotalRecovered=Label(corona,text="Total Recovered Cases",bg="dark blue",fg="white",font="lato 15 bold",padx="5",pady="5",borderwidth=2,relief="groove")
TotalRecovered.grid(row=1,column=2,sticky=N+S+E+W)
monitor()
country=Label(corona,text="Enter the name of the Country-:",bg="black",fg="yellow",font="lato 15 bold",padx="5",pady="5",borderwidth=2,relief="groove")
country.grid(row=3,column=0,sticky=N+S+E+W)
g=StringVar(corona)
f=Entry(corona,textvariable=g,font="lato 15 bold",fg="black")
f.grid(row=4,column=0,sticky=N+S+E+W)
show=Button(corona,text="SHOW",command=monitor1,bg="black",fg="yellow",font="lato 15 bold",padx="5",pady="5",borderwidth=2,relief="groove")
show.grid(row=4,column=2,sticky=N+S+E+W)
C=Label(corona,text="Country",bg="dark blue",fg="white",font="lato 15 bold",padx="5",pady="5",borderwidth=2,relief="groove")
C.grid(row=5,column=0,sticky=N+S+E+W)
TotalConfirmed=Label(corona,text="Total Confirmed Cases",bg="dark blue",fg="white",font="lato 15 bold",padx="5",pady="5",borderwidth=2,relief="groove")
TotalConfirmed.grid(row=5,column=1,sticky=N+S+E+W)
TotalDeaths=Label(corona,text="Total Deaths",bg="dark blue",fg="white",font="lato 15 bold",padx="5",pady="5",borderwidth=2,relief="groove")
TotalDeaths.grid(row=5,column=2,sticky=N+S+E+W)
TotalRecovered=Label(corona,text="Total Recovered Cases",bg="dark blue",fg="white",font="lato 15 bold",padx="5",pady="5",borderwidth=2,relief="groove")
TotalRecovered.grid(row=5,column=3,sticky=N+S+E+W)
corona.mainloop()   
