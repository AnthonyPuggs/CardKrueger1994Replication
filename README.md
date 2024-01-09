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

Now for the visual representation of the DiD model:
![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/85ae7a63-1f57-4c95-b0d7-a8109496c872)

As shown, it works according to how I explained it earlier. The counterfactual represents our parallel trend assumption, assuming that where it not for the minimum wage increase (intervention) the treatment group (NJ) would have continued trending downwards like the control group (PA). It’s important to recognise that the graph is just for visual representation reasons. The authors of the paper (nor am I) aren’t claiming that the increase in minimum wage increased employment. Rather that they found no statistically significant effects on employment from the increase in minimum wage, contrary to economic theory claiming it would decrease employment. 

Now, we can instead estimate this using regression analysis which is more accurate than just using sample means.
We will start simply without any controls, the model is:

$FTE_{it} = \beta_{1} + \beta_{2}STATE_{i} + \beta_{3}D_{t} + \delta(STATE_{i} \times D_{i}) + e_{it}$

Running this model results in the regression output:
![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/93f50a7f-30cd-4c10-a442-44ee99325c56)

The interaction term, (STATE x D) or d:state is our difference-in-differences estimator, with the coefficient remaining positive and with the same value of 2.75. Also note the p-value of 0.10, while perhaps not statistically significant enough at a 95% confidence level to claim that minimum wage increased employment, we can say for sure that it did not decrease employment.

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

Where:
ΔEi is the change in employment from before and after the minimum wage increase at store i

Xi is a set of characteristics of store i

NJi is a dummy variable that equals 1 for stores in New Jersey

GAPi is an alternative measure of the impact of the minimum wage at store i based on the initial wage set at that store (W¬1i):

GAPi = 0 for stores in Pennsylvania

GAPi = 0 for stores in New Jersey with W1i ≥ $5.05

GAPi = (5.05 – W1i)/W1i for other stores in New Jersey

Looking at these reduced-form models for change in employment:
![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/3317eb05-528b-4bb1-942b-10b439a5bd73)
![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/8936e9bd-12c8-4a89-a411-7160c476ca8c)

Models 1 and 2 used the regression model from 1a, regressing change in FTE employment against the New Jersey dummy variable. In the paper, model 1 is most comparable to the simple DiD of employment changes in column 4, row 4 of table 3 – where the wages in the NJ stores were set at the initial minimum wage ($4.25). This is due to the change in FTE employment being strongest in stores that were initially set at the old minimum wage, as well as the fact that the variable was using a balance sample of stores. 

Model 1 in my replication is instead more comparable to the simple DiD of employment changes in column 4, row 3 of table 3 – not using the balanced sample of stores. Table 4 is not only meant to be using a balanced sample of stores, but also sample of wages. I unfortunately was not able to do this, the more detailed reasons as to why can be found below under the ‘Notes’ header. This is why all the values are a bit different, but they all still convey the same message.

Model 2 introduces four control variables, dummy variables for three of the fast-food chains and another dummy for company-owned stores. This is done to see if any of our control variables significantly change the outcome, which doesn’t seem to be the case by simply looking at the coefficient and standard error. Using joint F tests for exclusion of all control variables, we can see whether these control variables improve the model or not. Looking at the probability value (p-value) for controls, it stands at a p-value of 0.48 (0.34 in the paper). This indicates that the covariates add little to the model and have no statistically significant effect on the size of the estimated New Jersey dummy.

 Models 3 through 5 now instead use the GAP variable to measure the effect of the minimum wage. It’s important to understand that GAPi is the proportional increase in wages at store i necessary to meet the new minimum wage. Variation in GAPi reflects both the New Jersey-Pennsylvania contrast and differences within New Jersey based on reported starting wages in wave 1. From the paper, the mean value of GAPi among NJ stores is 0.11, multiplying that by the model 3 coefficient gives us a 1.72 increase in FTE employment in NJ relative to PA. In my replication, the model 3 coefficient is a bit higher with the mean GAP value among NJ stores being slightly lower. This brings us to an increase in FTE employment of 1.783, which is reasonably close to the original value.

![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/01b4a812-5b89-4805-b287-530af8e8c56b)

