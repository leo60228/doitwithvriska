from faker import Faker
from dotenv import load_dotenv
from twocaptcha import TwoCaptcha
import os
import requests
from argparse import ArgumentParser
from time import sleep

load_dotenv()

apikey = os.getenv("2CAPTCHA_APIKEY")
sitekey = "6LclNi8aAAAAAELxL1QpqA4ymERKv1MV7AFGHfbN"
url = "https://www.doitwithoutdues.com/contact"

solver = TwoCaptcha(apiKey=apikey)

fake = Faker()
Faker.seed()


def contact(fake, solver, sitekey, url, testing=True):
    print("Solving captcha...")

    key = "[KEY]"
    if not testing:
        key_req = requests.post(
            "https://www.doitwithoutdues.com/api/form/FormSubmissionKey", data={}
        )
        key_res = key_req.json()
        key = key_res["key"]
    print("Got key:", key)

    captcha_code = "[CAPTCHA]"
    if not testing:
        captcha_res = solver.recaptcha(sitekey=sitekey, url=url)
        captcha_code = captcha_res.code
    print("Got code:", captcha_code)


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
