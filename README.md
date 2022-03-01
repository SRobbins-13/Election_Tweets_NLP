# Analysis of Gubernatorial Candidate Tweets using NLP Methods

### Abstract
The goal of this analysis is to investigate the social media messaging strategies of the candidates in the recent Virginia and New Jersey gubernatorial elections. The 2021 gubernatorial elections saw a significant swing away from the Democratic party in only a year, and with the midterms coming closer Democrats need to understand what went wrong with their messaging strategy if they want to hold the House and the Senate in 2022. This analysis examines the sentiment, primary topics, and engagement of each candidates tweets during election season to attempt to better understand the larger strategies at use by each candidate and how their message is being perceived.

### Design
The recent gubernatorial elections in Virginia and New Jersey resulted in a ~12pt swing away from the Democratic party since the 2020 election of Joe Biden. The goal of this project is to understand the social media and messaging landscape around the prominent issues and candidates in those races to see what led to that dramatic partisan swing in only a year.

Candidates can benefit from this analysis by using it to direct their messaging strategy. For example, if the analysis shows that the most common twitter topics do not match with what people stated were their motivating issue in the exit polls then candidates can confidently target their message away from the "trending topics" and toward the real "kitchen table" issues. This has the potential to dramatically influence the overall message strategy of both individual candidates and the major party organizations.

### Data
To perform this analysis I pulled the twitter timelines of each candidate, including retweets and quote-tweets, from January 1, 2021 through November 3, 2021 (election day). This ammounted to ~9500 tweets with a corpus total aggregated length of > 250,000 unique terms.

I also pulled datasets that matched Virginia and New Jersey specific search queries and hashtags to assess the public conversation around both elections. These datasets contained >20,000 tweets each, but due to limitations in the Twitter API permissions did not go back beyond the last 7 days (at time of pulling). With this limitation in mind, I propose a workflow that campaigns can use in real time to assess the public conversation around the current election environment and their candidates messaging efficacy.

### Algorithms
**_Data Extraction_**
1. Custom function to pull tweets from individual candidates
2. Custom functino to pull tweets related to specific search query

**_Data Cleaning_**
1. Functions to extract tweet data into usable data frame
2. Custom functions to clean tweet text and break down into tokens

**_Feature Engineering and Natural Language Processing_**
1. Find mentions of particular political figures (e.g. Trump, Biden, candidates opponent) and their count
2. Sentiment Analysis from tweet tokens
3. Topic Modeling of candidate tweets

**_Regression Analysis_**
1. Linear Regression with cross-validation
2. Regression Visualization

### Tools
- Data Collection: Tweepy and Twitter API
- Text Processing: SpaCy and NLTK
- Data Management: Pandas and numpy
- Data Visualization: Matplotlib and seaborn
- Data Modeling: Sklearn and statsmodels

### Communication
I completed a 5-minute presentation of my election message analysis. All visuals and slides are included in this repository.
