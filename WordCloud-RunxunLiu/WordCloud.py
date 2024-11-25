import json
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 确保下载 nltk 停用词和 VADER 词典
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('punkt')  # 确保下载 punkt 数据包
nltk.download('punkt_tab')  # 确保下载 punkt_tab 数据包

# 创建情绪分析器
sia = SentimentIntensityAnalyzer()

# 扩展停用词列表，包含政治相关的词语
political_stopwords = {
    # 政党相关
    'republican', 'democrats', 'democratic', 'supreme', 'party', 'gop',

    # 政治人物
    'trump', 'harris', 'biden', 'obama', 'clinton',

    # 政治术语
    'election', 'campaign', 'vote', 'voting', 'candidate', 'president',
    'presidential', 'senate', 'congress', 'government', 'policy',

    # 政治地点
    'washington', 'capitol', 'white house',

    # 其他政治相关词
    'political', 'administration', 'debate', 'primary', 'ballot',
    'electoral', 'legislation', 'lawmakers', 'governor', 'senator'
}

# 合并现有的停用词和政治停用词
stop_words = set(stopwords.words('english')).union(political_stopwords)

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
# 处理trump相关数据集
trump_texts = [item['title'] + " " + item['summary'] for item in trump_data]
trump_keywords = []
for text in trump_texts:
    # 使用 word_tokenize 进行分词
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # 提取情绪相关的关键词
    for word in words:
        score = sia.polarity_scores(word)
        if abs(score['compound']) > 0.2:  # 只保留情感强度较强的词
            trump_keywords.append((word, score))

trump_unique_keywords = set([word for word, score in trump_keywords])

# 处理harris相关数据集
harris_texts = [item['title'] + " " + item['summary'] for item in harris_data]
harris_keywords = []
for text in harris_texts:
    # 使用 word_tokenize 进行分词
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # 提取情绪相关的关键词
    for word in words:
        score = sia.polarity_scores(word)
        if abs(score['compound']) > 0.2:  # 只保留情感强度较强的词
            harris_keywords.append((word, score))

harris_unique_keywords = set([word for word, score in harris_keywords])

print("Trump Keywords:", trump_unique_keywords)
print("Harris Keywords:", harris_unique_keywords)


# 步骤3: 对两个数据集分别生成词云并保存
def generate_wordcloud(keywords, name, related_texts):
    word_freq = {}
    for text in related_texts:
        for word in word_tokenize(text.lower()):
            if word in keywords:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1

    # 根据情感得分设置颜色函数
    def color_func(word, **kwargs):
        score = sia.polarity_scores(word)['compound']
        if score > 0:
            return 'green'
        elif score < 0:
            return 'red'
        else:
            return 'gray'

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        color_func=color_func
    ).generate_from_frequencies(word_freq)

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