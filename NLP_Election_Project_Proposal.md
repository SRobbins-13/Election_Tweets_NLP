# Unsupervised Natural Language Processing Project Proposal
Samuel Robbins

#### Question/Premise
The recent gubernatorial elections in Virginia and New Jersey resulted in a ~10pt swing away from the Democratic party since the 2020 election of Joe Biden. The goal of this project is to understand the social media and messaging landscape around the prominent issues and candidates in those races to see what led to that dramatic partisan swing in only a year.

Candidates can benefit from this analysis by using it to direct their messaging strategy. For example, if the analysis shows that the most common twitter topics do not match with what people stated were their motivating issue in the exit polls then candidates can confidently target their message away from the "trending topics" and toward the real "kitchen table" issues. This has the potential to dramatically influence the overall message strategy of both individual candidates and the major party organizations.

#### Data Description
I plan to use tweets scraped using the twitter API from June (the party primaries) to November (the general election) that mention the issues or candidates in those key races. An individual sample in this analysis will be individual tweets. I will use topic modeling to determine which topics (e.g. education, the economy, covid, etc.) were the most salient during the election, and sentiment analysis to determine how different communities felt about each of those topics.

I plan to examine this problem from two standpoints. First, I will look at the tweets from the general election candidates to get the overall sentiment of their messaging strategy. Next, I will examine a larger dataset of tweet from general twitter users who mentioned the candidates, races, or issues at play to determine which issues got the most mentions, the sentiment behind those mentions, and how the accounts interact with each other - this will allow me to determine whether individual users are more likely to interact with certain accounts or certain messages. Finally, I will compare the most prominent topics from twitter to exit polls to see if their is a discrepancy in what people are talking about on twitter and what is actually motivating them to vote for a particular candidate.   

#### Tools
- Tweepy and Twitter API to pull tweets
- NLTK and spaCy for natural language processing
- scikit-learn for further data processing and modeling

#### MVP Goal
A minimum viable project for this project would be a sentiment analysis of the tweets from the candidates themselves to determine their messaging strategy i.e. whether they chose to primarily pursue a positive message about their own candidacy or a negative message about their opponent.
