from faker import Faker
from dotenv import load_dotenv
from twocaptcha import TwoCaptcha
import os
import requests
import random
import json
from argparse import ArgumentParser
from time import sleep

load_dotenv()

apikey = os.getenv("2CAPTCHA_APIKEY")
sitekey = "6LclNi8aAAAAAELxL1QpqA4ymERKv1MV7AFGHfbN"
url = "https://www.doitwithoutdues.com/contact"
names = [
    ["John", "Egbert"],
    ["June", "Egbert"],
    ["Rose", "Lalonde"],
    ["Dave", "Strider"],
    ["Jade", "Harley"],
    ["Aradia", "Megido"],
    ["Tavros", "Nitram"],
    ["Sollux", "Captor"],
    ["Karkat", "Vantas"],
    ["Nepeta", "Leijon"],
    ["Kanaya", "Maryam"],
    ["Terezi", "Pyrope"],
    ["Vriska", "Serket"],
    ["Equius", "Zahhak"],
    ["Gamzee", "Makara"],
    ["Eridan", "Ampora"],
    ["Feferi", "Peixes"],
    ["Jane", "Crocker"],
    ["Roxy", "Lalonde"],
    ["Dirk", "Strider"],
    ["Jake", "English"],
    ["Damara", "Megido"],
    ["Rufioh", "Nitram"],
    ["Kankri", "Vantas"],
    ["Meulin", "Leijon"],
    ["Porrim", "Maryam"],
    ["Latula", "Pyrope"],
    ["Aranea", "Serket"],
    ["Horuss", "Zahhak"],
    ["Kurloz", "Makara"],
    ["Cronos", "Ampora"],
    ["Meenah", "Peixes"],
    ["Callie", "Ohpeee"],
    ["Lord", "English"],
    ["Doc", "Scratch"],
    ["Harryanderson", "Egbert"],
    ["Vriska", "Maryamlalonde"],
    ["Vrissy", "Maryamlalonde"],
    ["Tavros", "Crocker"],
    ["Yiffanylongstocking", "Lalondeharley"],
]

solver = TwoCaptcha(apiKey=apikey)

fake = Faker()
Faker.seed()


def contact(fake, solver, sitekey, url, testing=True):
    print("Getting key...")

    key = "[KEY]"
    if not testing:
        key_req = requests.post(
            "https://www.doitwithoutdues.com/api/form/FormSubmissionKey", data={}
        )
        key_res = key_req.json()
        key = key_res["key"]
    print("Got key:", key)

    print("Solving captcha...")

    captcha_code = "[CAPTCHA]"
    if not testing:
        captcha_res = solver.recaptcha(sitekey=sitekey, url=url)
        captcha_code = captcha_res.code
    print("Got code:", captcha_code)

    [first, last] = random.choice(names)
    print("Name:", first, last)

    subject = fake.sentence()

    print("Subject:", subject)

    body = fake.paragraph()

    email = fake.ascii_email()
    form = {
        "name-yui_3_17_2_1_1608299661315_3805": [first, last],
        "email-yui_3_17_2_1_1608299661315_3806": email,
        "text-yui_3_17_2_1_1608299661315_3807": subject,
        "textarea-yui_3_17_2_1_1608299661315_3808": body,
    }
    form_json = json.dumps(form)
    print("Form:", form_json)

    body = {
        "captchaKey": captcha_code,
        "collectionId": "5fdcb4877ff8e90c28ffb603",
        "contentSource": "c",
        "form": form_json,
        "formId": "5fdcb49a07858c174a49adc7",
        "key": key,
        "objectName": "page-5fdcb4877ff8e90c28ffb603",
        "pageId": "5fdcb4877ff8e90c28ffb603",
        "pagePath": "/contact",
        "pagePermissionTypeValue": 1,
        "pageTitle": "CONTACT",
    }

    if not testing:
        requests.post(
            "https://www.doitwithoutdues.com/api/form/SaveFormSubmission", data=body
        )
        print("Sent!")
    else:
        print(body)


parser = ArgumentParser()
parser.add_argument("--real", action="store_true")
args = parser.parse_args()

if args.real:
    while True:
        try:
            contact(fake, solver, sitekey, url, False)
        except:
            print("Error:", sys.exc_info()[0])
            sleep(1)
else:
    contact(fake, solver, sitekey, url, True)
