# **TigerHacks 2017**

Doug Smith, Noah Yoshida, Cami Carballo

*Special thanks also to UTA ClaimBuster fact-checking team*

https://github.com/noyoshi/TigerHacks/blob/master/mysite/project/static/project/UI-screenshot.png

### Dependencies
- Code is primarily python2.7, please alias/run appropriately in your environment.
- All data in REQUIREMENTS.txt `pip install -r REQUIREMENTS.txt`
- spacy english module: `python -m spacy download en`

### Usage
- Configure your environment and install the requisite packages as explained in dependencies.
- Start the django server in mysite/
```
cd mysite
python manage.py runserver
```
- Server should start up and listen on a local port(8000).

### Common Data Type

fact JSON structure:
```
{
  date: Date
  sourceList: []{
    author: String
    publisher: String
    date: Date
    url: String
  }
  distilledFact: String
  factStrings: []String
  factHash: Hash
  confidenceScore: Number
}
```

_distilledFact:_ - String summarizing this fact based on common interpretation 
  of all fact strings

_factStrings:_ - Actual quotes of all strings that reduce to this fact

_factHash:_ - Hashed representation of what the fact concerns (Subjects x Sentiment)

_confidenceScore:_ - Numeric representation of how often this fact has been presented/verified

---
### RSS Feed Links

BBC

Top Stories: http://feeds.bbci.co.uk/news/rss.xml

Politics: http://feeds.bbci.co.uk/news/politics/rss.xml


NYT

Home Page: http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml

US: http://rss.nytimes.com/services/xml/rss/nyt/US.xml

Politics: http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml

