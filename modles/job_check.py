from modles.money import Money
from modles.database import Database
import requests

def check_alert():
    moneydict, position = Money.search_data()
    all_user = []
    data = Database.find_all(collection="users")
    for user in data:
        all_user.append(user["email"])
    for user in all_user:
        print(user)
        message = []
        user_all_alert = Database.find(collection="all_alert", query={"email": user})
        for user_alert in user_all_alert:
            if user_alert["rate_exchange"] == "cash":
                if moneydict[position[user_alert["currency"]]].cash_in != "-":
                    if float(user_alert["price"][0]) >= float(moneydict[position[user_alert["currency"]]].cash_in):
                        if user_alert["currency"] not in message:
                            message.append(user_alert["currency"])
                        else:
                            pass
                    elif moneydict[position[user_alert["currency"]]].cash_out != "-":
                        if float(user_alert["price"][0]) <= float(moneydict[position[user_alert["currency"]]].cash_out):
                            if user_alert["currency"] not in message:
                                message.append(user_alert["currency"])
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                elif moneydict[position[user_alert["currency"]]].cash_out != "-":
                    if float(user_alert["price"][0]) <= float(moneydict[position[user_alert["currency"]]].cash_out):
                        if user_alert["currency"] not in message:
                            message.append(user_alert["currency"])
                        else:
                            pass
                    else:
                        pass
                else:
                    pass

            if user_alert["rate_exchange"] == "sign":
                if moneydict[position[user_alert["currency"]]].sign_in != "-":
                    if float(user_alert["price"][1]) >= float(moneydict[position[user_alert["currency"]]].sign_in):
                        if user_alert["currency"] not in message:
                            message.append(user_alert["currency"])
                        else:
                            pass
                    elif moneydict[position[user_alert["currency"]]].sign_out != "-":
                        if float(user_alert["price"][1]) <= float(moneydict[position[user_alert["currency"]]].sign_out):
                            if user_alert["currency"] not in message:
                                message.append(user_alert["currency"])
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                elif moneydict[position[user_alert["currency"]]].sign_out != "-":
                    if float(user_alert["price"][1]) <= float(moneydict[position[user_alert["currency"]]].sign_out):
                        if user_alert["currency"] not in message:
                            message.append(user_alert["currency"])
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        print(user,":",message)
        requests.post(

            # 下面為範例連結要有check_alert()需自行更改
            "https://api.mailgun.net/v3/sandbox87d3013e6d57453fab608b61f689993b.mailgun.org/messages",
            # 下面為範例連結要有check_alert()需自行更改
            auth=("api", "key-33b1738475c22f210fd2a91be2a6db95"),
            # 下面為範例連結要有check_alert()需自行更改
            data={"from": "Mailgun Sandbox <postmaster@sandbox87d3013e6d57453fab608b61f689993b.mailgun.org>",

                  # "to": "kevinhe <kevin.hiskio@gmail.com>",
                  "to": user,
                  "subject": "外幣通知",
                  "text": "目前符合調的外幣為:{},請盡快至關網查看!".format(str(message).strip("[]"))})

# **測試使用**
# Database.initialize()
# check_alert()
# **測試使用**