from selenium import webdriver
import os
import time
import json
import random
import math
class SearchList:
    SearchedContent = []
    def DisplayContent(self):
        index = 0
        for i in self.SearchedContent:
            print('______________________________________________________________')
            print('Content reference: '+str(index))
            i.DisplayMovie();            
            index = index+1
        return;
    def ReturnSelectedContent(self, Reference):
                
        if(len(self.SearchedContent) > 0):
            try:
                if(len(self.SearchedContent) > int(Reference)):                     
                    movieInfo = self.SearchedContent[int(Reference)].ReturnMovieInfo()                    
                    try:
                     return movieInfo['Title'] 
                    except:
                     return movieInfo['title']
            except:                
                return None                                            
        else:                             
            return 'Empty'
        
        
    def SearchMovies(self, ContentName, page):        
        br = webdriver.Chrome('chromedriver.exe')
        br.implicitly_wait(15) # wait's for the page to get done
         #loading before it does anything with it
         #br.get('http://www.omdbapi.com/?i=tt3896198&apikey=b32d452f')
                
        found = False        
        while(found == False):            
            br.get('http://www.omdbapi.com/?s='+ ContentName +'&page='+str(page)+'&apikey=b32d452f')
            # to fill out a form
            data = json.loads(br.find_element_by_tag_name('body').text)
            #close the browser so it doesn't clutter the user
            if(data['Response'] == 'True'):    
                movies = []               
                for content in data['Search']:                    
                    movies.append(Movie(content))
                for content in movies:                                        
                    self.SearchedContent.append(content)
                found = True                
                br.close()            
            else:
                ContentName = input('Enter a valid content title: ')           
        #return page
        return {'Page':page, 'MaxPage':math.ceil(int(data['totalResults'])/10)}

    def SearchMoviesTMDB(self, ContentName, page):        
        br = webdriver.Chrome('chromedriver.exe')
        br.implicitly_wait(15) # wait's for the page to get done
         #loading before it does anything with it
         #br.get('http://www.omdbapi.com/?i=tt3896198&apikey=b32d452f')
#https://api.themoviedb.org/3/search/movie?query=hulk&api_key=efd9b74dce000dd9c3cbdd4d84d62a90&page=1
        found = False        
        while(found == False):            
            br.get('https://api.themoviedb.org/3/search/movie?query='+ContentName+'&api_key=efd9b74dce000dd9c3cbdd4d84d62a90&page='+str(page))
            # to fill out a form
            data = json.loads(br.find_element_by_tag_name('body').text)
            #close the browser so it doesn't clutter the user
            if(int(data['total_results']) > 0):                
                movies = []               
                for content in data['results']:                    
                    movies.append(Movie(content))
                for content in movies:                                        
                    self.SearchedContent.append(content)
                found = True                
                br.close()           
            else:
                ContentName = input('Enter a valid content title: ')             
        #return page information
        return {'Page':page, 'MaxPage':data['total_pages']}          

        
        
class WishList:
    MovieList = []
    ContentComment = []
    def DisplayList(self):
        if(len(self.MovieList) > 0):
            index = 0
            for i in self.MovieList:
                print('______________________________________________________________')
                print('Content reference: '+str(index))
                i.DisplayMovie();
                for comments in self.ContentComment:
                    if(int(comments['Reference'])==index):
                        print(comments['Comment'])
                index = index+1
        else:
            print('Your wishlist is empty')
        
    def AddToList(self, Search):
        self.MovieList.append(Search) 
        return;
    def RemoveFromList(self, Reference):
        valid = False
        while valid == False:
            if len(self.MovieList) > 0:
                try:
                    if int(Reference) < len(self.MovieList):
                        del self.MovieList[int(Reference)]
                        for comments in self.ContentComment:
                            if(int(comments['Reference'])==Reference):
                                del comments
                        print('This item has been removed!')
                        valid = True
                    else:
                        print('Enter E to exit or...')
                        Reference = input('Invalid entry; enter a refence that is valid: ') 
                except:
                    if(Reference == 'E' or Reference == 'e'):
                        valid = True                
                    else:
                        print('Enter E to exit or...')
                        Reference = input('Invalid entry; enter a refence that is valid: ')
            else:
                print('Your wishlist is empty!')
                valid = True
    def AddContentComment(self, Reference, Comment):
        valid = False
        while valid == False:
            if len(self.MovieList) > 0:
                try:
                    if int(Reference) < len(self.MovieList):
                        data = {'Reference':Reference,'Comment':Comment}
                        self.ContentComment.append(data)
                        print('This comment has been added!')
                        valid = True
                    else:
                        print('Enter E to exit or...')
                        Reference = input('Invalid entry; enter a refence that is valid: ') 
                except:
                    if(Reference == 'E' or Reference == 'e'):
                        valid = True                
                    else:
                        print('Enter E to exit or...')
                        Reference = input('Invalid entry; enter a refence that is valid: ')
            else:
                print('Your wishlist is empty!')
                valid = True
