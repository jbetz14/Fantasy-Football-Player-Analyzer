[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12510121&assignment_repo_type=AssignmentRepo)
# CSCI 422 Project - Josh Betz

The world of fantasy football is a complex one to say the least and if you are just starting or are looking to get an edge on your opponents you have found the right place. By using the Sleeper API and the Pro-Football-Reference website, the two sources are combined take the ease off of endless hours of research before a new week of games. Each week your league information (gathered from Sleeper) will be matched up with the Pro-Football-Reference datasets to give you the information needed to decide which players should give you the most point possible, alloying you to beat your pesky family members.

It starts with ingestion from the two sources, using the Sleeper API to get league info and players on your roster and also the Pro-Football-Reference data to get the up to date stats for players and teams.
< Update with information on Transformation and Serving >

## Ingestion
Sleeper API - https://docs.sleeper.com/

Sleeper is a fantasy draft application that has a more in depth experience to allow users to be more connected with their teams. The api allows for an easy way to gather user, league, and player information, all the data needed to analyze what players each user has and which ones are available to play each week. Each specific set of information is saved to a CSV file and sent to the cloud for futher transformation.

Pro-Football-Reference - https://www.pro-football-reference.com/

Pro-Football-Reference is where all the goods are at. This site provides ALL the stats you can imagine for not only football, but other sports as well. Passing, rushing, receiving, and defensive stats are all scraped from the site and also saved to individual CSV files to be transformed into a better way to visualize the data.

## Transformation
