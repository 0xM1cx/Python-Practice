import requests
from time import sleep


# contactNumbers = ["9366492551", "9164265322", "9619381867", "9771062549", "9100775142"]

def sendMessage(text, number):
    url = "https://sms77io.p.rapidapi.com/sms"
    payload = f"to=%2B63{number}&p=cbBoDzCNge5jYGxIHnLwJp8XEh9NR4wMrAlJh5S3PKTCXEfhGUVsElWo4ZSWHwAd&text={text}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "12846a6964msh1f5fb87de8ffe4dp1a7b3ajsn49458b66685f",
        "X-RapidAPI-Host": "sms77io.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)



def main(numbers):
    text = input("Write the Message you want to send: ")
    # print("In writing the number don't  ")
    # number = input("Number of the receiptient: ")
    _text = text.replace(" ", "%20")
    # for i in numbers:
    #     print(f"Sending to {i}")
    #     sleep(5)
    #     sendMessage(_text, i)
    sendMessage(_text, number="9914857904")

main()