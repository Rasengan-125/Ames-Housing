# Ames Housing

Exploratory data analysis on the Ames, Iowa housing dataset (Kaggle's House Prices competition),
starting with cleaning and moving toward predictive modeling.

## About this project

Unlike the Titanic project, which built up its rigor along the way, this one applies that same
process from the start: testing assumptions instead of accepting surface-level patterns, checking
before dropping or filling a column, and following up on surprising findings instead of glossing
over them.

## Structure

```
ames-housing/
├── notebooks/
│   ├── 01_cleaning.ipynb    missing value investigation and cleaning
│   ├── 02_eda.ipynb          univariate, bivariate, and multivariate analysis
├── data/
│   ├── train.csv              original, untouched
│   ├── train_cleaned.csv      checkpoint produced by 01_cleaning.ipynb
├── README.md
```

## Cleaning

Every missing value was investigated before being filled, not filled by default. Several columns
required catching genuine data-entry gaps hiding inside otherwise clean "does not apply" patterns:

- Garage, Basement, Pool, Misc, Alley, Fence, and Fireplace columns were confirmed as "no feature"
  rather than missing data, using a numeric counterpart (area, count) or the data description.
- Two rows in the Basement columns and several rows in MasVnr and Misc had a real value in one
  field but a missing or zero value in the related field. Each was resolved individually rather
  than swept into the bulk fill.
- `LotFrontage` was filled using a neighborhood-based median rather than a flat mean, validated by
  checking how well it would have predicted the known values before committing to it.

Full reasoning and code is in [`01_cleaning.ipynb`](./notebooks/01_cleaning.ipynb).

## Key findings

1. `OverallQual` is the strongest predictor of `SalePrice` (r = 0.79), ahead of every column in
   the original hypothesis.
2. `GrLivArea` (living area) is a strong predictor (r = 0.71), confirming part of the original
   guess. `LotArea` (land area) is the weakest (r = 0.26), the opposite of what was expected.
   Two follow-up theories for the weak `LotArea` correlation were tested and ruled out.
3. `NoRidge` and `NridgHt` are genuinely the highest-priced neighborhoods, not just
   overrepresented among price outliers. `NAmes`, the most common neighborhood by sales volume,
   turned out to be old housing stock with average quality rather than a value neighborhood.
4. `YearBuilt` correlates moderately with `OverallQual` (r = 0.57). `Neighborhood` was tested as a
   possible confounder and ruled out: the relationship holds, and varies in strength, within
   individual neighborhoods rather than collapsing once controlled for.
5. Houses with no fence had a higher average `SalePrice` than any fenced category, a
   counterintuitive finding only partially explained by slightly larger lot sizes.
6. A month-sold price pattern (September highest, April lowest) turned out to be fully explained
   by house size and quality differing by month, not a seasonal effect on price itself.

Full reasoning and code is in [`02_eda.ipynb`](./notebooks/02_eda.ipynb).

## Data cleaning summary

- Dropped `Id` (row index, no analytical value)
- Filled Garage, Basement, Pool, Misc, Alley, Fence, and FireplaceQu categorical columns with
  `"None"` where confirmed to mean no feature present
- Filled `Electrical` (single genuine gap) with the mode
- Filled `LotFrontage` using each house's neighborhood median

## Tech stack

Python, Pandas, Matplotlib, Seaborn, in Jupyter notebooks.

## Next steps

EDA phase complete. Next: predictive modeling, building on `OverallQual`, `GrLivArea`, and
`Neighborhood` as the strongest candidate features.
