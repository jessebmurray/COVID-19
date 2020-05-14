# COVID-19
(This repo contains visualizations and statistics on COVID-19.)

### How does population density affect the prevalence of COVID-19? 

Presumeably, counties with low population densities, like rural counties, would seem to have a lower prevalence of COVID-19 because people are, quite literally, farther apart. Likewise, counties with high population densities, like urban counties, would seem to have a higher prevalence of COVID-19 because people are closer together, think the NYC subway. 

Here we can see the positive relationship.

I obtained the county population and COVID-19 cases data from USA facts and I obtained county land area data from the 2010 US census. I made the images via the pandas and seaborn libraries with python. There's clearly a relationship between population density and coronavirus cases (hence the 6ft away heuristic) and it became more clear that there was a positive relationship as the number of cases increased. 

![](coast_size.gif)

The states included in the 'East Coast' category clearly don't include *all* the states on the East coast because I wanted to show the hardest hit states, which on the east coast meant those around the tri-state area. Also, I wanted the combined populations of the east coast and west coast states to be roughly equal (~50 million people).

<br>
<br>

For this plot, I got the data from google search trends (link below) and I made the graph using the pandas and seaborn libraries. The goal is to show the hockeystick-like rise in searches due to COVID-19. The lineplot points show the average and the error bands show the 95% CI for each month.
![](covid1.png)
