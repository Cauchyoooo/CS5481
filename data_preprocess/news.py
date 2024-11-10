import json
import os
import prompt

data_dir = '../RawData_news/'

raw_data = []

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

def do_preprocess():
    read_data()
    remove_duplicate_raw_entries()


if __name__ == "__main__":
    do_preprocess()