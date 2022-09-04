# python django 연습 저장소

    https://wikidocs.net/book/4223



### 가상환경 만드는 명령어
    cd ~/venvs
    python3 -m venv "이름"

### 가상환경 활성화
    source /Users/dongseup_lim/venvs/mysite2/bin/activate

### 가상환경 해제
    deactivate

### 장고 설치
    가상화 활성화
    pip install django==4.0.3

### 프로젝트 행성
    cd 프로젝트 경로로 이동
    django-admin startproject config .

### 앱생성
    django-admin startapp pybo

### 웹서버 실행
    python3 manage.py runserver