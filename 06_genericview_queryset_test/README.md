# Genericview queryset test 

## 들어가며
- 이전 프로젝트에서 현재 7일전 데이터를 출력하는 로직을 작성하는 기능이 있었습니다.
- 다른 팀원이 구현을하고 같이 테스트를 하다가 특이한 사항을 만나서 정리합니다.

## 증상
- 7일전 데이터 까지 가져오는 filter를 queryset에 지정하였는데, 결과값이 예상과 다르게 나왔습니다.

## 테스트
ListCreateAPIView에 다음과 같이 현재 기준으로 30초 이전 product를 출력할 수 있는 queryset을 만들었습니다.
```python
class ProdcutListView(ListCreateAPIView):
    queryset = Product.objects.filter(created_at__range = [datetime.datetime.now() - datetime.timedelta(seconds=30) , datetime.datetime.now()])
    serializer_class = ProdcutSerializer
```
datetime.datetime.now() 의 값은 현재 시간이니 API를 요청하는 시점의 시간으로 설정되기를 기대하고 작성한 쿼리입니다.
하지만 결과를 보면 알겠지만 시각이 고정되어 있는 것을 알 수 있습니다.

```bash
(0.000) SELECT "products"."id", "products"."name", "products"."code", "products"."created_at" FROM "products" WHERE "products"."created_at" BETWEEN '2021-11-17 18:47:45.199577' AND '2021-11-17 18:48:15.199588';
[17/Nov/2021 18:49:11] "GET /products HTTP/1.1" 200 13483

(0.000) SELECT "products"."id", "products"."name", "products"."code", "products"."created_at" FROM "products" WHERE "products"."created_at" BETWEEN '2021-11-17 18:47:45.199577' AND '2021-11-17 18:48:15.199588';
[17/Nov/2021 18:49:12] "GET /products HTTP/1.1" 200 13483

(0.000) SELECT "products"."id", "products"."name", "products"."code", "products"."created_at" FROM "products" WHERE "products"."created_at" BETWEEN '2021-11-17 18:47:45.199577' AND '2021-11-17 18:48:15.199588';
[17/Nov/2021 18:49:12] "GET /products HTTP/1.1" 200 13483
```

저 시간은 아래 로그를 자세히 보면 서버가 켜진 시각인것을 알 수 있습니다.
```bash
November 17, 2021 - 18:53:06
Django version 3.2.5, using settings 'genericview_queryset_test.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.

(0.000) SELECT "products"."id", "products"."name", "products"."code", "products"."created_at" FROM "products" WHERE "products"."created_at" BETWEEN '2021-11-17 18:52:36.668389' AND '2021-11-17 18:53:06.668400';
```

만약 이러한 시간에 따라서 변동되는 값에 대해서 queryset을 세팅하고 싶으면, get_queryset() 함수로 재 정의 하면 됩니다.
```python
def get_queryset(self):
    return Product.objects.filter(created_at__range = [datetime.datetime.now() - datetime.timedelta(seconds=30) , datetime.datetime.now()])
```
둘의 차이점은 쿼리가 만들어지는 시점 인것 같습니다.

내부적으로는 get_queryset() 이 호출되고 그 안에서 만약 현재 사용하고 있는 view에 queryset이 정의가 되어 있으면 queryset을 사용하는 로직으로 되어 있습니다.
```python
    assert self.queryset is not None, (
        "'%s' should either include a `queryset` attribute, "
        "or override the `get_queryset()` method."
         % self.__class__.__name__
    )
``` 

그래서 get_queryset() 을 활용하면 queryset이 필요할때 마다 queryset을 만들기 때문에 유동적으로 변하는 값(시각)에 대해서 대응이 가능한 것 같습니다.

일반적으로는 이러한 경우를 고려하지 않아도 될 것으로 생각됩니다.

```bash
(0.000) SELECT "products"."id", "products"."name", "products"."code", "products"."created_at" FROM "products" WHERE "products"."created_at" BETWEEN '2021-11-17 19:00:01.069274' AND '2021-11-17 19:00:31.069285';
[17/Nov/2021 19:00:31] "GET /products HTTP/1.1" 200 13483

(0.000) SELECT "products"."id", "products"."name", "products"."code", "products"."created_at" FROM "products" WHERE "products"."created_at" BETWEEN '2021-11-17 19:00:02.932611' AND '2021-11-17 19:00:32.932622';
[17/Nov/2021 19:00:32] "GET /products HTTP/1.1" 200 13483

(0.000) SELECT "products"."id", "products"."name", "products"."code", "products"."created_at" FROM "products" WHERE "products"."created_at" BETWEEN '2021-11-17 19:00:04.581676' AND '2021-11-17 19:00:34.581689';
[17/Nov/2021 19:00:34] "GET /products HTTP/1.1" 200 13483
```