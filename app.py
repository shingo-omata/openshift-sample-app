from flask import Flask # flask�p�b�P�[�W�̌Ăяo��

app = Flask(__name__) # ���܂��Ȃ��BFlask�̃C���X�^���X�𐶐����Ă��� 

@app.route("/") # �u���E�U����A�N�Z�X�����������Ɏ��s���鏈���������Ă���B���[�g�ɃA�N�Z�X�����hello�A�N�V�������Ăяo����āAhello Flask!�������������Ԃ��B
def hello():
    return "Hello Flask! "

if __name__ == "__main__":# ��������܂����������炵���B
    app.run(host = '0.0.0.0', port = 5000)