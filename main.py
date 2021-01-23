from faker import Faker

fake = Faker()
Faker.seed()

print(fake.ascii_email())
