# Dictionary of movies
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def above55(movie):
    for i in range(len(movies)):
        if movies[i]["name"] == movie:
                return movies[i]["imdb"]>5.5 

def sublist():
    under55 = []
    for i in range(len(movies)):
        if movies[i]["imdb"]<5.5:
            under55.append(movies[i]["name"])
    print(under55)
    
def categorylist(name):
    needMovies = []
    for i in range(len(movies)):
        if movies[i]["category"] == name:
                needMovies.append(movies[i]["name"])
    print(needMovies)

def list_average(preferred):
    n = 0
    k = 0
    for i in range(len(movies)):
         if movies[i]["name"] in preferred:
            n += movies[i]["imdb"]
            k += 1
    print(round(n/k, 1))

def cat_average(name):
    n = 0
    k = 0
    for i in range(len(movies)):
        if movies[i]["category"] == name:
            n += movies[i]["imdb"]
            k += 1
    print(round(n/k, 1))


# first task
movie = input('Enter a name of movie: ')
print(above55(movie))
print()
# second task
print("A sublist of movies with an IMDB score above 5.5: ")
sublist()
print()
# third task
category = input("Enter a category name: ")
print("Movies from category named " + category + ":")
categorylist(category)
print()
# fourth task
print("Average rating of movies The Choice, Colonia, Love, Bride Wars, We Two, Dark Knight is: ", end='')
list_average(['The Choice', 'Colonia', 'Love', 'Bride Wars', 'We Two', 'Dark Knight'])
print()
# fifth task 
category5 = input("Enter a category name: ")
print("Average IMDB score of movies from "+category5+" category is -", end=' ')
cat_average(category5)
print("The end.")