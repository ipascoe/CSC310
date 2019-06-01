# -*- coding: utf-8 -*-
"""
@author: Ian Pascoe & Mikayla Gempp

"""

import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


##Average Hours of Sleep: 7-9
def sleepTime(sleep):
   if sleep >= 7:
       sleepy = 0

   elif sleep < 4:
       sleepy = 2

   else:
       sleepy = 1
      
   return sleepy

##Average Heart Rate: 60-100 bpm
def HeartRate(heart):
   if heart > 100:
       rate = 2
   elif heart < 60:
       rate = 2
   else:
       rate = 0

   return rate
  
##Average amount of exercise(per day): 75-150 mins
def ExerciseTime(exercise):
   if exercise >= 75:
       fitness = 0
   elif exercise < 30:
       fitness = 2
   else:
       fitness = 1
   return fitness
      
##Average Water Drank per day: 64 oz
def WaterDrink(water):
   if water >= 64:
       liquid = 0
   elif water < 32:
       liquid = 2
   else:
       liquid = 1
   return liquid

##Anxious Scale: 1(low)-10(high)
def Anxiety(anxious):
   if anxious < 4 :
       stress = 0
   elif anxious > 7:
       stress = 2
   else:
       stress = 1
   return stress

def Final(daystree):
    if daystree <= .67:
	    final = 0
    elif daystree >= 1.34:
        final = 2
    else:
        final = 1     
    return final

def userinput():
    Weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday','Sunday']
    result = []
    sleep=[]
    heartrate=[]
    exercise=[]
    water=[]
    anxiety=[]
    daystress = 0
    for i in range(len(Weekdays)):
        print('Hello! Please answer all the questions below about today:')
        #Sleep 
        string = 'How many hours of sleep did you get on ' + Weekdays[i] + '?: '
        sleepy = int(input(string))
        sleepy = sleepTime(sleepy)
        sleep.append(sleepy)
        #Heart
        string = 'What was your average heart rate on ' + Weekdays[i] + '?: '
        heart = int(input(string))
        heart = HeartRate(heart)
        heartrate.append(heart)
        #Exercise
        string = 'How many minutes did you exercise on ' + Weekdays[i] + '?: '
        fitness = int(input(string))
        fitness = ExerciseTime(fitness)
        exercise.append(ExerciseTime(fitness))
        #Water
        string = 'How many ounces of water did you drink on ' + Weekdays[i] + '?: '
        liquid = int(input(string))
        liquid = WaterDrink(liquid)
        water.append(liquid)
        #Anxious
        string = 'On a scale of 1-10, how anxious were you on ' + Weekdays[i] + '?: '
        anxious = int(input(string))
        anxious = Anxiety(anxious)
        anxiety.append(anxious)
        #Results
        daystress = (sleepy+heart+fitness+liquid+anxious)/5
        final = Final(daystress)
        result.append(final)
        if final == 0:
            print('\n\n**Today, on ', Weekdays[i], 'your anxiety level was low.**')
        elif final == 1:
            print('\n\n**Today, on ', Weekdays[i], 'your anxiety level was moderate.**')
        else:
            print('\n\n**Today, on ', Weekdays[i], 'your anxiety level was high.**')
        print('We will see you tomorrow!\n\n')
    data = {'sleep':sleep, 'heartrate':heartrate, 'exercise':exercise, 'water':water, 'anxiety':anxiety, 'predicted_anx':result}
    df = pd.DataFrame(data=data)
    return df
        
