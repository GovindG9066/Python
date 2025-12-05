import re

email="Gadekargovind575@gmail.com"
pattern=r"^[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.match(pattern,email):
    print("Valid Email")
else:
    print("Invalid Email")


print("Next...")

url="https://www.google.com"
pattarnURL=r"^https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.match(pattarnURL,url):
    print("Valid URL",url)
else:
    print("Invalid URL")