import json
import os
import prompt
from openai import OpenAI

data_dir = '../../Data_Collect/Data/'

raw_data = []

cache = open('../Data/news_cache.json', 'w')

llm = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'
)

def get_llm_response(messages):
    response = llm.chat.completions.create(
    model="llama3.1:70b-instruct-q5_K_M",
    messages=messages
    )
    return response.choices[0].message.content

def read_data():
    global raw_data
    for fname in os.listdir(data_dir):
        with open(os.path.join(data_dir, fname)) as f:
            print(f"reading file {fname}")
            raw_data.extend(json.loads(f.read()))
            f.close()
    print("total_raw_entries: ", len(raw_data))

def remove_duplicate_raw_entries():
    global raw_data
    duplicate_removed = []
    url_memory = []
    for entry in raw_data:
        if not entry.get('url') in url_memory:
            url_memory.append(entry.get('url'))
            duplicate_removed.append(entry)
        else:
            continue
    raw_data = duplicate_removed
    print("total_entries_after_remove_duplicate: ", len(raw_data))

def news_tag_relevance():
    global raw_data
    intrested_data = []
    counter = 1
    for entry in raw_data:
        try:
            messages = [
                {"role": "system", "content": prompt.US_PRESIDENTIAL_ELECTION_BG},
                {"role": "system", "content": prompt.NEWS_TAG_RELEVANCE},
                {"role": "user", "content": f"{json.dumps(entry)}"}
            ]
            print("#" * 15 + f'{counter}/{len(raw_data)}' + "#" * 15)
            print(entry.get('title'))
            response = json.loads(get_llm_response(messages))
            print(response)
            relevance_score = int(response.get('relevance_score', 0))
            if relevance_score > 2.5:
                intrested_data.append(entry)
                cache.write(entry)
                cache.write(',\n')
            counter += 1
        except Exception:
            continue
    return intrested_data

def save(data):
    with open('../Data/news.json', 'w') as f:
        f.write(json.dumps(data))
        f.close()

def do_preprocess():
    read_data()
    remove_duplicate_raw_entries()
    intrested_data = news_tag_relevance()
    save(intrested_data)


if __name__ == "__main__":
    do_preprocess()