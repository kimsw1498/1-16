# streamlit 연습
# # flask보다 streamlit이 배포가 쉽다(접근성 좋음) / flask처럼 예쁘게 만들려면 CSS 변경하면 색깔이나 이런것을 바꿀 수 있다

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt               # 차트를 더 예쁘게 만들고 싶을 때 사용
# import seaborn as sns                         # 차트를 더 예쁘게 만들고 싶을 때 사용
# import numpy as np


# # 여러개 한번에 설치하는 방법 - pip install matplotlib seaborn numpy   (그냥 한 줄에 쭉 쓴다, 띄어쓰기 하고 컴마 없이)

# # 다른 개발자한테 어떤거 설치해야하는지 말해줘야지- requirements.txt 파일 만들어서 알려주기
# # 실행할 때는 한번에 가능 : pip install -r requirements.txt



# # 외부에서 데이터 가지고 오기
# # 공공기관에서 csv나 액셀파일로 줌 : 서로 변환, 읽기 가능 (공공데이터포털 이라는 홈페이지 참고)
# # 파일 다운로드 후 여기에 복사해서 넣기


# st.title("📊 국세청 근로소득 데이터 분석기")


# # 데이터 불러오기
# file_path = "국세청_근로소득 백분위(천분위) 자료_20241231.csv"               # 파일이름이 길어서 변수로 지정 - 같은 폴더에 있으니까 이런식으로만 하면 됨
# # 만약에 파일이 다른 하위 폴더에 들어있다면 file_path = "./data/국세청_근로소득 백분위(천분위) 자료_20241231.csv"  이런식으로 경로 지정해주기 (data는 하위 폴더명)
# # 만약 상위 폴더에 있다면 file_path = "../국세청_근로소득 백분위(천분위) 자료_20241231.csv"  이런식으로 경로 지정해주기 (..은 상위 폴더 의미, 방 나가기)


# # 혹시 모를 오류 방지  (액셀의 iferror 같은 느낌)
# try :                                                   # 오류가 없을때 처리 - 오류 생기면 저 밑에 있는 except 구문으로 넘어감
#     # 자료 읽기
#     df = pd.read_csv(file_path,encoding='cp949')                               # csv 파일을 잘 읽었는지 확인하기
#     st.success("✅ 데이터가 성공적으로 불러와졌습니다!")            # 성공 메세지 출력

#     # 데이터 미리 보기
#     st.subheader("📜 데이터 확인하기")
#     st.dataframe(df.head())                                 # () 안에 숫자 쓰지 않으면 :표 상단 5줄 보여줌(기본값) / ()안에 보고 싶은 숫자 넣으면 그 숫자만큼 보여줌

#     # 데이터 분석 그래프 그리기
#     st.subheader("📉 항목별 분포 그래프")

#     # 분석하고 싶은 열 이름을 선택
#     # 예를 들어 인원,총급여 같은 숫자 데이터가 있는 칸을 고를 수 있게 만들기
#     column_names = df.columns.tolist()                           # 각 컬럼의 제목들을 추출하겠다 - 데이터프레임의 열 이름들을 리스트로 변환
#     selected_col = st.selectbox("분포를 보고 싶은 항목을 선택하세요 : ", column_names)   # selectbox : 드롭다운 메뉴 만들기 / 첫번째 인자 : 설명문구, 두번째 인자 : 선택지들

#     # 그래프 그리기(seaborn 활용)
#     fig, ax = plt.subplots(figsize=(10, 5))                      # 차트의 크기 지정 / fig는 전체 그래프 사이즈(타이틀까지 모두 포함)/ ax는 그래프가 그려지는 공간
#     sns.histplot(df[selected_col], ax=ax, color="#FF5AD9", kde=True)  # seaborn의 histplot 막대그래프 / 컬러지정 - 16진법 (#쓰고16진법쓰기) /kde=True 분포도 곡선까지
    
#     plt.title(f"[{selected_col}] 분포 확인")                      # 그래프 맨 위에 제목
#     plt.xlabel(selected_col)                                     # x축 제목 (ex. 급여액)
#     plt.ylabel("빈도수")                                          # y축 제목

#     # 스트림릿 웹 화면에 그래프 표시
#     st.pyplot(fig)                                               # st.pyplot() : 스트림릿에서 그래프 그릴 때 사용하는 함수 / fig 변수를 넣어주기

# except FileNotFoundError:                              # 파일 못 찾았을 때 오류 처리
#     st.error(f"❌ '{file_path}' 파일을 찾을 수 없습니다. 파일명이 정확한지 확인하세요.")
# except Exception as e:                                 # 신텍스 에러
#     st.error(f"❌ 에러가 발생했습니다{e}")               # e함수는 신텍스 에러 내용을 알려줌



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import platform

# 1. 한글 폰트 설정 (그래프 깨짐 방지)
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

st.title("📊 국세청 근로소득 데이터 분석기")

file_path = "국세청_근로소득 백분위(천분위) 자료_20241231.csv"

try:
    # 2. encoding='cp949' 추가
    df = pd.read_csv(file_path, encoding='cp949')
    st.success("✅ 데이터가 성공적으로 불러와졌습니다!")

    st.subheader("📜 데이터 확인하기")
    st.dataframe(df.head())

    st.subheader("📉 항목별 분포 그래프")
    column_names = df.columns.tolist()
    selected_col = st.selectbox("분포를 보고 싶은 항목을 선택하세요 : ", column_names)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(df[selected_col], ax=ax, color="#FF5AD9")
    
    plt.title(f"[{selected_col}] 분포 확인")
    plt.xlabel(selected_col)
    plt.ylabel("빈도수")

    st.pyplot(fig)

except FileNotFoundError:
    st.error(f"❌ '{file_path}' 파일을 찾을 수 없습니다.")
except Exception as e:
    st.error(f"❌ 에러가 발생했습니다: {e}")
