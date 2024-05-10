import pandas


class Money(object):
    def __init__(self, currency, currency_cht, cash_in, cash_out, sign_in, sign_out):
        self.currency = currency
        self.currency_cht = currency_cht
        self.cash_in = cash_in
        self.cash_out = cash_out
        self.sign_in = sign_in
        self.sign_out = sign_out

    @staticmethod
    def search_data():
        data = pandas.read_html("https://www.boc.cn/sourcedb/whpj/")
        currency_table = data[1].iloc[:, 0:5]
        currency_table.columns = ["currency", "cash_buy", "cash_sell", "sight_buy", "sight_sell"]
        cn_to_en = {
            "阿联酋迪拉姆": "AED",
            "澳大利亚元": "AUD",
            "巴西里亚尔": "BRL",
            "加拿大元": "CAD",
            "瑞士法郎": "CHF",
            "丹麦克朗": "DKK",
            "欧元": "EUR",
            "英镑": "GBP",
            "港币": "HKD",
            "印尼卢比": "IDR",
            "印度卢比": "INR",
            "日元": "JPY",
            "韩国元": "KRW",
            "澳门元": "MOP",
            "林吉特": "MYR",
            "挪威克朗": "NOK",
            "新西兰元": "NZD",
            "菲律宾比索": "PHP",
            "卢布": "RUB",
            "沙特里亚尔": "SAR",
            "瑞典克朗": "SEK",
            "新加坡元": "SGD",
            "泰国铢": "THB",
            "土耳其里拉": "TRY",
            "新台币": "TWD",
            "美元": "USD",
            "南非兰特": "ZAR"
        }
        currency_flag_dict = {
            "AED": "https://flagpedia.net/data/flags/normal/ae.png",
            "AUD": "https://flagpedia.net/data/flags/normal/au.png",
            "BRL": "https://flagpedia.net/data/flags/normal/br.png",
            "CAD": "https://flagpedia.net/data/flags/normal/ca.png",
            "CHF": "https://flagpedia.net/data/flags/normal/ch.png",
            "DKK": "https://flagpedia.net/data/flags/normal/dk.png",
            "EUR": "https://flagpedia.net/data/flags/normal/eu.png",
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

        currency_table["currency"] = currency_table["currency"].map(cn_to_en)
        currency_cht = currency_table["currency"].str.extract("(\w+)", expand=True)
        currency_table["currency"] = currency_table["currency"].str.extract("\((\w+)\)", expand=True)
        moneydict = {}
        position = {}
        for i in range(0, 26):
            dollar = currency_table.values[i]
            moneydict[i] = Money(dollar[0], currency_cht.values[i][0], dollar[1], dollar[2], dollar[3], dollar[4])
            position[currency_cht.values[i][0]] = i
        return moneydict, position


