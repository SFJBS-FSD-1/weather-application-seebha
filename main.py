import os
import requests
import datetime
from flask import Flask,render_template,request

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])  #""" default method is get"""
def weather_page():
    print(request.method)
    if request.method=="POST":
        city=request.form["city"]
        api="9504d64c15bcdd5e6d4323dabcc9c54b"
        url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+\
            api+"&units=metric"   #here units=metric gives the correct unit without external calculations
        response=requests.get(url).json()
        print(response)
        if response['cod']==200:
            data={'temp':response['main']['temp'],'city':response['name'],'long':response['coord']['lon'],'lati':response['coord']['lat']
                  ,'sunrise':datetime.datetime.fromtimestamp(response.get('sys')['sunrise']),'status':200}
        elif response['cod']=='404':
            data={'message':response['message'],'status':404}
        return render_template("home.html", data=data)
    else:
        data=None
        return render_template("home.html",data=data)






# http://api.openweathermap.org/data/2.5/weather?q=bangalore&appid=997ea79e1c9575bd4f087cf90e68205d
# "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid"=997ea79e1c9575bd4f087cf90e68205d




port=int(os.environ.get("PORT",5000))


if __name__=="__main__":
    app.run(port=port)


