from cProfile import label
from tkinter import *
import tkinter as tk
from tkinter import font
from unittest import result
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
from PIL import Image, ImageTk
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
 #retrieve weather data from OpenWeather API
def getWeather():
    try:
        city=textfield.get()
        
        geolocator= Nominatim(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj =TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        
        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&units=imperial&appid=45a7df8264e59cb44244162f747bf369"
        
        json_data = requests.get(api).json()
        condition =json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp= int(json_data['main']['temp'])
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']
        
        t.config(text=(temp,"°"))
        c.config(text=(condition,'|', "FEELS","LIKE",temp, "°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!")

#Code for search objects
Search_image=PhotoImage(file="search.png")
myImage=Label(image=Search_image)
myImage.place(x=680,y=-60)

textfield=tk.Entry(root,justify="center",width=15,font=("poppins",25,"bold"))
textfield.place(x=590,y=22)
textfield.focus()

Search_icon=PhotoImage(file="searchIcon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",command=getWeather)
myimage_icon.place(x=850,y=17)

# Logo
Logo_image=PhotoImage(file="weather-app.png")
logo=Label(image=Logo_image)
logo.place(x=10,y=-80)

#code for bottom image
Frame_image=PhotoImage(file="textBox_6_700x130.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time code
name=Label(root,font=("arial",15,"bold"))
name.place(x=550,y=100)
clock=Label(root,font=("Helvetica",15,"bold"))
clock.place(x=550,y=130)

#Labels
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#36311e")
label1.place(x=220,y=405)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#36311e")
label2.place(x=310,y=405)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#36311e")
label3.place(x=420,y=405)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#36311e")
label4.place(x=550,y=405)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=530,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=530,y=250)
# Labels for data in bottom image
w=Label(text="...",font=("arial",15,"bold"),bg="#36311e")
w.place(x=220,y=430)
h=Label(text="...",font=("arial",15,"bold"),bg="#36311e")
h.place(x=310,y=430)
d=Label(text="...",font=("arial",15,"bold"),bg="#36311e")
d.place(x=420,y=430)
p=Label(text="...",font=("arial",15,"bold"),bg="#36311e")
p.place(x=550,y=430)

root.mainloop()
