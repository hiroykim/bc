#https://blockchain.info/blocks

import requests
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("금일 생성된 블록을 가져옵니다.")
url = "https://www.blockchain.com/btc/blocks?format=json"
resp = requests.get(url=url)
data = resp.json()

print(data)

# url 지원 없어짐
