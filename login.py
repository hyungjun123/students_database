def login(id, password):
    if id == "admin" and password == "1234":
        return "로그인 성공"
    return "로그인 실패"