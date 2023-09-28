num = int(input("Enter the number of fake names and addresses you want: "))
import faker

# Make a faker object
from faker import Faker
fake = Faker()

# Generate a sample name
for index in range(num):
  fakeName = fake.name()
  print(fakeName)
  fakePlace = fake.address()
  print(fakePlace)
  print()