def main():
    i=1
    while(i==1):
        df = userinput()
        plot_weekanx = df.loc[:,'predicted_anx'].rename('Weekly Anxiety')
        print('The pie chart below shows how your anxiety was overall during the week, showing how frequent you had low, mild, or high anxiety. This can change each week.')
        plot_weekanx.value_counts().plot.pie()
        print('The scatterplot below shows which data you inputted each day this week was most significant to your anxiety per day. This could change this week and help you show what you should focus on more in order to reduce anxiety.')
        sns.pairplot(df, hue='predicted_anx', size=2)
        ##Linear Regression
        print('The linear regression below for each variable against your final anxiety during the week, showing how their relationship to your overall anxiety was this week. This will also change each week to help you decide what to focus on more in order to reduce anxiety.')
        print('There will be an r squared score to show you how correlated each variable is from 0% to 100%. The closer to 100, the closer correlated the two variables are.')
        ##Sleep
        print("Sleep vs Final Anxiety")
        x = pd.DataFrame(df['sleep'])
        y = df['predicted_anx']
        plt.scatter(x, y)
        plt.show()    
        model = LinearRegression(fit_intercept=True)
        model.fit(x, y)
        print("Model slope:    ", model.coef_[0])
        print("Model intercept:", model.intercept_)
        # plot the model together with the data 
        yfit = model.predict(x)
        plt.scatter(x, y)
        plt.plot(x, yfit)
        plt.show()
        # compute the R^2 score – good models: R^2 ~ 1                                                                                             
        print("R^2 score: {}".format(model.score(x,y)))
        ##Heart Rate
        print("heart rate vs Final Anxiety")
        x = pd.DataFrame(df['heartrate'])
        y = df['predicted_anx']
        plt.scatter(x, y)
        plt.show()    
        model = LinearRegression(fit_intercept=True)
        model.fit(x, y)
        print("Model slope:    ", model.coef_[0])
        print("Model intercept:", model.intercept_)
        # plot the model together with the data 
        yfit = model.predict(x)
        plt.scatter(x, y)
        plt.plot(x, yfit)
        plt.show()
        # compute the R^2 score – good models: R^2 ~ 1                                                                                             
        print("R^2 score: {}".format(model.score(x,y)))
        ##Exercise
        print("exercise vs Final Anxiety")
        x = pd.DataFrame(df['exercise'])
        y = df['predicted_anx']
        plt.scatter(x, y)
        plt.show()    
        model = LinearRegression(fit_intercept=True)
        model.fit(x, y)
        print("Model slope:    ", model.coef_[0])
        print("Model intercept:", model.intercept_)
        # plot the model together with the data 
        yfit = model.predict(x)
        plt.scatter(x, y)
        plt.plot(x, yfit)
        plt.show()
        # compute the R^2 score – good models: R^2 ~ 1                                                                                             
        print("R^2 score: {}".format(model.score(x,y)))
        ##Water
        print("Water vs Final Anxiety")
        x = pd.DataFrame(df['water'])
        y = df['predicted_anx']
        plt.scatter(x, y)
        plt.show()    
        model = LinearRegression(fit_intercept=True)
        model.fit(x, y)
        print("Model slope:    ", model.coef_[0])
        print("Model intercept:", model.intercept_)
        # plot the model together with the data 
        yfit = model.predict(x)
        plt.scatter(x, y)
        plt.plot(x, yfit)
        plt.show()
        # compute the R^2 score – good models: R^2 ~ 1                                                                                             
        print("R^2 score: {}".format(model.score(x,y)))
        ##Anxiety
        print("Daily Anxiety vs Final Anxiety")
        x = pd.DataFrame(df['anxiety'])
        y = df['predicted_anx']
        plt.scatter(x, y)
        plt.show()    
        model = LinearRegression(fit_intercept=True)
        model.fit(x, y)
        print("Model slope:    ", model.coef_[0])
        print("Model intercept:", model.intercept_)
        # plot the model together with the data 
        yfit = model.predict(x)
        plt.scatter(x, y)
        plt.plot(x, yfit)
        plt.show()
        # compute the R^2 score – good models: R^2 ~ 1                                                                                             
        print("R^2 score: {}".format(model.score(x,y)))
        print('Lets work on having a good week next week! See you tomorrow!')
        
main()