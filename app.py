from flask import Flask # flaskパッケージの呼び出し

app = Flask(__name__) # おまじない。Flaskのインスタンスを生成している 

@app.route("/") # ブラウザからアクセスがあった時に実行する処理を書いている。ルートにアクセスするとhelloアクションが呼び出されて、hello Flask!をいう文字列を返す。
def hello():
    return "Hello Flask! "

if __name__ == "__main__":# これも決まった書き方らしい。
    app.run(host = '0.0.0.0', port = 5000)