# Movie-Recommender

Movie Recommender Report

**Data Source: Kaggle   [TMDB 5000 Movie Dataset | Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)** 

**We have 2 dataset one is having the detail about the movies and other is having the detail about cast and crew. The dataset is having record of 4803 movies and and having 22 unique features.**

**Target: Create an app where you put the movie name and it will recommend the 5 movies**

**Approach: will create a new columns which has corpus of keywords.  This corpus will having the words from overview, genres, keywords, production companies, cast and crew. Each movie is having a unique corpus. Will transform this corpus into 6000 dimension vector and calculate the cosine similarity between them.**
# Data Preprocessing
## Data Cleaning:
The dataset is having 22 unique feature, I will be using 8 of them. 

- Problem1: 6 features are stored as dictionaries and I have to extract only the name from each dictionaries. 
- Approach: create a loop where you pull the name from the dictionaries and append it to an empty list.
- Problem 2: Crew Feature has many names out of which I want the director name
- Approach: create a loop filter job title as director and pull the name from the dictionaries and append it to an empty list.
- Status: Effective
### Create a corpus of keywords
`	`**Approach**: Merge all the list of columns to one and convert this list to string and make it lower case.

`	`**Status**: Effective
### `	`Remove repeated words from corpus
`	`**Approach**: Stemming (Lemmatization is yet to be tested)

`	`**Status**: Effective
# Transformation:
- **Problem**: Transform the corpus into a vector
- **Approach**: CountVectorizer (Will convert into a 6000 dimension with stop words) 
- **Status**: Effective


# Similarity between Vectors:
**Approach**: Cosine Similarity

**Status**: Effective
# Extract The 5 Similar Movie:
**Approach**: To keep the indexing intact will enumerate similarity score and sort it by similarity score, next will take the index of those scores and find out the movie name.
# Deployment
**Will use streamlit module to create a website and deploy over Heroku platform.**

**Challenges**: By giving the movie name it should display the next 5 movie name with image.

**Approach**: will define a function which will take an input of movie name and give the index number of similar 5 movie. Will use TMDB api to fetch (by movie id) the poster of these 5 movies. Will print the posters along with the movie name. 

**Status:** Effective.

## **NOTE:** The size of Cosine Similarity is large therefor i have not uploaded it on git 


