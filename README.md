# CardKrueger1994Replication

# Introduction
David Card and Alan Krueger's 1994 paper, "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania" was a groundbreaking contribution to the labour economics literature. Prior to the early 90s, over 90% of economists agreed that increases in minimum wage would lead to disemployment effects (ref needed). This helped to kickstart the shift in economists views on minimum wage. It contributed toward the shift of viewing minimum wage effects in a perfectly competitive labour market, to instead a monospony labour market. 


# Analysis
These comparisons in Table 3, while insightful - make no allowance for other sources of variation in employment growth, such as across chains. We can use linear regression models to incorporate this.
These are of the form of:
(1a) $\normalsize \Delta E\tiny i \normalsize = a +bX\tiny i \normalsize + cNJ\tiny  i \small + \varepsilon\tiny i$
and
(1b) 







# Notes
There a couple important things to mention when following my replication. Firstly, the data set I am using is from the textbook Principles of Econometrics, 5th Edition by Hill, Griffiths & Lim (2016). This is particularly important because of the FTE variable. Card and Kreuger calculate FTE = 0.5 x number of part time workers + number of full time workers + number of managers. This data set includes the FTE ready to go without the variables on workers and managers, so my script does not need to do that calculation. These changes are all for simplicity - the data values and therefore output are identical to the original paper.
