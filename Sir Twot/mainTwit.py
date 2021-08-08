from tkinter.font import BOLD
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from tkinter import StringVar
import tkinter as tk
import time, random, requests, webbrowser
from bs4 import BeautifulSoup

root  = tk.Tk()

def botStart():
    PATH = pathEntry.get()
    driver = webdriver.Chrome(PATH)
    driver.get('https://twitter.com/login')
    while True:
        try:
            driver.find_element_by_css_selector('[name="session[username_or_email]"]').send_keys(usernameEntry.get())
            driver.find_element_by_css_selector('[name="session[password]"]').send_keys(passwordEntry.get())
            break
        except:
            time.sleep(0.2)

    while True:
        try:
            driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()
            break
        except:
            time.sleep(0.2)

    def bioSwapper():
        statusPage = 'https://twitter.com/settings/profile'
        homePage = 'https://twitter.com/home'

        with open('status.txt', 'r') as file:
            status = file.read().split('\n')
        
        driver.get(statusPage)

        while True:
            try:
                driver.find_element_by_css_selector('[name="description"]').send_keys(Keys.CONTROL + "a")
                driver.find_element_by_css_selector('[name="description"]').send_keys(Keys.DELETE)
                driver.find_element_by_css_selector('[name="description"]').send_keys(status[random.randint(0, (len(status)-1))])
                break
            except: 
                time.sleep(0.2)

        while True:
            try:
                driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div').click()
                break
            except:
                time.sleep(0.2)

        driver.get(homePage)

    
    def tweeter():
        tweetType = random.randint(1, 1000)
        if tweetType < 200:
            tweetMessage = randomFact()
        elif tweetType >= 200 and tweetType < 400:
            tweetMessage = randomJoke()
        elif tweetType >= 400 and tweetType < 600:
            tweetMessage = randomNews()
        elif tweetType >= 650 and tweetType < 800:
            tweetMessage = randomQuote()
        elif tweetType >= 800:
            tweetMessage = randomAnimal()

        while True:
            try:
                driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div').send_keys(tweetMessage)
                driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()
                break
            except:
                time.sleep(0.2)
    
    interval = int(intervalEntry.get()) * 60
    while True:
        bioSwapper()
        time.sleep(2)
        tweeter()
        time.sleep(interval)


def randomFact():
    facts = []

    source = requests.get('https://cerebraldatabank.neocities.org/database/').text
    soup = BeautifulSoup(source, 'lxml')

    facts = []
    for fact in soup.find_all('li'):
        unsplit = str(fact)
        temp = unsplit.replace("/", "")
        temp = temp.replace("<sup>", "")
        temp = temp.replace("<i>", "")
        temp = temp.replace('<abbr title="Système International (of units), also International System of Units>"', "")
        temp = temp.replace("<abbr>", "")
        temp = temp.replace("amp;", "")
        split = temp.split("<li>")
        facts.append(split[1])

    return facts [random.randint(0, (len(facts)-1))]

def randomJoke():
    jokes = []

    source = requests.get('https://bestlifeonline.com/one-liner-jokes/').text
    soup = BeautifulSoup(source, 'lxml')

    for joke in soup.find_all('li'):
        unsplit = str(joke)
        temp = unsplit.replace('li', '')
        temp = temp.replace("/", "")
        temp = temp.replace('\\', "")
        temp = temp.replace(">", "<")
        split = temp.split("<")
        jokes.append(split[2])

    del jokes[0:12]
    del jokes[40:68]

    return jokes [random.randint(0, (len(jokes)-1))]

def randomAnimal():
    with open('animalPics.txt', 'r') as file:
        animals = file.read().split('\n')

    return animals [random.randint(0, (len(animals)-1))]

def randomQuote():
    with open('quotes.txt', 'r') as file:
        quotes = file.read().split('\n')

    return quotes [random.randint(0, (len(quotes)-1))]

def randomNews():
    titles = []
    links = []
    source = requests.get('https://www.voanews.com/').text
    soup = BeautifulSoup(source, 'lxml')

    for article in soup.find_all('div', {"class":"top-story"}):
        splitTitle = article.prettify().split('"')
        titles.append(splitTitle [5])
        links.append(splitTitle [3])

    randomArticle = random.randint(0, (len(titles)-1))
    news = titles [randomArticle] + ' ' + 'https://www.voanews.com' + links [randomArticle]
    return news

def helpScreen():
    webbrowser.open('https://github.com/Antisine/Sir-Twot-the-Bot', new=2)

photoStart = tk.PhotoImage(file = r"C:\Users\Antisine\Documents\Coding Projects\Twitter Bot\startbutton.png")
photoHelp = tk.PhotoImage(file = r"C:\Users\Antisine\Documents\Coding Projects\Twitter Bot\helpbutton.png")

root.title('Sir Twot')
root.iconbitmap(r'C:\Users\Antisine\Documents\Coding Projects\Twitter Bot\boticon.ico')
tk.Label(root, text="Sir Twot", font=("Courier", 19)).grid(row=0, column=2)
tk.Label(root, text="     ").grid(row=1, column=0)
tk.Label(root, text="Username", font=("Times", 11, BOLD)).grid(row=1, column=1)
usernameEntry = StringVar()
tk.Entry(root, width=20, textvariable=usernameEntry).grid(row=1, column=2)
tk.Label(root, text="     ").grid(row=1, column=3)
tk.Label(root, text="     ").grid(row=2, column=0)
tk.Label(root, text="Password", font=("Times", 11, BOLD)).grid(row=2, column=1)
passwordEntry = StringVar()
tk.Entry(root, width=20, textvariable=passwordEntry).grid(row=2, column=2)
tk.Label(root, text="     ").grid(row=2, column=3)
tk.Label(root, text="     ").grid(row=3, column=0)
tk.Label(root, text="Interval", font=("Times", 11, BOLD)).grid(row=3, column=1)
intervalEntry = StringVar()
tk.Entry(root, width=20, textvariable=intervalEntry).grid(row=3, column=2)
tk.Label(root, text="     ").grid(row=3, column=3)
tk.Label(root, text="     ").grid(row=4, column=0)
tk.Label(root, text="PATH", font=("Times", 11, BOLD)).grid(row=4, column=1)
pathEntry = StringVar()
tk.Entry(root, width=20, textvariable=pathEntry).grid(row=4, column=2)
tk.Label(root, text="     ").grid(row=4, column=3)
tk.Label(root, text="     ").grid(row=5, column=2)
tk.Button(root, image=photoHelp, command=helpScreen, borderwidth=0).grid(row=6, column=1)
tk.Button(root, image=photoStart, command=botStart, borderwidth=0).grid(row=6, column=2)
tk.Label(root, text="     ").grid(row=7, column=2)

root.mainloop()