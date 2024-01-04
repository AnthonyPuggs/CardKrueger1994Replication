# CardKrueger1994Replication

# Introduction
David Card and Alan Krueger's 1994 paper, "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania" was a groundbreaking contribution to the labour economics literature. Prior to the early 90s, over 90% of economists agreed that minimum wage laws reduced employment among low skilled workers [(Kearl et al., 1979).](https://www.jstor.org/stable/1801612 "A Confusion of Economists?") This helped to kickstart the shift in economists’ views on minimum wage. It contributed toward the shift of viewing minimum wage effects only in a perfectly competitive labour market, to instead a monopsony labour market. 

Minimum wages under the assumptions of a perfectly competitive market seem to be incredibly inefficient, causing deadweight loss and having a net negative effect on low skilled workers by decreasing employment of them as a whole to only benefit a few through a higher mandated wage. This is visually represented below.

![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/4890f8a4-6f6a-492d-bab2-7d71d253e49b)

In this perfectly competitive market, the market naturally reaches an equilibrium at a wage of $10/hr and quantity of labour of 1,200. As seen, raising the minimum wage to $12/hr causes a movement along the labour supply curve to a higher quantity of labour of 1,600 (more people want to work because the wage is higher) but conversely, this also causes a movement along the labour demand curve to a lower quantity of labour of 700 (firms cannot afford to pay the new minimum wage so firms decrease employment). This effect is visually represented by the surplus of labour, the consumer and producer surplus aren’t shown on the figure but it also decreases total surplus, creating deadweight loss. Low skilled workers would have been better off overall if the minimum wage was not increased above the equilibrium.

This follows quite nicely, but introducing monopsonistic labour markets rather than perfect competition provides one theory for why increasing minimum wage doesn't always necessarily decrease employment (as will be empirically shown soon).

On April 1, 1992, New Jersey's minimum wage rose from $4.25 to $5.05 per hour. To evaluate the impact of the law, Card & Krueger surveyed 410 fast-food restaurants in New Jersey and eastern Pennsylvania before and after the minimum wage policy. Comparisons of employment growth at stores in New Jersey and Pennsylvania (where the minimum wage was constant) provide simple estimates of the effect of the higher minimum wage. This analysis provides fascinating results, as we will see below.


# Analysis
It is first important to understand how the difference-in-differences (DiD) method works as a causal inference tool. Simply, it tries to mimic the gold standard randomised control trial (RCT) by analysing the differential effect of a treatment on a 'treatment group' compared to a 'control group'. Key difference here of course is that DiD is done on natural experiments, as generally is with the nature of economics, we unfortunately don't get the randomisation of an RCT. Instead, we rely on the parallel trend assumption, which assumes that treatment group would follow the same trend as the control group in absence of the intervention. Assuming this, we can then take the difference between the treatment group post policy change and compare to the counterfactual treatment group trend to get our DiD estimator for the treatment effect. I will come back to a visual representation of this later. 

There are a few reasons why the parallel trend assumption holds here. Firstly, New Jersey is a small state with an economy that is closely linked to nearby states, leads us to a reasonable belief that fast-food stores in eastern Pennsylvania form a natural basis for comparison. Any common unobservable shocks are therefore likely experienced in both groups. Additionally, seasonal patterns of employment are similar in both New Jersey and eastern Pennsylvania, which allows the DiD methodology to difference out any seasonal employment effects. Before moving on, it is also important to understand why fast-food restaurants were chosen for this study. There are a few great reasons for this. Firstly, fast-food restaurants were a leading employer of low-wage workers. Secondly, fast-food restaurants are only a few number of chains and comply with minimum wage regulations and would be expected to raise wages following a minimum wage increase. Thirdly, homogeneity in the job requirements and products of fast-food restaurants help to obtain reliable measures of employment, wages, and product prices. Particularly with the lack of tips massively simplifying the measurement of wages in the industry. Lastly, the data is easy to gather with fast-food restaurants having high response rates to telephone surveys in the past.
We can start now by looking at the distribution of starting wage rates before and after the New Jersey minimum wage increase, comparing my replication to the original study.

![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/0c0bb9a5-f363-4221-a52a-5d4327f81840)
![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/0e465c7d-c920-4c39-9e39-83eec4201277)
![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/b2c6e4a6-7dab-436a-a28b-4a2466db9585)

Note that February 1992 was before the minimum wage increase which was in April 1992, of course meaning November 1992 was after the minimum wage increase. Here we can see that the distributions of starting wages in the states before the increase were very similar. Following the increase, nearly all the restaurants in New Jersey that were paying less than $5.05 per hour reported a starting wage equal to the new rate.

