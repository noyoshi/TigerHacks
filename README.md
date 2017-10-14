# **TigerHacks 2017**

Doug Smith, Noah Yoshida, Cami Carballo

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

