#!/usr/bin/python2.7
import datetime

from article import article
from extraction import extractFacts

# Run after variables are declared.
def testCall():
  testArticle = article(title,description, date,link,body)
  print extractFacts(testArticle)

title="Test Article"
date=datetime.date(1970,1,1)
link="www.example.com"
description="an example article"
body='''
After years of being characterised as dull, it seems Philip Hammond is now in the firing line for being too outspoken. The chancellor's use of the word "enemy" to describe EU negotiators on Friday is roundly condemned by The Sun. "The Chancellor should be focused on his pivotal budget next month," it says. "Instead he's lurching around, barking randomly. He must shut his gob."The Daily Mail calls it Mr Hammond's "Basil Fawlty moment". According to The Times, some Tories are pressing the prime minister to sack both the chancellor and Foreign Secretary Boris Johnson - a move that they say would reassert her authority, with honour satisfied on both Leave and Remain wings of the party.Get news from the BBC in your inbox, each weekday morning"Trump's stance on Iran finds few in accord," says a headline in the Daily Telegraph. The paper says he was reprimanded by world leaders for refusing to certify the Iran nuclear deal, and was warned he could trigger war.That is echoed by the Israeli newspaper, Haaretz, which says Donald Trump is prepared to risk mayhem to satisfy his ego and erase Obama's legacy.His "Iran deal bombshell" undermines American credibility and gives North Korea the perfect excuse to avoid deal-making, it says.One of Iran's biggest selling papers, Hamshahri, says Tehran has replied to Mr Trump's claim that the Revolutionary Guard is a terrorist group - by placing the US military on a list of groups that undermine international security and stability. The Guardian is among the papers to quote claims that Health Secretary Jeremy Hunt has floated the idea of stopping people from attending AE departments unless they have first consulted their GP or called NHS 111. An NHS England adviser, Dr Helen Thomas, is quoted as telling a conference that Mr Hunt suggested it to her and that the idea could be piloted - although NHS England denies the suggestion.Meanwhile, the i carries claims that some family doctors have been threatening to remove patients who "check Dr Google" before appointments.GPs are apparently becoming exasperated by the number of "cyberchondriacs" - people who cannot stop self-diagnosing online.For the Daily Mirror, the main news is the jailing of a couple from Merseyside who lied about being ill on holiday in an attempt to claim 20,000 in compensation.Paul Roberts was sentenced to 15 months and Deborah Briton nine months. It should serve as a warning to other fraudsters, the Mirror says, which adds that it is not a victimless crime - since scammers put up the cost of insurance for everyone else, as well as ripping off hoteliers. According to the Daily Mail, more than eight in 10 people who drive to work do not know the names of the roads they use, because they rely on sat-navs.And a study found nine in 10 motorists cannot name the roads around their home for the same reason. The Daily Star warns readers that after a 25C heatwave over the weekend, 100 mph Hurricane Ophelia will "smash" into our shores.'''
testCall()
