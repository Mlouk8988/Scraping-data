import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/dp/B08CF573K3/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
price = float(soup.find("span", class_="a-offscreen").getText().split("$")[1])
title = soup.find("span", class_="a-size-large product-title-word-break").getText()


if price < 200:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("Your Email", "Your Password")
        connection.sendmail(
            from_addr="Your Email",
            to_addrs="Your Email",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
