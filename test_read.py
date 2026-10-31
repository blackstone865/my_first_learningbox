
import requests
import time
with open("dirs.txt","r") as file:
    for line in file:
        clean_word = line.strip()
        fake_url = "http://www.baidu.com/" + clean_word
        response = requests.get(fake_url)
        time.sleep(3)
        print("i'm going to text: ", fake_url)
        print(response.status_code)