Model 4 added the same four control variables for chains and company ownership from model 2, and the p-value for controls being at 0.62 (0.44 in the paper) indicates that the covariates add little to the model once again.
Model 5 includes the prior four control variables, and an additional five control variables for region that include two regions of eastern PA and North, Central, and South NJ. These dummies help to control for any region-specific demand shocks and identify the effect of the minimum wage by comparing employment changes at higher and lower wage stores within the same region of NJ. The p-values for controls being at 0.48 (0.40 in the paper) indicate that again the covariates add little to the model. 

![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/41cb44c7-9265-4515-ad1f-be435f26c9b4)

Interestingly, only model 5 has issues with its statistical significance. The addition of the region dummy variables significantly attenuated the GAP coefficient and raised its standard error compared to models 3 and 4. This raised the p-value enough that it is longer possible to reject the null hypothesis of a zero employment effect of the minimum wage, as seen by the p-value of 0.063. The multicollinearity warning that appears in the regression seems to possibly be an issue at first glance. However, the warning is removed when any one of the five region dummies is removed, and the GAP p-value remains at 0.063. Multicollinearity is commonly an issue when adding too many control variables but doesn’t seem to be the issue here.

One reasoning given by the authors of the paper for the statistical insignificance is the presence of measurement error in the starting wage. That even if employment growth has no regional component, the addition of region dummies will lead to some attenuation of the GAP coefficient if some of the true variation in GAP is explained by region. If interested, the authors go much deeper into this in their paper on page 781.

# Specification Tests
The results in tables 3 and 4 seem to contradict the standard prediction from economic theory that a rise in the minimum wage will reduce employment. Table 5 presents some specification tests to test the robustness of this conclusion. My replication only includes the specifications relating to adjusting the FTE employment calculation, and only has values for change in employment and not proportional change.

![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/8eef863a-3ff8-4a30-9ebf-24dea9dc6b4c)
![image](https://github.com/AnthonyPuggs/CardKrueger1994Replication/assets/61487785/6f9734d4-e2d6-4b35-b1d6-08513fc01b34)

Testing alternative measures of FTE employment is important since the way the measure is calculated (mainly the 0.5 * part-time weighing as full-time) is not perfect. 50% on the basis of two sources of research in this area. First one being the 1991 Current Population Survey revealing that part-time workers in the restaurant industry work about 46% as many hours as full-time workers. The second being a study by Katz and Krueger (1992) that report the ratio of part-time workers’ hours to full-time workers’ hours in the fast-food industry is 0.57.

When redefining FTE to exclude management employees, the change has no effect relative to the base specification. In the other rows, managers are included back in FTE employment, but part-time workers are reweighed as either 40% or 60% of full-time workers (instead of 50%). These reweight changes also have little effect on the models.


# Notes
The difference in values following the table 4 values seem to be from the stores included in the analysis. My replication in Table 4 has 351 observations while the original paper has 357 observations. Table 4 (and everything following, so including table 5) uses a restricted sample that restricts the analysis to the set of stores with available employment (as seen in table 3 with balancing) and wage data in both waves of the survey. In my replication, all observations for which any of the employment variables were ‘NA’ were dropped. This is from the assumption those observations did not share the number of employees, making it unfit for inclusion in the models.

However, it’s possible the original paper treated these differently. From Aaronmams replication (in references below) he redoes the models instead this time dropping observations only if all of full-time employees, part-time employees, and managers equal 0 or those same roles in the second wave equal 0. Or if either starting wage in wave 1 or wave 2 is missing. After implementing this, the observations significantly increased to 370, moving even further away from the original paper.
It is surely possible to look through the original SAS file for the paper and workout how exactly the stores are included or not – but it feels unnecessary as the values are very close regardless.

# References
Card & Krueger 1994 Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania https://davidcard.berkeley.edu/papers/njmin-aer.pdf

Hill, Griffiths & Lim 2016 Principles of Econometrics, 5th Edition

https://www.pymc.io/projects/examples/en/latest/causal_inference/difference_in_differences.html for Python DiD visualisation

https://github.com/BiomedSciAI/causallib/blob/master/examples/fast_food_employment_card_krueger.ipynb for lovely Python code to scrape, convert and filter the data I want from the original dataset

https://aaronmams.github.io/Card-Krueger-Replication/ R code I used as inspiration for going about replication in Python

https://github.com/alopatina/Applied-Causal-Analysis/blob/master/Difference%20in%20difference%20Min%20Wages%20and%20Employment%20Card%20and%20Krueger%20replication.ipynb R code I used as inspiration for going about replication in Python



