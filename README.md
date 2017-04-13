# NYTimes_Headlines_Remix

For this project, I used the New York Times articles search API to get a JSON file of articles with headlines, snippets, publish dates, etc. However, I ran into an issue: the API only gave me 9 articles at a time and I couldn't bound the results by a specific date range outside of the NY Time's API console. I was able to sort by oldest and newest though. I settled on working with the 9 oldest headlines because they were more interesting that the headlines I see every day. To focus the results, I queried articles that contained the word "liberalism" to investigate articles dealing with this political ideology.

CODE OVERVIEW
My python script NYTimes_Remix.py has three parts: 

First, I stores the components of the API call in discrete variables. These include my API key, a sort (oldest), and a query string, in this case "liberalism". 

Second, it excludes a specific headline by it's ID because the headline contained abnormal characters that ruined the flow of the text. 

Third, it parses out the lines of the API output according to line breaks and period placement, and then reassembles a random sampling of those lines. 

RESULTS

