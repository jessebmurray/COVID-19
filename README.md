# COVID-19
### How does population density affect the prevalence of COVID-19? 

![](coast_size.gif)

Presumeably, counties with low population densities, like rural counties, would seem to have a lower prevalence of COVID-19 because people are, quite literally, farther apart. Likewise, counties with high population densities, like urban counties, would seem to have a higher prevalence of COVID-19 because people are closer together, think the crowded NYC subway. 

![](relationship.png)

#### Interpretation
We can see that there is indeed a positive relationship, which adds weight to the 6 ft away heuristic, and agrees with what we would expect. It became more clear that there was a positive relationship as the number of cases increased, however, the relationship gradually diminished over time. I think this may be because, in the early stages of the crisis, the crowded and busy counties got hit first, however, as the virus spread everywhere, the entropy increased so to speak and it didn't matter so much whether a location was crowded or not, counties everywhere had the virus in similar amounts. 

I showed Seattle versus Manhattan because I clearly remember in the beginning of March walking around the streets of manhattan, going in the subway, etc. and nobody was wearing masks. At the time, Seattle Washington was known to have cases and so people may have been more careful there, and, I believe Seattle was locked down much earlier than NYC. 

One of the saddest moments of making these graphs was when I updated the data and found that I had to increase the top limit of the y-axis to fit the much greater number of cases in a few of the counties. 

 

#### Methods and materials
I obtained the county population and COVID-19 cases data from USA facts and I obtained county land area data from the 2010 US census. I created the visualization with pandas and matplotlib in python. I included the hardest hit states on the east and west coast to obtain more reliable sample sizes of COVID-19 cases. I also chose the states specifically so that the combined populations of the east coast and west coast states would be roughly equal (51 plus or minus 1 million people). 




<br>
<br>
<br>
<br>

<!-- Here we can see the relationship across all US counties. I think it's less clear here because there could be a lot of counties with very small populations, and if those counties happen to have a lot of cases, they would have an enormous number of cases per capita without necessarily having a high population density. 

![](all_size.gif)

<br>
<br>

-->

For this plot, I got the data from google search trends (link below) and I made the graph using the pandas and seaborn libraries. The goal is to show the hockeystick-like rise in searches due to COVID-19. The lineplot points show the average and the error bands show the 95% CI for each month.
![](covid1.png)
