# Simple Chatbot with python

## install packages
ChatterBot 라이브러리 설치를 위해 pypi 사이트에서 다음 패키지를 수동으로 다운

- python3.9.6 쓰다 위 패키지가 지원하는 버전에 맞지 않아 3.8.10, 3.7.9 설치함, Path에 경로 추가
- 만약 python 인터프리터가 변경이 되면(이는 곧 python 파일이 달라짐을 의미) vscode 아래에서 인터프리터를 변경해야함

관리자 실행 명령 cmd [외부 인터넷 막혀있어 패키지 설치 어려울 때]
```
> pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org 설치할패키지이름
```
- chatterbot_corpus-1.2.0-py2.py3-none-any.whl 
- ChatterBot-1.0.8-py2.py3-none-any.whl
- spacy-3.1.2-cp37-cp37m-win_amd64.whl (chatterbot 실행시 필요한 추가 패키지, 해당 버전을 다운받을때 python 버전에 맞게 살펴볼것, cp'__' _부분이 버전)

C:\Users\USER\AppData\Local\Programs\Python\Python37\lib\site-packages\패키지명\파일명.py

- chatterbot.corpus.korean이 처음에 파일이 없어서 패키지 data안에 corpus 깃헙에서 korean파일 가져와서 다운 받음

<img src="https://user-images.githubusercontent.com/45554623/130724393-679e95f8-dd4c-4bfb-84af-609589263b53.png">