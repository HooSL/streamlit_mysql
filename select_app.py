import streamlit as st
import mysql.connector
from mysql.connector import connection
from mysql.connector.errors import DatabaseError, Error

from mysql_connection import get_connection

def run_select_app():
    st.subheader('데이터 조회')
    #연결하는 코드
    #try 라고 나오면 들여쓰기 되어있는 문장들을 실행하라는 뜻
    
    try:
        connection = get_connection()

        #1. id,email,age,address 데이터 조회
        
        query = ''' select id,email,age,address from test_user;'''

        #셀렉트 결과 가져오는 경우
        cursor = connection.cursor()
        cursor.execute(query)

        # select문은 아래 내용이 필요하다.
        record_list = cursor.fetchall()
        print(record_list)

        #데이터 하나씩 액세스해서 보기
        for row in record_list:
            st.write(row)
            
        #2. id를 검색하면 해당 데이터만 조회
        st.subheader('ID로 조회')

        id = st.number_input('ID를 입력하세요.',min_value=1)
        query = '''select id, email, age, address from test_user where id = %s'''
        record = (id,)
        cursor.execute(query,record)
         # select문은 아래 내용이 필요하다.
        record_list = cursor.fetchall()
        print(record_list)

        #데이터 하나씩 액세스해서 보기
        for row in record_list:
            st.write(row)

        #3. 이메일 항목에서 검색하는 기능
        st.subheader('E-mail 검색')
        search_word = st.text_input('검색어 입력')
        if st.button('검색하기!'):
            query = '''select id, email, age, address from test_user where email like '%''' + search_word+'''%';'''
            
            cursor.execute(query)
            # select문은 아래 내용이 필요하다.
            record_list = cursor.fetchall()
            print(record_list)

        #데이터 하나씩 액세스해서 보기
            for row in record_list:
                st.write(row)





    #위의 코드를 실행하다가 문제가 생시면 except를 실행하라는 뜻
    except Error as e :
        print('Error while connecting to MySQL',e)
    #finally는 try에서 에러가 나든 안나든 무조건 실행하라는 뜻
    finally :
        cursor.close()
        if connection.is_connected():
            connection.close()
            print('MySQL connection is closed')
        else:
            print('connection does not exist')
















