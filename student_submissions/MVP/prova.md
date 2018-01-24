# OBJECTIVE:    
predict the domestic gross of a movie

## SOURCES:    
* boxmojo: general info   
* The numbers: financials
* Awards web page: for nominations and oscars prizes

## FEATURES:
* adjusted budget 
* geners
* distributor
* rating
* run-time

## ENGINEREED FEATURES   
### Celebrity level of director:
* number of movies directed
* average gross of previous movies
* number of nominations received
* number of oscar prizes won
    
### Celebrity level of actors:
* average number of previous movies of the cast
* weighted average of domestic gross of the cast
* weighted average of intenational gross of the cast
* number of nominations received
* number of oscar prizes won

### Polynomial
* Interaction with the adjusted budget

After having merges 3 different sources, I have cleaned and normalized the data.    
A first base case (domestic gross (adj) vs budget (adj) gave  to me a score of 0.27.    
Starting from there, I added new features to improve the perfromance of the model and its predicting power.   
Particularly promising are the enginered features that allowed to me to improve the cscore up to 0.57, twice the base case.
To further improve the model, I am adding up interaction terms. And I am also trying different transformations of the features to make them a bit more normal shaped. This may have a big impact as you can notice by looking at the differnece between the two below figures, one representing the domestic gross (adj) vs budget (adj)  and the other is the same representation in a log-log plane. As you can observe, in the second figure there seems to be clearer linear relationship
