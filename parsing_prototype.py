import requests
import json
import csv
import os
# import numpy as np
# from numpy import dot
# from numpy.linalg import norm
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import MySQLdb
import auth_data

def get_deposit_data():
    login = auth_data.datasource
    conn = MySQLdb.connect(
        db=login['db'],
        host=login['host'],
        user=login['user'],
        passwd=login['passwd'],
        port=login['port'],
        charset=login['charset']
    )
    c=conn.cursor()
    
    pwd = os.getcwd()
    file_path = pwd+"/depositdata.csv"

    
    results = []

    c.execute("select fin_prdt_cd,spcl_cnd from depositProduct")
    for row in c.fetchall():
      fin_prdt_cd = row[0] #bank code
      spcl_cnd = row[1] #raw terms
      results.append([fin_prdt_cd, spcl_cnd])

    # CSV 파일로 저장
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"기존에 존재하던 {file_path} 파일이 삭제되었습니다.")
    else:
        print(f"기존에 존재하던 {file_path} 파일이 존재하지 않습니다.")

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 헤더 작성
        writer.writerow(['fin_prdt_cd', 'spcl_cnd'])
        # 결과 작성
        writer.writerows(results)
    conn.close()

def get_saving_data():
    login = auth_data.datasource
    conn = MySQLdb.connect(
        db=login['db'],
        host=login['host'],
        user=login['user'],
        passwd=login['passwd'],
        port=login['port'],
        charset=login['charset']
    )
    c=conn.cursor()
    
    pwd = os.getcwd()
    file_path = pwd+"/savingdata.csv"

    
    results = []

    c.execute("select fin_prdt_cd,spcl_cnd from savingProduct")
    for row in c.fetchall():
      fin_prdt_cd = row[0] #bank code
      spcl_cnd = row[1] #raw terms
      results.append([fin_prdt_cd, spcl_cnd])

    # CSV 파일로 저장
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"기존에 존재하던 {file_path} 파일이 삭제되었습니다.")
    else:
        print(f"기존에 존재하던 {file_path} 파일이 존재하지 않습니다.")

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 헤더 작성
        writer.writerow(['fin_prdt_cd', 'spcl_cnd'])
        # 결과 작성
        writer.writerows(results)
    conn.close()
        


# """# 코사인 유사도 분석 로직"""
#
#
#
# def cos_sim(a, b):
#   return dot(a, b)/(norm(a)*norm(b))
#
# doc1 = np.array([0, 1, 1, 1])
# doc2 = np.array([1, 0, 1, 1])
# doc3 = np.array([2, 0, 2, 2])
#
# print("문서 1과 문서 2의 유사도 : ", cos_sim(doc1, doc2))
# print("문서 1과 문서 3의 유사도 : ", cos_sim(doc1, doc3))
# print("문서 2과 문서 3의 유사도 : ", cos_sim(doc2, doc3))

"""# 유사도를 이용한 추천 시스템 구현"""

# data = pd.read_csv(os.getcwd()+"/depositdata.csv", low_memory = False)

# 상위 2만개의 sample을 data에 저장
# data = data.head(20000)

"""### 데이터 전처리
<br/>TF-IDF를 연산할 때 데이터에 Null 값이 들어있으면 에러가 발생합니다.
<br/>TF-IDF의 대상이 되는 data의 spcl_cnd 열에 결측값에 해당하는 Null 값이 있는지 확인합니다.
<br/>Null 값을 빈 값으로 대체합니다.

"""

# TF-IDF의 대상이 되는 data의 spcl_cnd 열에 결측값에 해당하는 Null 값이 있는지 확인합니다.
# spcl_cnd 열에 존재하는 모든 결측값을 전부 카운트하여 출력합니다.
# print('spcl_cnd 열의 결측값의 수 : ', data['spcl_cnd'].isnull().sum())

# Null 값을 빈 값으로 대체합니다.
# data['spcl_cnd'] = data['spcl_cnd'].fillna('')

"""### 데이터 분석
<br/>spcl_cnd 열에 대해서 TF-IDF 행렬을 구한 후 행렬의 크기를 출력합니다.
<br/>20000개의 문서 벡터에 대하여 상호 간의 코사인 유사도를 구합니다.
"""

# spcl_cnd 열에 대해서 TF-IDF 행렬을 구한 후 행렬의 크기를 출력합니다.
# tfidf = TfidfVectorizer(stop_words = 'english')
# tfidf_matrix = tfidf.fit_transform(data['spcl_cnd'])
# print('TF-IDF 행렬의 크기(shape) : ', tfidf_matrix.shape)

# 20000개의 문서 벡터에 대하여 상호 간의 코사인 유사도를 구합니다.
# cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
# print('코사인 유사도 연산 결과 : ', cosine_sim.shape)

"""### 결과 출력하기
<br/>기존 데이터프레임으로부터 상품코드(fin_prdt_cd)를 key, 약관 내용(fin_prdt_cd_to_index)을 value로 하는 딕셔너리 fin_prdt_cd_to_index를 만들어 둡니다.
<br/>선택한 상품의 제목을 입력하면 코사인 유사도를 통해 가장 spcl_cnd 가 유사한 10개의 상품을 찾아내는 함수를 만듭니다.
"""


def get_recommendations(fin_prdt_cd,rownum,type):
    if type == "deposit":
        get_deposit_data()
    else:
        get_saving_data()
    """# 유사도를 이용한 추천 시스템 구현"""
    data = pd.read_csv(os.getcwd()+"/"+type+"data.csv", low_memory = False)
    """### 데이터 전처리
    <br/>TF-IDF를 연산할 때 데이터에 Null 값이 들어있으면 에러가 발생합니다.
    <br/>TF-IDF의 대상이 되는 data의 spcl_cnd 열에 결측값에 해당하는 Null 값이 있는지 확인합니다.
    <br/>Null 값을 빈 값으로 대체합니다.
    """
    # Null 값을 빈 값으로 대체합니다.
    data['spcl_cnd'] = data['spcl_cnd'].fillna('')
    """### 데이터 분석
    <br/>spcl_cnd 열에 대해서 TF-IDF 행렬을 구한 후 행렬의 크기를 출력합니다.
    <br/>20000개의 문서 벡터에 대하여 상호 간의 코사인 유사도를 구합니다.
    """
    # spcl_cnd 열에 대해서 TF-IDF 행렬을 구한 후 행렬의 크기를 출력합니다.
    tfidf = TfidfVectorizer(stop_words = 'english')
    tfidf_matrix = tfidf.fit_transform(data['spcl_cnd'])
    # 문서 벡터에 대하여 상호 간의 코사인 유사도를 구합니다.
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    fin_prdt_cd_to_index = dict(zip(data['fin_prdt_cd'], data.index))
    idx = fin_prdt_cd_to_index[fin_prdt_cd]

    # 해당 상품와 모든 상품와의 유사도를 가져온다
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 상품들을 정렬한다
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 'rownum' 개의 상품를 받아온다
    sim_scores = sim_scores[1:int(rownum)+1]

    # 가장 유사한 'rownum' 개의 상품의 인덱스를 얻는다
    movie_indices = [idx[0] for idx in sim_scores]

    # 가장 유사한 'rownum'개의 상품의 제목을 리스트에 담는다
    recommended_movies = list(data['fin_prdt_cd'].iloc[movie_indices])

    # 결과를 배열로반환한다
    return recommended_movies

# 사용 예시
# recommendations_json = get_recommendations("00320342",3,"deposit")
# print(recommendations_json)