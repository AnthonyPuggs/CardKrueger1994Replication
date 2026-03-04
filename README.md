# Card & Krueger (1994) Replication

A Python replication of Card & Krueger's seminal 1994 paper, *"Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania"*.

> For the full write-up with figures, equations, and regression output, see the [GitHub Pages site](https://anthonypuggs.github.io/CardKrueger1994Replication/) or the corresponding [Substack post](https://anthonypuggs.substack.com/p/python-replication-of-card-and-krueger).

## Overview

Prior to the early 1990s, over 90% of economists agreed that minimum wage laws reduced employment among low-skilled workers [(Kearl et al., 1979)](https://www.jstor.org/stable/1801612). Card & Krueger's natural experiment challenged this consensus by surveying 410 fast-food restaurants in New Jersey and eastern Pennsylvania before and after New Jersey raised its minimum wage from \$4.25 to \$5.05 on April 1, 1992.

Their key finding: **no statistically significant negative effect on employment** from the minimum wage increase, contrary to standard competitive labour market predictions. This replication reproduces the core tables and regressions from the paper using Python.

## What's Replicated

| Paper Section | Description | Method |
|---|---|---|
| **Table 2** | Distribution of starting wage rates (Feb & Nov 1992) | Grouped bar charts comparing NJ vs PA |
| **Table 3** | Mean FTE employment before/after, DiD estimator | Sample means, balanced & unbalanced |
| **Table 4** | Reduced-form models for change in employment (Models 1-5) | OLS with NJ dummy and GAP variable, with/without controls |
| **Table 5** | Specification tests (alternative FTE measures) | OLS with reweighted part-time employment |
| **DiD Visual** | Difference-in-differences graph with counterfactual | Plotted from Table 3 sample means |

## Methods

- **Difference-in-Differences (DiD):** Compares employment changes in NJ (treatment) vs PA (control) to estimate the causal effect of the minimum wage increase, relying on the parallel trends assumption.
- **OLS Regression:** Models range from a simple DiD specification to models with controls for chain, ownership, and region. The GAP variable captures within-NJ variation based on the initial wage distance to the new minimum.
- **Specification Tests:** Robustness checks using alternative FTE employment definitions (excluding managers, reweighting part-time at 0.4x and 0.6x).

## Data

The original dataset is automatically downloaded at runtime from [David Card's website](https://davidcard.berkeley.edu/data_sets/njmin.zip). It contains survey data on 410 fast-food restaurants across NJ and eastern PA from two waves (February 1992 and November 1992).

## Installation

```bash
git clone https://github.com/AnthonyPuggs/CardKrueger1994Replication.git
cd CardKrueger1994Replication
pip install -r requirements.txt
```

### Requirements

- Python 3.8+
- pandas
- numpy
- scikit-learn
- statsmodels
- requests
- matplotlib
- seaborn
- scipy

## Usage

```bash
python CardKrueger1994Replication.py
```

This will download the data, run all analyses, print regression output to the console, and save the following figures:

- `Distribution of Starting Wage Rates Feb 1992.png`
- `Distribution of Starting Wage Rates Nov 1992.png`
- `DID.png`

## Key Results

- The DiD estimator for change in mean FTE employment is **+2.75**, indicating NJ stores gained employment relative to PA stores after the minimum wage increase.
- Regression analysis confirms this: the interaction term (state x time) is positive across all specifications.
- Adding controls for chain, ownership, and region does not meaningfully alter the result.
- The GAP variable models show similar positive effects, though Model 5 (with region dummies) attenuates the coefficient.

## Notes

The replication uses 351 observations in Table 4 compared to 357 in the original paper, due to differences in how missing employment data is handled. See the [full write-up](https://anthonypuggs.github.io/CardKrueger1994Replication/#notes) for details.

## References

- Card, D. & Krueger, A.B. (1994). [Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania](https://davidcard.berkeley.edu/papers/njmin-aer.pdf). *American Economic Review*, 84(4), 772-793.
- Hill, R.C., Griffiths, W.E. & Lim, G.C. (2016). *Principles of Econometrics*, 5th Edition.
- [PyMC DiD Example](https://www.pymc.io/projects/examples/en/latest/causal_inference/difference_in_differences.html)
- [BiomedSciAI Card-Krueger Notebook](https://github.com/BiomedSciAI/causallib/blob/master/examples/fast_food_employment_card_krueger.ipynb)
- [Aaronmams R Replication](https://aaronmams.github.io/Card-Krueger-Replication/)
- [Alopatina R Replication](https://github.com/alopatina/Applied-Causal-Analysis/blob/master/Difference%20in%20difference%20Min%20Wages%20and%20Employment%20Card%20and%20Krueger%20replication.ipynb)

## License

[MIT](LICENSE)
