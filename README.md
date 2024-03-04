# Fantasy-Football-Player-Analyzer

The world of fantasy football is a complex one to say the least and if you are just starting or are looking to get an edge on your opponents you have found the right place. By using the Sleeper API and the Pro-Football-Reference website, the two sources are combined take the ease off of endless hours of research before a new week of games. Each week your league information (gathered from Sleeper) will be matched up with the Pro-Football-Reference datasets to give you the information needed to decide which players should give you the most point possible, alloying you to beat your pesky family members.

It starts with ingestion from the two sources, using the Sleeper API to get league info and players on your roster and also the Pro-Football-Reference data to get the up to date stats for players and teams. The raw data we get from the two sources is good, but could use a bit of manipulation and cleaning to make them even better. After a few adjustments to the files that are coming from the Sleeper API, we wrap up transforming the data and send the finished datasets into a database. The data is then inserted from the database into PowerBI to set up an analysis to give a better idea of how each player is playing week to week and about their possible future potential.

Each step is explained more in-depth with the following sections:

## Ingestion

Sleeper API - https://docs.sleeper.com/

Sleeper is a fantasy draft application that has a more in depth experience to allow users to be more connected with their teams. The api allows for an easy way to gather user, league, and player information, all the data needed to analyze what players each user has and which ones are available to play each week. Each specific set of information is saved to a CSV file and sent to the cloud for futher transformation.

Pro-Football-Reference - https://www.pro-football-reference.com/

Pro-Football-Reference is where all the goods are at. This site provides ALL the stats you can imagine for not only football, but other sports as well. Passing, rushing, receiving, and defensive stats are all scraped from the site and also saved to individual CSV files to be transformed into a better way to visualize the data.

## Transformation

With all of the datasets that the ingestion phase provides, the data needs to be transformed into new sets we can use for the serving phase. Multiple aspects of transforming the data needs to be taken into consideration, like removing excess data, renaming columns and values within them, or pivoting rows and columns to better fit the next stage.

### RosterToRosteredPlayers
The first step for transforming is to shorten the players.csv, given that it is a large file and causes performance issues. The solution to this is to just gather the information of the rostered players, creating a subset of players with the ones that are rostered. 

### ProjectionsForRosteredPlayers
Now that there are a better set of players that need point values, we can use the Sleeper API to get the PPRs. This takes data from the weekly projection files and grabs the rostered player info from each week and combines them all into one CSV file. 

### Remove Excess Columns
The user.csv and roster.csv contains extra information about users and rosters that is not needed for the intended project, so we remove those columns to clean up the sets.


The CSV files that are adjusted from the transform phase, in addition to the ones that came from pro-football-reference, can then be inserted into a database of choosing. For this project, I used Azure cloud services to store the data. This step is not needed, but is recommended.

## Serving

With all of the datasets now being in a state that is easy to understand and use, we can insert the data into PowerBI for futher analysis. The end goal of this project was to give a way to easy compare player stats and point projections, so with the visualizations provided in PowerBI we can show these values all in one place. 

The route I took for the visualization was to show all of the players on my roster and allow a selection of a player to view their passing, receiving, and/or rushing stats along with point projections. In the future, I intend to add additional info like the team they play the next week and provide a more visually pleasing aesthetic.