class Movie:
     MovieInfo = []
     def __init__(self, data = None):
         self.MovieInfo = data
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
     def ReturnMovieInfo(self):
         return self.MovieInfo
    
     def DisplayMovie(self):
      try: 
         try:
             print('Title: ' + self.MovieInfo['Title'])
             print('Year: ' + self.MovieInfo['Year'])
             print('Rated: ' + self.MovieInfo['Rated'])
             print('Released: ' + self.MovieInfo['Released'])
             print('Runtime: ' + self.MovieInfo['Runtime'])
             print('Genre: ' + self.MovieInfo['Genre'])
             print('Director: ' + self.MovieInfo['Director'])
             print('Writer: ' + self.MovieInfo['Writer'])
             print('Actors: ' + self.MovieInfo['Actors'])
             print('Plot: ' + self.MovieInfo['Plot'])
             print('Language: ' + self.MovieInfo['Language'])
             print('Country: ' + self.MovieInfo['Country'])
             print('Awards: ' + self.MovieInfo['Awards'])
             print('Year: ' + self.MovieInfo['Year'])
             print('Ratings: ')
             for ratings in self.MovieInfo['Ratings']:
                 print(ratings['Source']+' '+ratings['Value'])
             print('Type: ' + self.MovieInfo['Type'])
         except:
             print('Type: ' + self.MovieInfo['Type'])
      except:
             print('Title: ' + self.MovieInfo['title'])             
             print('Released: ' + self.MovieInfo['release_date'])
             print('Plot: ' + self.MovieInfo['overview'])
             print('Language: ' + self.MovieInfo['original_language'])             
     def SearchMovie(self, title):
         
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
                 self.MovieInfo = data
                 found = True
                 br.close()
             else:
                 title = input('Enter a valid content title: ')
         
         
         
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
                     self.MovieInfo = data
                     found = True
                     br.close()
                 elif(filterType.upper() == 'GENRE') and (self.CheckMovieGenre(movie=data,genre=filterSearch)==True):                     
                     self.MovieInfo = data
                     found = True
                     br.close()
                 elif(filterType.upper() == 'TYPE') and (self.CheckMovieType(movie=data,Type=filterSearch)==True):
                     self.MovieInfo = data
                     found = True
                     br.close()

def PageTurner(page,maxPage):
    print('Enter E to exit or...')
    print('Enter < or > to flip between pages')
    end = False
    while(end == False):
        entry = input()
        if (entry == '<' and page >= 1):
            end = True
            return page-1
        elif(entry == '<'):
            entry = input('This is the first page; enter < or E to exit: ')
        elif(entry == '>' and page < maxPage):
            end = True
            return page+1 
        elif(entry == '>'):
            entry = input('This is the last page; enter < or E to exit: ')               
        elif(entry == 'e' or entry == 'E'):
            end = True
            return 0
        else:
            entry = input('Invalid input, enter either < or > to change pages: ')
            
    
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
    
def checkValidType(Type):
    try:
        if(Type.upper() == 'MOVIE' or Type.upper() == 'SERIES'):
            return True
        else:
            return False
    except:
        return False
def wishlistMenu(movie, wishlist):
    option = input('Do you want to add this film to your wishlist? [y/n]: ')
    valid = False
    while valid == False:
        try:
            if option.upper() == 'Y':
                wishlist.AddToList(movie)
                valid = True
            elif option.upper() == 'N':
                valid = True
            else:
                option = input('Invalid input; enter y or n: ')
        except:
            option = input('Invalid input; enter y or n: ')
        
    
    
#trasfer the data to a python dictonary


