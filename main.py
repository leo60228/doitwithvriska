from faker import Faker
from dotenv import load_dotenv
from twocaptcha import TwoCaptcha
import os

load_dotenv()

apikey = os.getenv("2CAPTCHA_APIKEY")
sitekey = "6LclNi8aAAAAAELxL1QpqA4ymERKv1MV7AFGHfbN"
url = "https://www.doitwithoutdues.com/contact"

solver = TwoCaptcha(apiKey=apikey)

fake = Faker()
Faker.seed()


def contact(fake, solver, sitekey, url):
    result = solver.recaptcha(sitekey=sitekey, url=url)
    print(result)


contact(fake, solver, sitekey, url)
