#!/usr/bin/env python
# coding: utf-8

# In[14]:


# 데이터 처리하는 라이브러리 사용하기
import pandas as pd


# In[15]:


# 오라클 연결, 접속, SQL구문 처리 라이브러리
# 먼저 prompt에서 설치 : conda install -c conda-forge cx_Oracle
# pip은 무조건 최신버전 설치, conda(install -c conda-)로 설치하면 버전 적합성을 체크한 후 설치됨 
import cx_Oracle


# In[16]:


# 오라클 연결하기
dsn=cx_Oracle.makedsn('localhost',1521,'xe')    # makedsn : 오라클과 연결하기. 오라클의 주소에 통로 만드는 것
print(dsn)


# In[17]:


# 오라클 접속하기
conn=cx_Oracle.connect('house','dbdb',dsn)
conn


# In[18]:


# <데이터베이스 사용방법>


# In[19]:


# 1. 데이터베이스와 소통할 객체 생성
cursor=conn.cursor()
cursor


# In[20]:


# 2. SQL구문을 커서에 실어서 오라클에 전달(execute)하면,
# 3. 오라클이 SQL구문을 처리한 후.

sql = """
select eve_name, TO_DATE(eve_edate) - TO_DATE(sysdate)||'일 남음' as eve_dday, prod_image, 
        sel_name, prod_name, sal_ratio||'%', To_char(prod_sale,'999,999,999') as "판매가", 
        (Case when del_fee in '0' then '무료배송'
                     else '유료배송'
                     END) as "배송방법"
From seller, prod, delivery, event, sale
Where sel_id = prod_id
AND prod_code = del_code
AND prod_event = eve_code
AND prod_code = sal_code
and eve_name = '오늘의 딜'

"""

cursor.execute(sql)


# In[21]:


# 4. 결과값을 커서에 실어서 보내준다.
# 리스트 형태로 모든 데이터 읽어오기..
row = cursor.fetchall()
print(row)
# 전체 리스트 안에 튜플 형태로 행단위로 들어있다.


# In[22]:


# 컬럼 이름 확인하기
colname=cursor.description
print(colname)
# 데이터베이스의 역할은 끝남 (모든 정보를 다 가져옴) -> 접속을 끊어줘야 함


# In[23]:


# 5. cursor를 닫은 다음, DB와의 연결을 끊어준다
# 커서 반납하기
cursor.close()


# In[24]:


# DB와의 접속 끊기
conn.close()


# In[25]:


col = []
for i in colname :
    col.append(i[0])
print(col)
# 위의 colname은 리스트형태. 거기에서 0번째 값이 모두 이름이었기 때문에 가져옴


# In[26]:


# pandas를 사용한 데이터 프레임 형식으로 변환
emp = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
print(emp)


# In[ ]:





# In[ ]:




