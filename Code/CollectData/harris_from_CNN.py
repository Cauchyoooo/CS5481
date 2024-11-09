import json
import time
import uuid
from datetime import datetime
import requests


def scrawl(url):
    json_data = requests.get(url).json()
    for item in json_data['result']:
        try:
            target = {
                'url': item['url'],
                'title': item['headline'],
                'date': datetime.strptime(item['lastModifiedDate'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d'),
                'summary': item['body']
            }
            data.append(target)
        except Exception as e:
            print(f"处理项目时发生错误: {item}")
            continue


if __name__ == '__main__':
    data = []
    uu_id = None
    start_index = 0
    end_index = 1200
    page_size = 10
    print('begin')
    for i in range(start_index, end_index, page_size):
        uu_id = str(uuid.uuid4())
        full_url = (
            f"https://search.prod.di.api.cnn.io/content?q=Harris&size=10&from={i}&page=1&sort=newest"
            f"&request_id=pdx"
            f"-search-{uu_id}")
        scrawl(full_url)
        time.sleep(0.1)
    print('提取完毕，开始写入')
    json_output = json.dumps(data, ensure_ascii=False, indent=4)
    with open('harris_from_CNN.json', 'w', encoding='utf-8') as f:
        f.write(json_output)
    print('end')
    print(len(data))
