#https://bitnodes.earn.com/api/v1/sanpshots/?limit=100&page=1
#https://bitnodes.io/api/v1/snapshots/?limit=100&page=1

import requests
import time
import matplotlib.pyplot as plt

nPage = 100
if nPage > 100:
    print("요청 페이지가 너무 많아 시간이 오래 걸립니다.")
else:
    t = []
    n = []
    for page in range(1, nPage):
        url = 'https://bitnodes.io/api/v1/snapshots/?limit=100&page=' + str(page)
        resp = requests.get(url=url)
        data = resp.json()
        print("page %d loaded." % page)

        for i in range(len(data['results'])):
            ts = time.gmtime(data['results'][i]['timestamp'])
            t.append(time.strftime("%Y-%m-%d %H:%M:%S", ts))
            n.append(data['results'][i]['total_nodes'])

    #역순으로 뒤집기
    t = t[::-1]
    n = n[::-1]
    #print(t)
    #print(n)

    # 최근 노드수의 변화를 확인한다.
    plt.figure(figsize=(8,6))
    plt.plot(n, color='red', linewidth=0.7)
    plt.title('Bitcoin Nodes\n' + t[0] + '~' + t[-1] )
    plt.grid(color='green', alpha=0.2)
    plt.show()
