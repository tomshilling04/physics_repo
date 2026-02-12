# Week 3 Summary

## Decoupling Separation
Firstly, changed parameters on parameter identification python file to show what my viscous and GW timescales are for the Cerioli simulation.
Then with the knowledge of what my intercept would look like between the timescales, I plotted a graph for timescales against separation, a. Made a np.array of values going up to 200 and then plotted. The graph looks like this: 
![Decoupling separation shown by the intercept of the graph](../Decoupling_sep.png)


## Reducing Noise

The graphs produced last week with the simulations may have had the data looking wrong, but it still needed to be made cleaner, just so it looks good when the data I want to be produced is made. Reworked my code to have much more timesteps between accreted mass diff. Made the graph much less noisy. 

### Prograde Graph

![Accretion rate over time. Much less noise in these pngs and limits also changed](../Week3/Cerioli_sim/Accretion_rate_across_time_improved_scaling_pt2.png)  
This, compared to the previous week, is much better. The difference between the primary and secondary sink are much more noticable. There are no intersections between the two accretion rates. This does not correlate with Cerioli's data. However, an initial peak is more noticeable for the secondary accretion rate, which is good. 

### Retrograde Graph

 
