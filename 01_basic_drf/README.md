# 개요

The Complete Guide to Django REST Framework and Vue JS 실습

[강의링크](https://www.udemy.com/course/the-complete-guide-to-django-rest-framework-and-vue-js/)

기본설정은 `13. Introduction to DRF and NewsAPI Project Setup` 참조

구현 범위
- 17. The APIView Class
- 18. Serializers Validation
- 19. The ModelSerializer Class
- 20. How to handle Nested Relationships



# 강의 시작전 환경설정
1.news app만들기
```bash
django-admin startapp news
```

2.INSTALLED_APPS에 rest_freamework 및 news 추가

3. news app에 Article model 만들기 (강의 13참고해서 만들기)

4. super user 만들기
- python manage.py createsuperuser

5. admin 페이지에서 Article model을 접근할 수 있도록 admin.py에 코드 추가
```python
admin.site.register(Article)
```

6. debug 설정
좌측 debug아이콘 클릭해서 launch.json에 들어가서 아래 내용 추가
```python
        {
            "name" : "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "console" : "integratedTerminal",
            "args" : [
                "runserver",
                "--noreload",
                "0:8000"
            ],
            "django": true
        }
```