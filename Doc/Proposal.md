# Proposal: Timeline Generation

## 1 Introduction

### 1.1 Background

The U.S. presidential election is a major global event, and its process and outcomes have profound impacts on international politics and economics. With the rise of social media, the speed and breadth of election-related information dissemination have significantly increased.

### 1.2 Motivation

Information on website is often fragmented, making it difficult to fully understand the evolution of events. Creating a clear event timeline can help people better understand the dynamics of the election.

### 1.3 Goal

The main goal of this project is to **generate a detailed timeline of U.S. election events** by collecting and analyzing website data, thereby helping users track and understand key events in the election process. Through this project, we will acquire comprehensive data engineering skills, including practical experience in data collection, management, analysis, visualization, and application development. These skills are crucial for understanding and handling large-scale datasets and generating meaningful analytical results.

## 2 Methods

### 2.1 Data Collection

- Establish keywords (e.g., #Election2024, #PresidentialDebate) and time ranges (e.g., primaries, national conventions, debates, and election day) to ensure data relevance and timeliness.
- Utilize news platforms like BBC, CNN and The New York Times for data scraping. It's not easy to scrap datas on social media like Twitter(X) or Facebook for their anti-scrap technique.

### 2.2 Event Detection

- Apply time-based event detection methods, such as clustering and natural language processing (NLP) techniques, to identify and extract important events.
- Reference literature like Twevent and real-time event detection technologies to optimize the accuracy of event detection if possible.

### 2.3 Timeline Generation

- Organize detected events into a chronological timeline, integrating time, event descriptions, and news sources.
- Address overlapping data from different sources to ensure the timeline's accuracy and completeness.

## 3 Experiments

### 3.1 Process

~~~mermaid
graph TD

A["Define the Scope and Keywords"] --> B["Data Collection"]
B --"Data Preprocess"--> F["Organized Data"]
F --"Implement Event Detection Algorithms"--> C["Event Detection"]      
C --> D["Timeline Generation"]      
D --> E["Visualization"]
A1["Identify key events and milestones"] --- A      
A2["Determine relevant keywords and hashtags"] --- A       
B1["Crawling Website"] --- B      
B2["Data Filtering"] --- B              
D1["Include Node Information"] --- D      
D2["Perform Data Deduplication"] --- D       
E1["Create visual representation"] --- E       
~~~

(1) **Define the Scope and Keywords**:

This initial step involves identifying key events and milestones relevant to the project (A1) and determining relevant keywords and hashtags (A2). These elements are essential to set the boundaries and focus for data collection.

(2) **Data Collection**:

Data is gathered by crawling websites (B1) and applying data filtering techniques (B2) to ensure the relevance of the collected information. The collected data then undergoes preprocessing to become organized data (F).

(3) **Organized Data**:

After preprocessing, the data becomes structured, making it ready for further analysis.

(4) **Event Detection**:

Event detection algorithms are implemented on the organized data. This step involves applying specific algorithms to identify and categorize significant events within the data (C).

(5) **Timeline Generation**:

For the timeline generation, node information is included (D1) and data deduplication is performed (D2) to ensure accuracy and clarity of the resulting timeline (D).

(6) **Visualization**:

Finally, a visual representation of the timeline is created (E1), enabling easy interpretation and presentation of the information (E).

### 3.2 Tools and Technologies

- Utilize technological tools like Python and Jupyter Notebook.
- Employ existing APIs and scraping tools (e.g., Scrapy, Tweepy) for data collection.
- Use NLP Models for event detection.
- Libraries such as D3.js or TimelineJS can be used to create interactive and visually appealing timelines.