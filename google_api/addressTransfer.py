import requests

# 검색할 주소
codes = ['1393', '1397', '1400', '1401', '1402']
location = ['부산광역시 연제구 거제천로 190', '부산 진구 부전1동122-5',
            '부산광역시 기장군 정관읍 용수로 87', '부산 금정구 두실로11', '부산 금정구 금사동 106-17']

# Production(실제 서비스) 환경 - https 요청이 필수이고, API Key 발급(사용설정) 및 과금 설정이 반드시 필요합니다.
index = 0

for key in location:
    # GoogleApiKey를 아래 URL에 넣어주어야 한다.
    URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=GoogleApiKey' \
          '&sensor=false&language=ko&address={}'.format(key)

    # URL로 보낸 Requst의 Response를 response 변수에 할당
    response = requests.get(URL)

    # JSON 파싱
    data = response.json()

    # lat, lon 추출
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']

    print(codes[index], lat, lng)
    index = index + 1
