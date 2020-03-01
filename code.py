from bs4 import BeautifulSoup
import requests

url = 'http://18.207.92.139:8000/random_company'
get_resp = requests.get(url, timeout=5)
content = BeautifulSoup(get_resp.content, "html.parser")

print(content)
