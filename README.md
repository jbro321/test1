1. virtualenv로 가상환경 설치 후 설정
2. django설치
3. django-admin startproject **_이름_**
4. cd **_이름_**
5. django-admin startapp board
6. python manage.py runserver
7. models.py 에 사용자, 비밀번호, dtt 추가
   < 내 db에 반영하기 위해서 migrate 한다. 수정사항이 있으면 8번 9번 반복>
8. python manage.py makemigrations
9. python manage.py migrate
10. sqlite3 db.sqlite3 > .tables > .schema "jpuser" 로 db 확인
11. python manage.py createsuperuser 로 admin 계정 생성
12. admin.py > from .models import Jpuser
