import requests
import json
from pprint import pprint

file_path = "./movie_data.json"

# API 지정
apikey = "5d5ba12807e444883a57039b0e2a1015"

# 정보를 알고 싶은 영화 리스트 만들기
tmdb_id_list = [line.split(', ') for line in open('all_tmdb_id.txt', 'r')]
tmdb_id_list = list(map(int, sum(tmdb_id_list, [])))

# API 지정
movie_api = "https://api.themoviedb.org/3/movie/{movies}?api_key={key}&language=ko-KR"
genre_api = "https://api.themoviedb.org/3/genre/movie/list?language=en-US&api_key={key}"

# string.format_map() 매핑용 클래스 만들기
class Default(dict):
    def __missing__(self, key):
        return key

movie_data = []

# 각 영화의 정보 추출하기
for tmdb_id in tmdb_id_list:
    # API의 URL 구성하기
    url = movie_api.format_map(Default(movies=tmdb_id, key=apikey))
    # API에 요청을 보내 데이터 추출하기
    # json 형태의 데이터가 나온다.
    r = requests.get(url)
    # 결과를 JSON 형식으로 변환하기
    raw_data = json.loads(r.text)

    data = {"model": "movies.movie"}
    fields = {}
    fields['title'] = raw_data['title']
    fields['tagline'] = raw_data['tagline']
    fields['id'] = raw_data['id']
    fields['genre'] = []
    genre_list = []
    for genre in raw_data['genres']:
        genre_list.append(genre['id'])
    fields['genre'] = genre_list
    fields['poster_path'] = raw_data['poster_path']
    fields['backdrop_path'] = raw_data['backdrop_path']
    fields['overview'] = raw_data['overview']
    fields['released_date'] = raw_data['release_date']
    fields['popularity'] = raw_data['popularity']
    fields['vote_average'] = raw_data['vote_average']
    fields['vote_count'] = raw_data['vote_count']
    # fields['adult'] = raw_data['adult']
    
    data["fields"] = fields
    movie_data.append(data)

with open(file_path, 'w', encoding='utf-8') as outfile:
    json.dump(movie_data, outfile, indent=4, ensure_ascii=False)
