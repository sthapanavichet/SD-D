import requests
from ratelimit import limits

# api_key
api_key = 'c9a36f46351617abfaffb664f309c260'
# Get genre mappping
genres_mapping = requests.get(f'https://api.themoviedb.org/3/genre/movie/list?language=en&api_key={api_key}').json()['genres']


def validate_input(input):
    if len(input) > 100:  # Check if the string is too long
        print('Input name is too long. Please try again.')
        return False
    elif input.isnumeric():  # Check if only number is entered
        print('Input name cannot be all numeric')
        return False
    elif input.isspace():  # Check if only whitespace is entered
        print('Input name cannot be empty')
        return False
    else:
        return True

def display_movie(movies):
    for movie in movies:
        genre_ids = movie.get('genre_ids', [])

        # Map the genre id to the genre
        genre_names = [genre['name'] for genre in genres_mapping if genre['id'] in genre_ids]

        # Print details of the top result
        print("\nResult:")
        print(f"Title: {movie['title']}")
        print(f"Release Date: {movie['release_date']}")
        print(f"Overview: {movie['overview']}")
        print(f"Genres: {', '.join(genre_names)}")

@limits(calls=15, period=60)
def search_movie():
    while True:
        movie_query = input('Enter the name of a movie: ')
        if validate_input(movie_query):
            break
    movie_query = movie_query.replace(' ', '+')
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_query}&api_key={api_key}&sort_by=popularity.desc"
    while True:
        release_year = int(input('Enter year of release (enter 0 to skip): '))
        if release_year < 0:
            print('Invalid Year.')
        elif release_year == 0:
            break
        else:
            url += f"&year={release_year}"
            break

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Check if there are any results
        if data['results']:
            display_movie([data['results'][0]])
        else:
            print("No results found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
@limits(calls=15, period=60)
def discover_movie():
    page_number = 1
    while True:
        genres = input('Enter genres you want to discover (use , to separate two or more genres): ')
        if validate_input(genres):
            break
    if genres.count(',') > 1:
        genres = genres.lower().split(',')
    genre_query = [str(genre['id']) for genre in genres_mapping if genre['name'].lower() in genres]
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&include_adult=false&include_video=false&language=en-US&page={page_number}&with_genres={','.join(genre_query)}"
    while True:
        release_year = int(input('Enter year of release (enter 0 to skip): '))
        if release_year < 0:
            print('Invalid Year.')
        elif release_year == 0:
            break
        else:
            url += f'&primary_release_year={release_year}'
            break
    while True:
        sort_by = input('How do you want the movies to be sort?(Popularity/Rating/ReleaseDate/None): ').lower()
        if sort_by == 'popularity':
            url += f'&sort_by=popularity.desc'
            break
        elif sort_by == 'rating':
            url += f'&sort_by=vote_average.desc'
            break
        elif sort_by == 'releasedate':
            url += f'&sort_by=primary_release_date.desc'
            break
        elif sort_by == 'none':
            break
        else:
            print('Enter a valid option')
    while True:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            # Check if there are any results
            if data['results']:
                display_movie(data['results'])
            else:
                print("No results found.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
        change_page = input('Next/Back/Exit: ').lower()
        if change_page == 'next':
            page_number += 1
            url = url.replace(f'page={page_number-1}', f'page={page_number}')
        elif change_page == 'back' and page_number > 1:
            page_number -= 1
            url = url.replace(f'page={page_number + 1}', f'page={page_number}')
        elif change_page == 'exit':
            break
        else:
            print('Action cannot be performed')

def main():
    while True:
        choice = input("Enter 1 to search for a movie: \nEnter 2 to discover movies \nChoice: ")
        if choice == '1':
            search_movie()
            break
        elif choice =='2':
            discover_movie()
            break
        else:
            print('Invalid choice')


if __name__ == '__main__':
    main()
