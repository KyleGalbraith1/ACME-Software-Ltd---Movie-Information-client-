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
     def CheckMovieType(movie, Type):         
         if Type.upper() in movie['Type'].upper():
             return True
         else:
             return False   
    
     def DisplayMovie(self):
         print('Title: ' + Movie.MovieInfo['Title'])
         print('Year: ' + Movie.MovieInfo['Year'])
         print('Rated: ' + Movie.MovieInfo['Rated'])
         print('Released: ' + Movie.MovieInfo['Released'])
         print('Runtime: ' + Movie.MovieInfo['Runtime'])
         print('Genre: ' + Movie.MovieInfo['Genre'])
         print('Director: ' + Movie.MovieInfo['Director'])
         print('Writer: ' + Movie.MovieInfo['Writer'])
         print('Actors: ' + Movie.MovieInfo['Actors'])
         print('Plot: ' + Movie.MovieInfo['Plot'])
         print('Language: ' + Movie.MovieInfo['Language'])
         print('Country: ' + Movie.MovieInfo['Country'])
         print('Awards: ' + Movie.MovieInfo['Awards'])
         print('Year: ' + Movie.MovieInfo['Year'])
         print('Ratings: ')
         for ratings in Movie.MovieInfo['Ratings']:
             print(ratings['Source']+' '+ratings['Value'])
         print('Type: ' + Movie.MovieInfo['Type'])
         
    
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
                 elif(filterType.upper() == 'TYPE') and (Movie.CheckMovieType(movie=data,Type=filterSearch)==True):
                     Movie.MovieInfo = data
                     found = True
                     br.close()

def checkValidGenre(genre):
    if(genre.upper() == 'HORROR' or genre.upper() == 'DRAMA' or genre.upper() == 'ACTION'
    or genre.upper() == 'COMEDY' or genre.upper() == 'SCI-FI' or genre.upper() == 'ROMANCE'
    or genre.upper() == 'THRILLER' or genre.upper() == 'MYSTERY' or genre.upper() == 'CRIME'
    or genre.upper() == 'ANIMATION' or genre.upper() == 'ADVENTURE'or genre.upper() == 'FANTASY'
    or genre.upper() == 'BIOGRAPHY' or genre.upper() == 'DOCUMENTARY'
    or genre.upper() == 'FAMILY' or genre.upper() == 'MUSICAL' or genre.upper() == 'SHORT'
    or genre.upper() == 'WAR' or genre.upper() == 'WESTERN'):
        return True
    else:
        return False
    
def checkValidType(type):
    if(type.upper() == 'MOVIE' or type.upper() == 'SERIES'):
        return True
    else:
        return False
    
#trasfer the data to a python dictonary
Film = Movie()

#Film.SearchMovie(title='a cool bool fool soon')
#Film.DisplayMovie()
#WL = WishList()
#WL.AddToList(MovieID = Film.GetID())
end = False
while(end == False):
    print('ACME-Software-Ltd---Movie-Information-client-')
    print('Menu')
    print('1. Search by title')
    print('2. Search by random')
    print('3. Exit')
    print('')
    print('====================================================') 
    
    
    option1 = input('Enter an option by number: ')
    if option1 == '1':
        print('Enter E to exit or')
        search = input('Enter a movie title:')
        if search.upper() != 'E':
            Film.SearchMovie(search)
            Film.DisplayMovie()
            
    elif option1 == '2':
        end2 = False
        while end2 == False:
            print('Enter E to exit or')        
            FT = input('Enter how you want to filter (Genre or Type): ')
            if FT.upper() == 'GENRE':
                end3 = False
                while end3 == False:
                    FS = input('Enter how you want to filter (Horror): ')
                    if (checkValidGenre(FS)):
                        Film.SearchMovieRng(filterType = FT, filterSearch = FS)
                        Film.DisplayMovie()
                        end2 = True
                        end3 = True
                    else:
                        print('Invalid genre')
            elif FT.upper() == 'TYPE':
                end3 = False
                while end3 == False:
                    FS = input('Enter how you want to filter (Movie,Series): ')
                    if (checkValidType(FS)):
                        Film.SearchMovieRng(filterType = FT, filterSearch = FS)
                        Film.DisplayMovie()
                        end2 = True
                        end3 = True
                    else:
                        print('Invalid genre')
            elif FT.upper() == 'E':
                end2 = True
            else:
                print('Invalid entry')
    elif option1 == '3':
        end = True            
                
                
                
                
                
                
                
#WL = WishList()
#WL.AddToList(MovieID = Film.GetID())
#WL.DisplayList()

#for Ratings in movies['Ratings']:
 #   source = Ratings['Source']
  #  rating = Ratings['Value']
   # print(source,rating)

