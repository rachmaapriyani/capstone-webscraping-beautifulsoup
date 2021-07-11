# Webscrapping using BeautifulSoup

At this module we will learn on how do simple web scrapping using beautiful soup. Web scrapping is one of a method that we can use to colleting the data from internet. At this particular module, we will try to scrap Top 7 Popular movies release in 2021 from https:imdb.com, it's an online database of information related to films, television programs, home videos, video games, and streaming content online – including cast, production crew and personal biographies, plot summaries, trivia, ratings, and fan and critical reviews, originally a fan-operated website, the database is now owned and operated by IMDb.com, Inc.To do this we will only use a couple default library from python and BeautifulSoup. 



## Dependencies

Actually to follow this module you only need to install beautifulsoup4 with `pip install beautifulsoup4` and you are good to go. But here some libraries that needed to be installed first that I use at this module : 

- beautifulSoup4
- pandas
- matplotlibs
- seaborn
- flask


## What is BeautifulSoup

Beautiful Soup is a Python library for pulling data out of HTML and XML files. Beautiful Soup 3 only works on Python 2.x, but Beautiful Soup 4 also works on Python 3.x. Beautiful Soup 4 is faster, has more features, and works with third-party parsers
like lxml and html5lib.

Since beautifulsoup used to pull the data out of a HTML, so first we need to pull out the html first. How we do it? We will use default library `request`. 

So all this code is doing is sending a GET request to spesific address we give. This is the same type of request your browser sent to view this page, but the only difference is that Requests can't actually render the HTML, so instead you will just get the raw HTML and the other response information.

We're using the .get() function here, but Requests allows you to use other functions like .post() and .put() to send those requests as well. At this case we will going to the imdb movies release in 2021 website, you can click [here](https://www.imdb.com/search/title/?release_date=2021-01-01,2021-12-31) to follow what exactly that link goes to. 


## Conclusion

In conclusion from the data we can get top 7 popular movies in 2021. Other optional analyzing I found out the long duration movies also in 2021, and classifying the movies also base on the ratings value. When you don't have a direct access to a data from a website you can always do the scrapping method. For this case Im using beautiful soup and it's more beginner friendly and a helpful utility that allows a programmer to get specific elements out of a webpage. 

I will implement the scrapping to one function and put it at the flask webapp, but in this case I just display the top 7 popular movies in 2021 base on the maximum rating values in the flask webapp.