#Film.SearchMovie(title='a cool bool fool soon')
#Film.DisplayMovie()
#WL = WishList()
#WL.AddToList(MovieID = Film.GetID())
end = False
WL = WishList()
while(end == False):
    print('====================================================') 
    print('ACME-Software-Ltd---Movie-Information-client-')
    print('Menu')
    print('1. Specific search by title')
    print('2. Search by random')
    print('3. General search')
    print('4. Edit wishlist')
    print('5. Exit')
    print('====================================================') 
    print('')
    
    
    
    option1 = input('Enter an option by number: ')
    if option1 == '1':
        clear = lambda: os.system('cls') #on Windows System
        clear()
        print('Enter E to exit or...')
        search = input('Enter a movie title: ')
        if search.upper() != 'E':
            Film = Movie()
            Film.SearchMovie(search)
            Film.DisplayMovie()
            wishlistMenu(Film, WL)
    elif option1 == '2':
        clear = lambda: os.system('cls') #on Windows System
        clear()
        end2 = False
        while end2 == False:
            print('Enter E to exit or...')        
            FT = input('Enter how you want to filter (Genre or Type): ')
            try:
                if FT.upper() == 'GENRE':
                    end3 = False
                    while end3 == False:
                        FS = input('Enter how you want to filter (Horror): ')
                        if (checkValidGenre(FS)):
                            Film.SearchMovieRng(filterType = FT, filterSearch = FS)
                            Film.DisplayMovie()
                            wishlistMenu(Film, WL)
                            end2 = True
                            end3 = True
                        else:
                            print('Invalid genre')
                elif FT.upper() == 'TYPE':
                    end3 = False
                    FS = input('Enter how you want to filter (Movie,Series): ')
                    while end3 == False:                    
                        if (checkValidType(FS)):
                            Film.SearchMovieRng(filterType = FT, filterSearch = FS)
                            Film.DisplayMovie()
                            wishlistMenu(Film, WL)
                            end2 = True
                            end3 = True
                        else:
                            FS = input('Invalid entry; enter either movie or series: ')
                elif FT.upper() == 'E':
                    end2 = True
                else:
                    print('Invalid entry')
            except:
                print('Invalid entry')
    elif option1 == '3':
         SPage = SearchList()
         end2 = False
         validDatabase = False
         clear = lambda: os.system('cls') #on Windows System
         clear()
         database = input('Enter a database you want to search by [IMDB or TMDB]: ')
         while validDatabase == False:             
             try:
                 if database.upper() == 'IMDB':
                     database = database.upper()
                     validDatabase = True
                 elif database.upper() == 'TMDB':
                     database = database.upper()
                     validDatabase = True
                 else:
                     database = input('Invalid entry; enter either [IMDB or TMDB]: ')                 
             except:
                 database = input('Invalid entry; enter either [IMDB or TMDB]: ')
         while end2 == False:             
             print('______________________________________________________________')
             print('General search Menu')
             print('1. Search content')
             print('2. Add content to wishlist')
             print('3. Exit')
             print('______________________________________________________________')                    
             option2 = input('Enter an option by number: ')
             end3 = False
             while end3 == False:
                 if option2 == '1':
                     end4 = False
                     page = 1
                     print('This search will be made using '+database)
                     ContentName = input('Enter the name of the content you want to search: ')
                     while end4 == False:
                         if page > 0:
                             if database == 'IMDB':
                                 PageInfo = SPage.SearchMovies(ContentName, page)
                             else:
                                 PageInfo = SPage.SearchMoviesTMDB(ContentName, page)
                             newPage=int(PageInfo['Page'])
                             maxPage=int(PageInfo['MaxPage'])
                             if page == newPage:                                 
                                 SPage.DisplayContent()
                                 print('______________________________________________________________')
                                 print('Page: '+str(page) +'/'+str(maxPage))
                             else:
                                 page = newPage
                             page = PageTurner(page,maxPage)                         
                         else:
                             end3 = True
                             end4 = True
                 elif option2 == '2':
                     print('Enter E to exit or...')
                     ContentRef = input('Enter a valid content reference to add it: ')
                     valid = False
                     while valid == False:
                         if (ContentRef == 'E' or ContentRef == 'e'):
                             valid = True
                         elif (SPage.ReturnSelectedContent(ContentRef) != None 
                               and SPage.ReturnSelectedContent(ContentRef) != 'Empty'):
                             m = Movie()
                             m.SearchMovie(str(SPage.ReturnSelectedContent(ContentRef)))
                             WL.AddToList(m)
                             valid = True
                         elif SPage.ReturnSelectedContent(ContentRef) == 'Empty':
                             print('Your search list is empty, search for content first')
                             valid = True
                         else:
                             print('Enter E to exit or...')
                             ContentRef = input('Invalid entry; enter a refence that is valid: ')
                    
                     end3=True
                 elif option2 == '3':
                     end2 = True
                     end3 = True
                 else:
                     option2 = input('Invalid entry; enter a number: ')
                        
    elif option1 == '4':
        clear = lambda: os.system('cls') #on Windows System
        clear()
        end2 = False
        while end2 == False:
            print('______________________________________________________________')
            print('Wishlist Menu')
            print('1. Display wishlist')
            print('2. Remove content')
            print('3. Add comments to content')
            print('4. Exit')
            print('______________________________________________________________')                    
            option2 = input('Enter an option by number: ')
            end3 = False
            while end3 == False:
                if option2 == '1':
                    WL.DisplayList()
                    end3 = True
                elif option2 == '2':
                    contentRef = input('Enter a valid content reference to remove it: ')
                    WL.RemoveFromList(contentRef)
                    end3=True
                elif option2 == '3':
                    contentRef = input('Enter a valid content reference to add a comment: ')
                    contentComment = input('Enter a comment for the content: ')
                    WL.AddContentComment(contentRef,contentComment)
                    end3=True
                elif option2 == '4':
                    end2 = True
                    end3 = True
                else:
                    option2 = input('Invalid entry; enter a number: ')
                        
    elif option1 == '5':
         end = True 