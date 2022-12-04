# 이지오더 API

## 개발 현황:
- [X] 가게 만들기 API
- [X] 주문하기 API
- [x] 직원호출 API
- [x] 가게 삭제 API
- [o] 메뉴 확인 API

# 가게 만들기 API
### 가게 만들기 <br>
호출타입: **GET REQUEST**
```json

{
  "result": "success!"
}

```

URL/api/makestore/{가게이름}/{가게 테이블 수}/<br>
[예시](https://easyorderAPI.seungwoohan0104.repl.co/api/makestore/test/3)

# 주문하기 API
### 주문하기 <br>
호출타입: **GET REQUEST**
```json

{
  "result": "success!"
}

```

URL/api/order/{가게이름}/{시킨 테이블}/{메뉴이름}/{메뉴가격}/<br>
[예시](https://easyorderAPI.seungwoohan0104.repl.co/api/order/test/2/제육볶음/5000)

# 직원호출 API
### 직원 호출하기 <br>
호출타입: **GET REQUEST**
```json

{
  "result": "success!"
}

```

URL/api/order/{가게이름}/{호출 테이블}/<br>
[예시](https://easyorderAPI.seungwoohan0104.repl.co/api/call/test/2/)

# 가게삭제 API
### 가게 삭제하기 <br>
호출타입: **GET REQUEST**
```json

{
  "result": "success!"
}

```

URL/api/deletestore/{가게이름}/<br>
[예시](https://easyorderAPI.seungwoohan0104.repl.co/api/deletestore/test/)
