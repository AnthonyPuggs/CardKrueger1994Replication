# CardKrueger1994Replication

# Introduction
David Card and Alan Krueger's 1994 paper, "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania" was a groundbreaking contribution to the labour economics literature. Prior to the early 90s, over 90% of economists agreed that minimum wage laws reduced employment among low skilled workers [(Kearl et al., 1979).](https://www.jstor.org/stable/1801612 "A Confusion of Economists?") This helped to kickstart the shift in economists views on minimum wage. It contributed toward the shift of viewing minimum wage effects only in a perfectly competitive labour market, to instead a monospony labour market. 

Minimum wages under the assumptions of a perfectly competitive market seem to be incredibly inefficient, causing deadweight loss and having a net negative effect on low skilled workers by decreasing employment of them as a whole to only benefit a few through a higher mandated wage. This is visually represented below.

![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/4890f8a4-6f6a-492d-bab2-7d71d253e49b)

In this perfectly competitive market, the market naturally reaches an equilibrium at a wage of $10/hr and quantity of labour of 1,200. As seen, raising the minimum wage to $12/hr causes a movement along the labour supply curve to a higher quantity of labour of 1,600 (more people want to work because the wage is higher) but conversely, this also causes a movement along the labour demand curve to a lower quantity of labour of 700 (firms cannot afford to pay the new minimum wage so firms decrease employment). This effect is visually represented by the surplus of labour, the consumer and producer surplus isn't shown on the figure but it also decreases total surplus, creating deadweight loss. Low skilled workers would have been better off overall if the minimum wage was not increased above the equilibrium.

This follows quite nicely, but introducing monopsonistic labour markets rather than perfect competition provides one theory for why increasing minimum wage doesn't always necessarily decrease employment (as will be empirically shown soon).

On April 1, 1992, New Jersey's minimum wage rose from $4.25 to $5.05 per hour. To evaluate the impact of the law, Card & Krueger surveyed 410 fast-food restaurants in New Jersey and eastern Pennsylvania before and after the minimum wage policy. Comparisons of employment growth at stores in New Jersey and Pennsylvania (where the minimum wage was constant) provide simple estimates of the effect of the higher minimum wage. This analysis provides fascinating results, as we will see below.


# Analysis
I begin by firstly replicating part of Table 3, looking at the mean and standard errors of full-time equivalent (FTE) employees by state and period. This will give us a simple estimate of the treatment effect from the minimum wage by using the difference-in-differences estimator. 

![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/d3433c19-fe92-49c7-ae3d-84ae8ed6184e)

nj = 0 is Pennsylvania
nj = 1 is New Jersey
d = 0 is before the minimum wage increase
d = 1 is after the minimum wage increase

Interestingly enough, FTE employment fell in Pennsylvania (the control group) and FTE employment increased in New Jersey (the treatment group). We can quantify this by estimating the difference-in-differences estimator which is:

![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/4f0abf2e-18c4-40b9-8627-3640047f6bce)

This estimates that FTE employment increased by 2.75 employees during the period where New Jersey increased their minimum wage. The difference-in-differences estimator having a positive sign is contrary to what is predicted by traditional economic theory.

Now, we can instead estimate this using regression analysis which is more accurate than just using sample means.
We will start simply without any controls, the model is:

$FTE_{it} = \beta_{1} + \beta_{2}NJ_{i} + \beta_{3}D_{t} + \delta(NJ_{i} \times D_{i}) + e_{it}$

Running this model results in the regression output:

![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/3581c3b0-a348-409e-921a-32ea2a78eca1)

The interaction term, (NJ x D) or nj:d is our difference-in-differences estimator, with the coefficient remaining positive and with the same value of 2.75. Also note the p-value of 0.10, while perhaps not statistically significant enough at a 95% confidence level to claim that minimum wage increased employment, we can say for sure that it did not decrease employment.

Now we can do another regression, adding control variables. Some of these are dummy variables for fast-food restaurants and whether the restaurant was company-owned rather than franchise-owned. Some are also dummy variables for geographical regions within the survey area.

With controls, the model is now:

$FTE_{it} = \beta_{1} + \beta_{2}NJ_{i} + \beta_{3}D_{t} + \delta(NJ_{i} \times D_{i}) + \beta_{4}KFC + \beta_{5}ROYS + \beta_{6}WENDYS + \beta_{7} COOWNED + \beta_{8}CENTRALJ + \beta_{9}SOUTHJ + \beta_{10}PA1$

![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/927ae4f4-295f-4cfc-942c-7c48903e1520)

As can be seen, adding controls to the regression did not alter the difference-in-differences estimator, it is still positive. 

This analysis, while insightful - make no allowance for other sources of variation in employment growth, such as across chains. We can use new linear regression models to incorporate this. Using pandel data, we can control for unobserved individual-specific characteristics.
These are of the form of:

(1a) $\Delta E_{i}= a + bX_{i} + cNJ_{i} + \varepsilon_{i}$

and

(1b) $\Delta E_{i}= a' + b'X_{i} + c'GAP_{i} + \varepsilon'_{i}$

Due to the dataset used, only the regression model (1a) will be used. The model incorporating the GAP variable will be included shortly in an update.

By running this model:

![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/89e93285-59ab-4e34-baff-8f75c8e09f76)

With nj being our difference-in-differences estimator, the coefficient is still at 2.75 and very statistically significant with a p-value of 0.001. 

We run one more model here accounting for a few controls:

![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/18736504-c752-4ccd-be7e-f3da591a459a)

Consistent with all the models and outputs so far, the difference-in-differences estimator does not change.

We have failed to conclude that the minimum wage increase has reduced employment in these New Jersey fast-food restaurants.


# Notes
There a couple important things to mention when following my replication. Firstly, the data set I am using is from the textbook Principles of Econometrics, 5th Edition by Hill, Griffiths & Lim (2016). This is particularly important because of the FTE variable. Card and Krueger calculate FTE = 0.5 x number of part time workers + number of full time workers + number of managers. This data set includes the FTE ready to go without the variables on workers and managers, so my script does not need to do that calculation. Secondly, the dataset already has the 'demp' variable, which is the change in FTE employment from wave 1 to wave 2, so my script also does not need to calculate this.

# References
Card & Krueger 1994 Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania https://davidcard.berkeley.edu/papers/njmin-aer.pdf

Hill, Griffiths & Lim 2016 Principles of Econometrics, 5th Edition