Now, we can look at the employment effects of the minimum-wage increase – the main part of the study. 
![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/2630b860-88d5-4e3b-b1c2-8e4732f05ce4)
![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/6a47cd99-6ab0-4ad9-a329-c7ea82939636)

Only the ‘stores by state’ part of table 3 was replicated, as it is most relevant to the DiD method and the results of the paper.  Variable 5 was also not calculated as I was unable to find which stores temporarily closed, and the variable doesn’t really change the overall result. Most values are either identical or very close, with the standard errors having their own rows in the replication. 
Looking at the mean FTE employment before and after, NJ were initially smaller than their PA counterparts but interestingly grew relative to PA’s stores after the minimum wage increase. To look at the relative gain, we turn to our DiD estimator for change in mean FTE employment, which is 2.75. This estimates that FTE employment increased by 2.75 employees during the period where New Jersey increased their minimum wage. The DiD estimator having a positive sign is contrary to what is predicted by traditional economic theory.
Now, we can instead estimate this using regression analysis which is more accurate than just using sample means.
We will start simply without any controls, the model is:

$FTE_{it} = \beta_{1} + \beta_{2}STATE_{i} + \beta_{3}D_{t} + \delta(STATE_{i} \times D_{i}) + e_{it}$

Running this model results in the regression output:
![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/93f50a7f-30cd-4c10-a442-44ee99325c56)

The interaction term, (STATE x D) or nj:d is our difference-in-differences estimator, with the coefficient remaining positive and with the same value of 2.75. Also note the p-value of 0.10, while perhaps not statistically significant enough at a 95% confidence level to claim that minimum wage increased employment, we can say for sure that it did not decrease employment.

Now we can do another regression, adding control variables. Some of these are dummy variables for fast-food restaurants and whether the restaurant was company-owned rather than franchise-owned. Some are also dummy variables for geographical regions within the survey area.

With controls, the model is now:

$FTE_{it} = \beta_{1} + \beta_{2}STATE_{i} + \beta_{3}D_{t} + \delta(STATE_{i} \times D_{i}) + \beta_{4}CHAIN2 + \beta_{5}CHAIN3 + \beta_{6}CHAIN4 + \beta_{7} COOWNED + \beta_{8}CENTRALJ + \beta_{9}SOUTHJ + \beta_{10}PA1$
![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/fed75eba-6328-465d-bba6-dafb35c10d37)

As can be seen, adding controls to the regression did not alter the difference-in-differences estimator, it is still positive. 

This analysis, while insightful - make no allowance for other sources of variation in employment growth, such as across chains. We can use new linear regression models to incorporate this. Using panel data, we can control for unobserved individual-specific characteristics.
These are of the form of:

(1a) $\Delta E_{i}= a + bX_{i} + cNJ_{i} + \varepsilon_{i}$

and

(1b) $\Delta E_{i}= a' + b'X_{i} + c'GAP_{i} + \varepsilon'_{i}$

The GAP variable is an alternative measure of the impact of the minimum wage at store I based on the initial wage set at that store:

GAPi = 0 for stores in Pennsylvania

GAPi = 0 for stores in New Jersey with W1i ≥ $5.05

GAPi = (5.05 – W1i)/W1i for other stores in New Jersey

GAP is the proportional increase in wages at store i necessary to meet the new minimum rate. Variation in GAP reflects both the New Jersey-Pennsylvania contrast and differences within New Jersey based on reported starting wages in wave 1.
Looking at these reduced-form models for change in employment:
![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/3317eb05-528b-4bb1-942b-10b439a5bd73)
![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/c3502ccc-666f-4dca-91bd-77f709db1ed8)





# Notes

# References
Card & Krueger 1994 Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania https://davidcard.berkeley.edu/papers/njmin-aer.pdf

Hill, Griffiths & Lim 2016 Principles of Econometrics, 5th Edition

https://www.pymc.io/projects/examples/en/latest/causal_inference/difference_in_differences.html for Python DiD visualisation

https://github.com/BiomedSciAI/causallib/blob/master/examples/fast_food_employment_card_krueger.ipynb for lovely Python code to scrape, convert and filter the data I want from the original dataset

https://aaronmams.github.io/Card-Krueger-Replication/ R code I used as inspiration for going about replication in Python

https://github.com/alopatina/Applied-Causal-Analysis/blob/master/Difference%20in%20difference%20Min%20Wages%20and%20Employment%20Card%20and%20Krueger%20replication.ipynb R code I used as inspiration for going about replication in Python



