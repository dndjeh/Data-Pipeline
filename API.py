import requests
import pandas as pd
from datetime import datetime, timedelta
import time
from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일 로드
API_KEY = os.getenv("API_KEY")

# 7일에 한번 씩
## 4일전 데이터까지만 요청됨

today = datetime.today()

# 시작 날짜: 11일 전
start_date = today - timedelta(days=10)

# 종료 날짜: 4일 전
end_date = today - timedelta(days=4)

# 빈 DataFrame에 결과 누적
all_data = pd.DataFrame()

for i in range((end_date - start_date).days + 1):
    date = start_date + timedelta(days=i)
    date_str = date.strftime('%Y%m%d')

    url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/CardSubwayStatsNew/1/1000/{date_str}"

    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()

        # row가 실제로 존재하는지 확인
        if 'CardSubwayStatsNew' not in data or 'row' not in data['CardSubwayStatsNew']:
            print(f" {date_str} 수집 실패: row 없음")
            continue

        rows = data['CardSubwayStatsNew']['row']
        if not rows:
            print(f" {date_str} 수집 실패: row가 비어 있음")
            continue

        df_day = pd.DataFrame(rows)

        # 요청 컬럼들이 존재하는지 검사
        required_cols = ['USE_YMD', 'SBWY_ROUT_LN_NM', 'SBWY_STNS_NM', 'GTON_TNOPE', 'GTOFF_TNOPE']
        if not set(required_cols).issubset(df_day.columns):
            print(f" {date_str} 수집 실패: 컬럼 누락됨")
            continue

        df_day = df_day[required_cols]
        df_day.columns = ['사용일자', '호선명', '역명', '승차인원', '하차인원']

        all_data = pd.concat([all_data, df_day], ignore_index=True)
        print(f"{date_str} 수집 완료")
        
        time.sleep(0.5)

    except Exception as e:
        print(f"⚠️ {date_str} 예외 발생: {e}")
        continue

# 필요 컬럼 정리
# 타입 변환 및 저장
all_data['사용일자'] = pd.to_datetime(all_data['사용일자'], format='%Y%m%d')
all_data['승차인원'] = all_data['승차인원'].astype(int)
all_data['하차인원'] = all_data['하차인원'].astype(int)

#컬럼명 변경


print(all_data.head())
