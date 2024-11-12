import json
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 确保下载 nltk 停用词和 VADER 词典
nltk.download('stopwords')
nltk.download('vader_lexicon')

# 创建情绪分析器
sia = SentimentIntensityAnalyzer()

# 步骤1: 加载数据
with open('../Data_Preprocess/Data/news.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 将数据按照是否包含trump和harris分成两个数据集，确保不包含对方名字
trump_data = []
harris_data = []
for item in data:
    title_summary = item['title'] + " " + item['summary']
    if 'trump' in title_summary.lower() and 'harris' not in title_summary.lower():
        trump_data.append(item)
    elif 'harris' in title_summary.lower() and 'trump' not in title_summary.lower():
        harris_data.append(item)

# 步骤2: 对两个数据集分别进行文本预处理及提取情绪关键词
stop_words = set(stopwords.words('english'))

# 处理trump相关数据集
trump_texts = [item['title'] + " " + item['summary'] for item in trump_data]
trump_keywords = []
for text in trump_texts:
    # 分词和小写化
    words = text.lower().split()
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # 提取情绪相关的关键词
    for word in words:
        score = sia.polarity_scores(word)
        if score['compound']!= 0:
            trump_keywords.append((word, score))

trump_unique_keywords = set([word for word, score in trump_keywords])

# 处理harris相关数据集
harris_texts = [item['title'] + " " + item['summary'] for item in harris_data]
harris_keywords = []
for text in harris_texts:
    # 分词和小写化
    words = text.lower().split()
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # 提取情绪相关的关键词
    for word in words:
        score = sia.polarity_scores(word)
        if score['compound']!= 0:
            harris_keywords.append((word, score))

harris_unique_keywords = set([word for word, score in harris_keywords])

print("Trump Keywords:", trump_unique_keywords)
print("Harris Keywords:", harris_unique_keywords)

# 步骤3: 对两个数据集分别生成词云并保存
def generate_wordcloud(keywords, name, related_texts):
    word_freq = {}
    for text in related_texts:
        for word in text.lower().split():
            if word in keywords:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1

    # 根据情感得分设置颜色函数
    color_func = lambda word, **kwargs: 'green' if sia.polarity_scores(word)['compound'] >= 0 else'red'

    wordcloud = WordCloud(width=800, height=400, background_color='white', color_func=color_func).generate_from_frequencies(word_freq)

    # 保存词云图像
    wordcloud_filename = f"{name}_emotion_wordcloud.png"
    wordcloud.to_file(wordcloud_filename)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # 关闭坐标轴
    plt.title(f"{name} Emotion-related Keywords Word Cloud")
    plt.show()

# 生成并保存trump相关的词云
generate_wordcloud(trump_unique_keywords, "Trump", trump_texts)

# 生成并保存harris相关的词云
generate_wordcloud(harris_unique_keywords, "Harris", harris_texts)