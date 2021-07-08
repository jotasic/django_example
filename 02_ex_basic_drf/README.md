## endpoint

1. api/jobs - GET, POST method 허용
   1. GET : 전체 job 조회
   2. POST : job 등록
2. api/jobs/<int:pk> - GET, PUT, DELETE 허용
   1. GET : job 상세페이지
   2. PUT : job 내용 수정
   3. DELETE : job 삭제

## modeling

### JobOffer

1. company_name
2. company_email
3. job_title
4. job_description
5. salary
6. city
7. state
8. created_at
9. available
