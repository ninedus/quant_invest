# oracle to postgre mig

아래는 Oracle 데이터베이스의 모든 테이블을 PostgreSQL에 생성하고, 각 테이블의 모든 레코드를 PostgreSQL로 복사하는 Python 코드입니다. 이 코드는 cx_Oracle과 psycopg2 라이브러리를 사용합니다. 두 데이터베이스 간의 스키마와 데이터를 동기화하는 데 유용합니다.

<code> mig_oracle_pg.py

# 주요 설명:

1. Oracle 테이블 스키마 가져오기: user_tables와 user_tab_columns를 사용하여 테이블 이름과 컬럼 정보를 가져옵니다.
2. PostgreSQL 테이블 생성: Oracle의 데이터 타입을 PostgreSQL 데이터 타입으로 매핑하여 테이블을 생성합니다.
3. 데이터 복사: Oracle 테이블의 모든 데이터를 가져와 PostgreSQL에 삽입합니다.
4. 에러 처리: 에러 발생 시 롤백하고, 모든 연결을 닫습니다.

요구사항:

- cx_Oracle 및 psycopg2 라이브러리를 설치해야 합니다:
  ```
  pip install cx_Oracle psycopg2
  ```
- Oracle Instant Client가 필요합니다.

Note: 위 코드를 실행하기 전에 Oracle과 PostgreSQL의 연결 정보를 정확히 설정하세요.
