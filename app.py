import flask, flask_login, bpgUsers, werkzeug, os
from check_db import *
from check_news import *

UPLOAD_FOLDER = 'E:\\Scripts\\uploads\\'

app = flask.Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'N2Nconnect123'  # Change this!
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
#flask_login.login_user(remember=True)

users = {'bnadmin': {'password': 'N2Nconnect123'},
			'0138811': {'password': 'Liverp00l'},
            'palida': {'password': 'Bisnews0123'}}

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return
    user = User()
    user.id = email
    return user

@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return flask.render_template('e500.html'), 500

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return
    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if flask.request.method == 'GET':
        return flask.render_template("index_login.html")
#    flask_login.login_user(user='email',remember=True)
    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('BPChartBOT'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

@app.route('/')
def home():
    result = ["Hello World!!!"]
    return flask.redirect(flask.url_for('login'))
    
@app.route('/BPChartBOT', methods=('GET','POST'))
@flask_login.login_required
def bp_chart_bot():
    if flask.request.method == 'GET':
        return flask.render_template("bp_chart_bot.html",Data = flask_login.current_user.id)
    else:
        select = flask.request.form['select']
        if select == '10':
            result = BP_CHART_BOT()
            return flask.render_template("bp_chart_bot.html",Data=result)
        elif select == '11':
            result = BP_CHART_BOT1()
            return flask.render_template("bp_chart_bot.html",Data=result)
        elif select == '12':
            result = BP_CHART_BOT2()
            return flask.render_template("bp_chart_bot.html",Data=result)
        elif select == '13':
            result = BP_CHART_BOT3()
            return flask.render_template("bp_chart_bot.html",Data=result)
        elif select == '14':
            result = BP_CHART_BOT4()
            return flask.render_template("bp_chart_bot.html",Data=result)

@app.route('/News', methods=('GET','POST'))
@flask_login.login_required
def news():
    if flask.request.method == 'GET':
        return flask.render_template("news.html",Data = flask_login.current_user.id)
    else:
        select = flask.request.form['select']            
        if select == '65':
            newsInfo = flask.request.form['value4']
            result = hiddenNews(newsInfo)
            answer = "Your News ID: "+newsInfo+" request have already been done"
            return flask.render_template("news_result.html",Data = flask_login.current_user.id,Data2 = answer,Data3=result)
        elif select == '66':
            newsInfo = flask.request.form['value4']
            result = activatedNews(newsInfo)
            answer = "Your News ID: "+newsInfo+" request have already been done"
            return flask.render_template("news_result.html",Data = flask_login.current_user.id,Data2 = answer,Data3=result)
        elif select == '67':
            newsInfo = flask.request.form['value4']
            result = queryNewsH(newsInfo)
            answer = "Your query Headline: "+newsInfo+" have already been done"
            return flask.render_template("news_result.html",Data = flask_login.current_user.id,Data2 = answer,Data3=result)
            #return flask.render_template("news.html",Data = result2)


@app.route('/BPChartBackdate', methods=('GET','POST'))
@flask_login.login_required
def bp_chart_backdate():
    if flask.request.method == 'GET':
        return flask.render_template("bp_chart_backdate.html",Data = flask_login.current_user.id)
    else:
        select = flask.request.form['select']            
        if select == '15':
            stkCode = flask.request.form['value1']
            beginDate = flask.request.form['value2']
            endDate = flask.request.form['value3']
            result = BP_CHART_BACK_DATE(stkCode,beginDate,endDate)
            return flask.render_template("form.html",Data=result)
            
@app.route('/BPChartExchange', methods=('GET','POST'))
@flask_login.login_required
def bp_chart_exchange():
    if flask.request.method == 'GET':
        return flask.render_template("bp_chart_exchg.html",Data = flask_login.current_user.id)
    else:
        select = flask.request.form['select']           
        if select == '18':
            result = BP_CHART_EXCH231()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '19':
            result = BP_CHART_EXCH232()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '20':
            result = BP_CHART_EXCHG_136()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '21':
            result = BP_CHART_EXCHG_141()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '22':
            result = BP_CHART_EXCHG_161()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '23':
            result = BP_CHART_EXCHG_168()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '24':
            result = BP_CHART_EXCHG_169()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '25':
            result = BP_CHART_EXCHG_17()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '26':
            result = BP_CHART_EXCHG_174()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '27':
            result = BP_CHART_EXCHG_175()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '28':
            result = BP_CHART_EXCHG_177()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '29':
            result = BP_CHART_EXCHG_179()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '30':
            result = BP_CHART_EXCHG_180()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '31':
            result = BP_CHART_EXCHG_181()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '32':
            result = BP_CHART_EXCHG_184()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '33':
            result = BP_CHART_EXCHG_185()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '34':
            result = BP_CHART_EXCHG_186()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '35':
            result = BP_CHART_EXCHG_194()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '36':
            result = BP_CHART_EXCHG_195()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '37':
            result = BP_CHART_EXCHG_196()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '38':
            result = BP_CHART_EXCHG_198()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '39':
            result = BP_CHART_EXCHG_199()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '40':
            result = BP_CHART_EXCHG_211()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '41':
            result = BP_CHART_EXCHG_212()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '42':
            result = BP_CHART_EXCHG_212_1()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '43':
            result = BP_CHART_EXCHG_213()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '44':
            result = BP_CHART_EXCHG_213_1()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '45':
            result = BP_CHART_EXCHG_215()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '46':
            result = BP_CHART_EXCHG_233()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '47':
            result = BP_CHART_EXCHG_241()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '48':
            result = BP_CHART_EXCHG_34()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '49':
            result = BP_CHART_EXCHG_35()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '50':
            result = BP_CHART_EXCHG_4()
            return flask.render_template("bp_chart_exchg.html",Data=result)

        elif select == '51':
            result = BP_CHART_EXCHG_62()
            return flask.render_template("bp_chart_exchg.html",Data=result)

@app.route('/BPChartETC', methods=('GET','POST'))
@flask_login.login_required
def bp_chart_etc():
    if flask.request.method == 'GET':
        return flask.render_template("bp_chart_etc.html",Data = flask_login.current_user.id)
    else:
        select = flask.request.form['select']           
        if select == '16':
            result = BP_CHART_ECO()
            return flask.render_template("bp_chart_etc.html",Data=result)

        elif select == '17':
            result = BP_CHART_EOD2()
            return flask.render_template("bp_chart_etc.html",Data=result)            

        elif select == '52':
            result = BP_CHART_FOREX()
            return flask.render_template("bp_chart_etc.html",Data=result)

        elif select == '53':
            result = BP_CHART_MKTCAP()
            return flask.render_template("bp_chart_etc.html",Data=result)

        elif select == '54':
            result = BP_CHART_NAV()
            return flask.render_template("bp_chart_etc.html",Data=result)

        elif select == '55':
            result = BP_CHART_NAV2_MANULITE()
            return flask.render_template("bp_chart_etc.html",Data=result)

        elif select == '56':
            result = BP_CHART_OIL()
            return flask.render_template("bp_chart_etc.html",Data=result)

        elif select == '57':
            result = BP_CHART_SETTSUM()
            return flask.render_template("bp_chart_etc.html",Data=result)

        elif select == '58':
            result = BP_CHART_STOCKSTAT1()
            return flask.render_template("bp_chart_etc.html",Data=result)

        elif select == '59':
            result = BP_CHART_STOCKSTAT2()
            return flask.render_template("bp_chart_etc.html",Data=result)

        elif select == '60':
            result = BP_CHART_T0100()
            return flask.render_template("bp_chart_etc.html",Data=result)

        elif select == '61':
            result = BP_CHART_T0630()
            return flask.render_template("bp_chart_etc.html",Data=result)

        elif select == '62':
            result = BP_CHART_T1010()
            return flask.render_template("bp_chart_etc.html",Data=result)

        elif select == '63':
            result = BP_CHART_ThaiGOLD()
            return flask.render_template("bp_chart_etc.html",Data=result)

        elif select == '64':
            result = BP_CHART_WARRANT()
            return flask.render_template("bp_chart_etc.html",Data=result)

        else:
            result = ''
            return flask.render_template("bp_chart_etc.html",Data=result)

@app.route('/BPGUsers', methods=('GET','POST'))
@flask_login.login_required
def queryBPGUsers():
    if flask.request.method == 'GET':
        return flask.render_template("bpg_user.html", Data=flask_login.current_user.id)
    else:
        select = flask.request.form['select']
        if select == '68':
            status = flask.request.form['status']
            answer = "Users Status :"
            result = bpgUsers.queryUsersStatus('A') if status == '1001' else bpgUsers.queryUsersStatus('S')
            return flask.render_template("bpg_user_status.html", Data=flask_login.current_user.id,Data2=answer,Data3=result)

@app.route('/suspenseUsers', methods=('GET','POST'))
@flask_login.login_required
def upload_file():
    return flask.render_template('bpg_user_suspense_account.html',Data=flask_login.current_user.id)

@app.route('/suspenseUsersbyAccount', methods=('GET', 'POST'))
@flask_login.login_required
def querySuspenseUsers():
    if flask.request.method == 'POST':
        f = flask.request.files['uploadFile']
        f.save(UPLOAD_FOLDER+werkzeug.utils.secure_filename(f.filename))
        answer = bpgUsers.suspenseUsersbyAccount()
        result = bpgUsers.queryUsersSuspensebyAccount()
    return flask.render_template('bpg_user_suspense_by_account.html',Data=flask_login.current_user.id,Data2=answer,Data3=result)


if __name__ == '__main__':
    app.run(debug='True',host='0.0.0.0',port='8080')