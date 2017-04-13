# NYTimes_Headlines_Remix

For this project, I used the New York Times articles search API to get a JSON file of articles with headlines, snippets, publish dates, etc. However, I ran into an issue: the API only gave me 9 articles at a time and I couldn't bound the results by a specific date range outside of the NY Time's API console. I was able to sort by oldest and newest though. I settled on working with the 9 oldest headlines because they were more interesting that the headlines I see every day. To focus the results, I queried articles that contained the word "liberalism" to investigate articles dealing with this political ideology.

CODE OVERVIEW
-------------
My python script NYTimes_Remix.py has three parts: 

First, I stores the components of the API call in discrete variables. These include my API key, a sort (oldest), and a query string, in this case "liberalism". 

Second, it excludes a specific headline by it's ID because the headline contained abnormal characters that ruined the flow of the text. 

Third, it parses out the lines of the API output according to line breaks and period placement, and then reassembles a random sampling of those lines. 

RESULTS
-------

1 Meet the...

THE PRESS..

 The indications from Europe seem to be that there is quite a pleasant, friendly understanding between the Austrian, Russian and French Governments.

 Whatever refers to a commercial centre so intimately related to the trade of the United States as is Bremen, must be of more or less interest.

 Italy is, indeed, in a wretchedly backward, and backward-treading condition..

 The good burgesses of that city are in trouble.

 Notwithstanding the indisputable wisdom and patriotism of its founders, and the pains taken to aggregate all the traditions of history and all the deductions of political science to aid in their transcendantly important task, they could ascertain nothing absolutely certain with reference to the novel system..

 Shiel, the British Envoy at the Court of Teheran, supported warmly by Mr.

 What is your solution of the present state of Europe ? said I lately to one of the most eminent of the French writers, who having himself weathered the three revolutions, has been a most attentive observer of events, and he replied:.

 Hardly a fact or rumor of extra-national interest has been brought forth this week in the world of politics

2 News Confirms

The news confirms rumors current at Rio, at the last arrivals, of the defeat of General Oribe, by the combined Brazilian and insurgent troops, with a loss of a large amount baggage and 6,000 horses ; and settles the question of the independence of the Bande Oriental..

 THE AUSTRIAN CONSTITUTION, which has been withdrawn, so much to the chagrin of agitatory committees and patriotism generally, was after all, the remotest shadow of what liberalism ought to be..

 Those, however, who pay much attention to French affairs may justify my noting a few items.

 Hardly a fact or rumor of extra-national interest has been brought forth this week in the world of politics.

 Notwithstanding the indisputable wisdom and patriotism of its founders, and the pains taken to aggregate all the traditions of history and all the deductions of political science to aid in their transcendantly important task, they could ascertain nothing absolutely certain with reference to the novel system..

 The concession is reported to be vouchsafed at the pressing instance of Mr.

 A Missionary meeting at Boston, on Monday night, was gratified with the announcement that his youthful serenity, the Shah of Persia, has proclaimed liberty of conscience, and toleration to all religions, within the limits of his kingdom.

 Stevens, the British Consul..

 Shiel, the British Envoy at the Court of Teheran, supported warmly by Mr

3 Once more, meet the...

THE PRESS..

 Shiel, the British Envoy at the Court of Teheran, supported warmly by Mr.

 It is destined to solve a great problem.

 Italy is, indeed, in a wretchedly backward, and backward-treading condition..

 The indications from Europe seem to be that there is quite a pleasant, friendly understanding between the Austrian, Russian and French Governments.

 to be productive of any especial good to the cause of liberal opinions..

 The news confirms rumors current at Rio, at the last arrivals, of the defeat of General Oribe, by the combined Brazilian and insurgent troops, with a loss of a large amount baggage and 6,000 horses ; and settles the question of the independence of the Bande Oriental..

 Stevens, the British Consul..

 THE AUSTRIAN CONSTITUTION, which has been withdrawn, so much to the chagrin of agitatory committees and patriotism generally, was after all, the remotest shadow of what liberalism ought to be.
