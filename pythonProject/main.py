import requests
import bs4

import tkinter as tk

def get_html_data(url):
    data = requests.get(url)
    return data


def get_covid_data():
    url = "http://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data=""

    for block in info_div:
        text = block.find("h1", class_=None).get_text()

        count = block.find("span", class_=None).get_text()

        all_data = all_data + text + " " + count + "\n"

    return all_data

#Button COMMANDs
def get_country_data():
    name= textfield.get()
    url = "http://www.worldometers.info/coronavirus/country/"+ name
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = ""

    for block in info_div:
     try:
        text = block.find("h1", class_=None).get_text()

        count = block.find("span", class_=None).get_text()

        all_data = all_data + text + " " + count + "\n"
     except AttributeError:
         continue

    mainlabel['text']=all_data


def reload():
    new_data = get_covid_data()
    mainlabel['text']=new_data



get_covid_data()


root = tk.Tk()
root.geometry("700x700")
root.title("COVID-19 TRACKER")
f = ("Times New Roman" , 25 ,"bold")
root.configure(bg="black")

banner = tk.PhotoImage(file="coronavirus1.png")
bannerlabel = tk.Label(root , image =banner)
bannerlabel.pack()

textfield= tk.Entry(root , width = 65 ,  bg='red' ,fg='black' )
textfield.pack()


mainlabel = tk.Label(root , text=get_covid_data(), font=f ,bg='black' ,fg='white')
mainlabel.pack()



gbtn = tk.Button(root ,text ="Get_Data" , font= f , relief= 'solid' , command=get_country_data ,bg='red',fg='white' )
gbtn.pack()

rbtn = tk.Button(root ,text ="Reload" , font= f , relief= 'solid' , command=reload ,bg='red',fg='white')
rbtn.pack()

root.mainloop()
