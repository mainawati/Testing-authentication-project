try:
    from flask import Flask,render_template,url_for,request,redirect, make_response
    import random
    import json
    from time import time
    from random import random
    from flask import Flask, render_template, make_response
    from flask_dance.contrib.github import make_github_blueprint, github
  
except Exception as e:
    print("Some Modules are Missings {}".format(e))


app = Flask(__name__)

app.config['SECRET_KEY']='Define_The_Key'
HEX_SEC_KEY= 'd5fb8c4fa8bd46638dadc4e751e0d68d'
app.config['SECRET_KEY']=HEX_SEC_KEY

github_blueprint = make_github_blueprint(client_id='346fe929b99fb2686a62',
                                         client_secret='30a3ad63db0bddcc3309e83da8d454e7bd5fc5a7')

app.register_blueprint(github_blueprint, url_prefix='/github_login')


@app.route('/')
def github_login():

    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            return '<h1>Your Github name is {}'.format(account_info_json['login'])

    return '<h1>Request failed!</h1>'


if __name__ == "__main__":
    app.run(port=3001,debug=True)