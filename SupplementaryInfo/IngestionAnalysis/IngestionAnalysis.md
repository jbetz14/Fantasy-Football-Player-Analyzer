# Ingestion

The National Football League has a lot of information that goes along with the sport, and these data sets show that is very true. The Pro-Football-Reference source provides enless amounts of information that can be used to guide decisions on possible future outcomes of games and players. Sleeper might have less content when it comes to data due to the information surrounding more of the fantasy side of sports (like fantasy league and user info), but it also provides a huge data set that contains player information. 

## Pro-Football-Reference

Given that there is information going back over a hundred years, there is bound to be information that is not needed in the current season. The rushing, passing, and receiving data provided in ingestion shows the current season's players with their respective information. This data is scraped from their website and converted to a CSV file to be used for transformation. The data scraped from the site is quite small compared to what it could be, but given the scope of the project it might be all that is needed. There could be addition data added in the future.

## Sleeper

Sleeper is going to provide all the information surrounding the fantasy league, rosters, and users that is needed to predict what the best options for the next week of NFL games. The CSV files containing the league and roster information are quite small and easy to understand, but do reference the players file by id other than just a player name. This means that the player file is quite big and will require a stronger compute choice. This file could also be restructured and only provide information on players that are relevant. 
