from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
import json
from collections import Counter

link = requests.get('http://strims.world/').text
soup = BeautifulSoup(link, 'lxml')
Events = []
Time = []
Discipline = []
Text = []
Event = []
Eve = []
Day = []


def Event(request):

    AllEvents = soup.find_all('td', class_='wydarzenie')

    def count_events_on_each_day(id):
        day = []
        for x in (soup.find_all('div', id=id)):
            day.append(x)
        day = str(day[0])
        day = day.split("\"")
        count = Counter(day)
        ilosc_wydarzen = count['wydarzenie']

        return ilosc_wydarzen

    def add_matching_day_to_array():

        for i in range(len(AllEvents)):
            if i <= dayOneEventsAmount:
                Day.append(1)
            if dayOneEventsAmount < i < dayTwoEventsAmount + dayOneEventsAmount:
                Day.append(2)
            if dayOneEventsAmount + dayTwoEventsAmount < i < dayOneEventsAmount + dayTwoEventsAmount + dayThreeEventsAmount:
                Day.append(3)
            if dayOneEventsAmount + dayTwoEventsAmount + dayThreeEventsAmount < i < dayOneEventsAmount + dayTwoEventsAmount + dayThreeEventsAmount + dayFourEventsAmount:
                Day.append(4)
            if dayOneEventsAmount + dayTwoEventsAmount + dayThreeEventsAmount + dayFourEventsAmount < i < dayOneEventsAmount + dayTwoEventsAmount + dayThreeEventsAmount + dayFourEventsAmount + dayFiveEventsAmount:
                Day.append(5)
        return Day

    def pretting_data():
        Licznik = 0
        for i in AllEvents:
            Events.append(i)
            Text.append(i.text)
            i = str(i).strip('<td class=\"wydarzenie\">')
            i = i.split(' ')
            Time.append(i[0])
            Discipline.append(i[2])
            i = " ".join(i)
            Event = Text[Licznik].split()
            del Event[0]
            Event = " ".join(Event)
            Discipline[Licznik] = Discipline[Licznik].replace('class="', '').replace('"', '')
            Licznik += 1
            Eve.append(Event)



    for i in range(5):

        count_events_on_each_day(i+1)

    dayOneEventsAmount = count_events_on_each_day(1)
    dayTwoEventsAmount = count_events_on_each_day(2)
    dayThreeEventsAmount = count_events_on_each_day(3)
    dayFourEventsAmount = count_events_on_each_day(4)
    dayFiveEventsAmount = count_events_on_each_day(5)

    add_matching_day_to_array()
    pretting_data()

    ListaEventow = []
    Licznik = 0
    Eventt = {}
    for i in range(len(AllEvents)):
        print(Time[i], Eve[i], Discipline[i])

        Eventt = {

            'time': Time[Licznik],
            'event': Eve[Licznik],
            'discipline': Discipline[Licznik],
            'day': Day[Licznik],
        }
        if len(Eventt['time']) == 5:
            ListaEventow.append(Eventt)

        else:
            Eventt.clear()

        Licznik += 1

    b = []
    for i in range(0, len(ListaEventow)):
        if ListaEventow[i] not in ListaEventow[:i]:
            b.append(ListaEventow[i])

    ListaEventow.clear()
    del ListaEventow
    ListaEventow = b

    return render(request, 'blog/terminarz.html', {'ListaEventow': ListaEventow})