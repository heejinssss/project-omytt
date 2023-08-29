
# 1. JustWatch에서 추출한 'nfx'/'dnp'/'wac'/'wav'/'apt'/'ply' json 파일에서 tmdb id만 출력

'''
import json

movies_json = open('json_data/my_netflix.json', encoding='utf-8')
movies_list = json.load(movies_json)

try:
    lst = []
    for dict_lst in movies_list: # 페이지당
        for num in range(30): # 페이지 내에서 30번씩 (page size = 30)
            for type in ((dict_lst["items"])[num])["scoring"]:
                if type["provider_type"] == "tmdb:id":
                    lst.append(type["value"])
    print(lst)
except:
    print(lst)
'''

# -------------------------------------------------------------------------------

# 2. 전체 tmdb id 값과 OTT tmdb id 값을 비교하여 json 형태로 출력

import sys

# OTT 값을 리스트로 저장
ott_list = ['nfx', 'dnp', 'wac', 'wav', 'apt', 'ply']

# OTT tmdb id 값을 저장할 딕셔너리 생성
ott_id_dict = {"nfx": "", "dnp": "", "wac": "", "wav": "", "apt": "", "ply": ""}

# ott_tmdb.txt 에서 tmdb id 값을 ott_id_dict 딕셔너리에 저장
for ott in ott_list:
    list_file = [line.split(', ') for line in open(f'id_data/{ott}_tmdb.txt', 'r')]
    list_file = list(map(int, list_file[0]))
    ott_id_dict[ott] = list_file

# 전체 OTT tmdb id 값을 리스트로 저장
tmdb_id_list = [line.split(', ') for line in open('all_tmdb_id.txt', 'r')]
tmdb_id_list = list(map(int, sum(tmdb_id_list, [])))

movie_data = [] # 모든 id 데이터 담을 리스트
for tmdb_id in tmdb_id_list:
    data = {} # id 별로 데이터 담을 딕셔너리
    fields = {}

    # data => model 값
    data["model"] = "movies.ott"

    # data => fields => tmdb id 값
    fields["tmdb_id"] = tmdb_id

    # data => fields => ott 값 추가
    tmp = []
    for ott in ott_list:
        if tmdb_id in ott_id_dict[ott]: # tmdb id 값이 'nfx'/'dnp'/'wac'/'wav'/'apt'/'ply'에서 제공하는 영화의 tmdb id 값과 일치한다면
            tmp.append(ott) # 해당하는 ott를 임시 리스트에 저장
    fields["ott"] = tmp

    # data => fields 값
    data["fields"] = fields
    
    movie_data.append(data)

sys.stdout = open('ott_offer.txt', 'w', encoding="UTF-8")    

print(movie_data)

sys.stdout.close()