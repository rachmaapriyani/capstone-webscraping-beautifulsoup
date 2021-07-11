from flask import Flask, render_template
import pandas as pd
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.imdb.com/search/title/?release_date=2021-01-01,2021-12-31')
soup = BeautifulSoup(url_get.content,"html.parser")

movie_data = soup.findAll('div', attrs={'class':'lister-item mode-advanced'})

temp = [] #initiating a tuple

for store in movie_data:
    
    #get movie title columns
    Movie_Title = store.h3.a.text
        
    #get movie duration(optional) columns
    Runtime_Minute = store.p.find ('span', class_ ='runtime').text.replace('min','').replace(' ','') if store.p.find ('span', class_ ='runtime') else '0'
        
    #get movie rating columns
    Rating = store.find('div', class_ = 'inline-block ratings-imdb-rating').text.replace('\n','') if store.find('div', class_ = 'inline-block ratings-imdb-rating') else '0' 
    
    #get metascore columns
    Metascore = store.find('span', class_= 'metascore').text.replace(' ','') if store.find('span', class_= 'metascore') else '0'
    
    #get votes columns
    Votes = store.find('span', attrs = {'name': "nv"}).text if store.find('span', attrs = {'name': "nv"}) else '0'
    
    
    temp.append((Movie_Title,Runtime_Minute,Rating,Metascore,Votes)) 

temp = temp[::-1]

#change into dataframe
data = pd.DataFrame(temp, columns = ('Movie_Title','Runtime_Minute','Rating','Metascore','Votes'))

#insert data wrangling here
data['Rating'] = data['Rating'] .astype('float')
data['Metascore'] = data['Metascore'] .astype('int64')
data['Runtime_Minute'] = data['Runtime_Minute'] .astype('int64')
data['Votes'] = data['Votes'].str.replace(',', ".").astype(float)

#end of data wranggling 

@app.route("/")
def index(): 
	
	top7 = data.nlargest(7,'Rating')[['Movie_Title','Rating']].set_index('Movie_Title')

	# generate plot
	plt.figure(figsize=(15,5))
	ax = sns.barplot(x='Rating',y=top7.index,data=top7)
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]


	# render to html
	return render_template('index.html',
		card_data = top7, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)
