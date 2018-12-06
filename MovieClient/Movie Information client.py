from selenium import webdriver
import time
import json
import random
class WishList:
    MovieList = []
    def DisplayList(self):
        for i in WishList.MovieList:
            print(i);
        return;
    def AddToList(self, MovieID):
        WishList.MovieList.append(MovieID) 
        return;
    
class Movie:
     MovieInfo = {}
     def __init__(self):
         return;
     def CheckMovieGenre(movie, genre):         
         if genre.upper() in movie['Genre'].upper():
             return True
         else:
             return False         
    
     def DisplayMovie(self):
         print(Movie.MovieInfo) 
    
     def GetID(self):         
         return Movie.MovieInfo['imdbID'];
         
     def SearchMovie(self, title ):
         br = webdriver.Chrome('chromedriver.exe')
         br.implicitly_wait(15) # wait's for the page to get done
         #loading before it does anything with it
         #br.get('http://www.omdbapi.com/?i=tt3896198&apikey=b32d452f')
         found = False
         while(found == False):
             br.get('http://www.omdbapi.com/?t='+ title + '&apikey=b32d452f')
             # to fill out a form
             data = json.loads(br.find_element_by_tag_name('body').text)
             #close the browser so it doesn't clutter the user
             if(data['Response'] == 'True'):
                 Movie.MovieInfo = data
                 found = True
                 br.close()
             else:
                 title = input('Enter a valid movie title: ')
         
         
         
     def SearchMovieRng(self, filterType=None, filterSearch=None):
         br = webdriver.Chrome('chromedriver.exe')
         br.implicitly_wait(15) # wait's for the page to get done
             #loading before it does anything with it
         found = False
         while(found == False):
             randomID = str(random.randrange(0, 3, 3))+str(random.randrange(0, 3, 3))
             index = 0
             while(index<5):
                 randomID = randomID+str(random.randrange(0, 10, 3))
                 index = index+1
             #br.get('http://www.omdbapi.com/?i=tt3896198&apikey=b32d452f')         
             br.get('http://www.omdbapi.com/?i=tt'+ randomID + '&apikey=b32d452f')
             # to fill out a form
             data = json.loads(br.find_element_by_tag_name('body').text)
             #close the browser so it doesn't clutter the user                 
             if(data['Response'] == 'True'):
                 if (filterType == None):
                     Movie.MovieInfo = data
                     found = True
                     br.close()
                 elif(filterType.upper() == 'GENRE') and (Movie.CheckMovieGenre(movie=data,genre=filterSearch)==True):                     
                     Movie.MovieInfo = data
                     found = True
                     br.close()
            

                 
             

             
    

#trasfer the data to a python dictonary
Film = Movie()
#Film.SearchMovie(title = 'blade runner')
#Film.SearchMovie(title='a cool bool fool soon')
#Film.DisplayMovie()
#WL = WishList()
#WL.AddToList(MovieID = Film.GetID())
FT = input('Enter how you want to filter (Genre or Type[movie, series, DVD]): ')
if FT.upper() == 'GENRE':
    FS = input('Enter how you want to filter: ')
Film.SearchMovieRng(filterType = FT, filterSearch = FS)
Film.DisplayMovie()
#WL = WishList()
#WL.AddToList(MovieID = Film.GetID())
#WL.DisplayList()

#for Ratings in movies['Ratings']:
 #   source = Ratings['Source']
  #  rating = Ratings['Value']
   # print(source,rating)

