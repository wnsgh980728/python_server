from flask import Flask, render_template
from flask import request, redirect, make_response
from aws import detect_labels_local_file as label
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")
@app.route("/compare", methods=["POST"])

def compare():

    try:
        if request.method == "POST":
            # POST

    except:
        return "얼굴 비교 실패"

    return "얼굴 비교 페이지"

@app.route("/detect", methods=["POST"])
def detect():
    try:
        if request.method == "POST":
            f = request.files["file"]

            filename = secure_filename(f.filename)
            # 외부에서 온 이미지, 파일 등을
            # 마음대로 저장할 수 없음
            # 서버에 클라이언트가 보낸 이미지를 저장!!
            f.save("static/" + filename)
            r = label("static/" + filename)
            return r
    except:
        return "감지 실패"

@app.route("/mbti", methods=["POST"])
def mbti():
    try:
        if request.method == "POST":
            mbti = request.form["mbti"]

            return f"당신의 MBTI는 {mbti}입니다"
    except:
        return "데이터 수신 실패"

@app.route("/login", methods=["GET"])
def login():
    try:
        if request.method == "GET":
            # get -> request.args
            login_id = request.args["login_id"]
            login_pw = request.args["login_pw"]

            if (login_id == "nayeho") and (login_pw == "1234"):
                # 로그인 성공 -> 로그인 성공 페이지로 이동
                # nayeho님 환영합니다
                
                response = make_response(redirect("/login/success"))
                response.set_cookie("user", login_id)

                return response
            else:
                # 로그인 실패 -> / 경로로 다시 이동
                return redirect("/")
    except:
        return "로그인 실패"
    
@app.route("/login/success", methods=["GET"])
def login_success():

    login_id = request.cookies.get("user")
    return f"{login_id}님 환영합니다"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
# Ctrl + L하시면 터미널 클리어
