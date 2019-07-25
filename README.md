# Project Submission
> Matthew Flood
> Create a Tableau Story

[Tableau public version 1](https://public.tableau.com/profile/matthew.flood#!/vizhome/story_v1_15638300454880/Story1)

[Tableau public version 2](https://public.tableau.com/profile/matthew.flood#!/vizhome/story_final_15638306505240/Trafficaccidentsnearmyhome)


## Summary

My story 

The intention of my story is to convey an understanding of traffic-accident frequency and location in the various neighborhoods close to my home in Denver.


## Design

I wanted to know which neighborhoods had the most and least accidents. For this I used a simple bar plot that shows counts for each neighborhood.

I wanted to see if there have been any significant changes in traffic-accident
behavior over the past 5 years, so I created visualizations that have year/month on the x axis and includes the neighborhood and count.  My first design had neighborhood and time on the x-axis with circles for data points, but after feedback, I moved the neighborhoods to the Y axis and just used the "automatic" mark.

I wanted to see the data on a map, so I created a map visualization to show where most of the traffic is happening.  I also created an animation so you can watch the accident locations accumulate over time.


## Feedback

"A few things for Traffic Accidents by Month: 1. Since you are using position to show the count of accidents, using circle size for count is redundant. 2. Using different colors for each neighborhood is also redundant since each neighborhood gets its own column. You might consider putting the neighborhoods on the X-Axis so you can see how all the neighborhoods change with respect to eachother" 

"Having different colors for each neighborhood on the map is redundant, since we can tell which neighborhood it is by the position on the map."

"Put each sheet in a Dashboard, and then put the dashboards into the story, that way you can add text elements to the layout."

## Resources

#### Data Source

The data was obtained from denvergov.org.  I wrote a python script to filter out neighborhoods that I was not concerned with to reduce the datafile size from 110MB to 17MB.

[https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-crime ](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-crime )


