from flask import Flask, render_template,request,session,redirect
from modles.money import Money
from modles.user import User
from modles.database import Database

currency_flag_dict = {
    "AED": "https://flagpedia.net/data/flags/normal/ae.png",
    "AUD": "https://flagpedia.net/data/flags/normal/au.png",
    "BRL": "https://flagpedia.net/data/flags/normal/br.png",
    "CAD": "https://flagpedia.net/data/flags/normal/ca.png",
    "CHF": "https://flagpedia.net/data/flags/normal/ch.png",
    "DKK": "https://flagpedia.net/data/flags/normal/dk.png",
    "EUR": "/static/img/european-union.png",
    "GBP": "https://flagpedia.net/data/flags/normal/gb.png",
    "HKD": "https://flagpedia.net/data/flags/normal/hk.png",
    "IDR": "https://flagpedia.net/data/flags/normal/id.png",
    "INR": "https://flagpedia.net/data/flags/normal/in.png",
    "JPY": "https://flagpedia.net/data/flags/normal/jp.png",
    "KRW": "https://flagpedia.net/data/flags/normal/kr.png",
    "MOP": "https://flagpedia.net/data/flags/normal/mo.png",
    "MYR": "https://flagpedia.net/data/flags/normal/my.png",
    "NOK": "https://flagpedia.net/data/flags/normal/no.png",
    "NZD": "https://flagpedia.net/data/flags/normal/nz.png",
    "PHP": "https://flagpedia.net/data/flags/normal/ph.png",
    "RUB": "https://flagpedia.net/data/flags/normal/ru.png",
    "SAR": "https://flagpedia.net/data/flags/normal/sa.png",
    "SEK": "https://flagpedia.net/data/flags/normal/se.png",
    "SGD": "https://flagpedia.net/data/flags/normal/sg.png",
    "THB": "https://flagpedia.net/data/flags/normal/th.png",
    "TRY": "https://flagpedia.net/data/flags/normal/tr.png",
    "TWD": "https://flagpedia.net/data/flags/normal/tw.png",
    "USD": "https://flagpedia.net/data/flags/normal/us.png",
    "ZAR": "https://flagpedia.net/data/flags/normal/za.png"
}

app = Flask(__name__)
app.secret_key="elio"

Database.initialize()

@app.route("/")
def home():

    moneydict, position = Money.search_data()
    print(moneydict)
    return render_template("home.html",moneydict=moneydict,position=position,currency_flag_dict=currency_flag_dict)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['InputName']
        email = request.form['InputEmail']
        password = request.form['InputPassword']
        result = User.register_user(name, email, password)
        if result is True:
            session['email'] = email
            session['name'] = name
            return redirect("/")
        else:
            message = "這個電子郵件已經存在過了"
            return render_template("register.html", message=message)
    else:
        return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['InputEmail']
        password = request.form['InputPassword']
        result = User.check_user(email, password)
        if result is True:
            session['email'] = email
            session['name'] = User.find_user_data(email)['name']

            return redirect("/")
        else:
            message = "您的電子信箱或是密碼錯誤 !!"
            return render_template("login.html", message=message)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session['email'] = None
    session['name'] = None
    return redirect("/")

@app.route("/new_alert", methods=["GET", "POST"])
def new_alert():
    if session['email']:
        moneydict, position = Money.search_data()
        if request.method == 'POST':
            input_currency = request.form['input_currency']
            rate_exchange = request.form['rate_exchange']
            bank_buy = request.form['bank_buy']
            bank_sale = request.form['bank_sale']
            result = All_alert.create_alert(session['email'], input_currency, rate_exchange, [bank_buy, bank_sale])
            if result is True:
                message = "新增成功 !! 您的通知已成功建立,可以繼續新增 !!"
                currency_msg = "幣別 : {}".format(input_currency)
                exchange_msg = "匯率 : {}".format("現金匯率" if rate_exchange == "cash" else "即期匯率")
                buy_msg = "銀行買入通知價格 : $ {}".format(bank_buy)
                sale_msg = "銀行賣出通知價格 : $ {}".format(bank_sale)
                return render_template("new_alert.html", moneydict=moneydict, message=message,
                                       currency_msg=currency_msg, exchange_msg=exchange_msg, buy_msg=buy_msg,
                                       sale_msg=sale_msg)
            else:
                message = "新增失敗 !! 通知已建立過 (每個幣別只能對應兩種匯率) ,請重新新增 !!"
                currency_msg = "幣別 : {}".format(input_currency)
                exchange_msg = "匯率 : {}".format("現金匯率" if rate_exchange == "cash" else "即期匯率")
                buy_msg = "銀行買入通知價格 : $ {}".format(bank_buy)
                sale_msg = "銀行賣出通知價格 : $ {}".format(bank_sale)
                return render_template("new_alert.html", moneydict=moneydict, message=message,
                                       currency_msg=currency_msg, exchange_msg=exchange_msg, buy_msg=buy_msg,
                                       sale_msg=sale_msg)
        else:
            return render_template("new_alert.html", moneydict=moneydict)
    else:
        return redirect("/login")




if __name__ == "__main__":
    app.run(debug=True)