# Data cleaning

In this notebook we will explore the dataset characteristics in order to clean and prepare it for analysis and modeling.

## Getting the data

As we can see, the missing data is marked as '?' in this dataset.
Lets start by replacing it with proper missing data indicators. After that we can check the data types for each feature.

## Missing data

With proper missing data indicators, we can have a better understanding of the quality of each record in the dataset and in each one of its features.


With 20% of missing data for normalized_losses, we will just drop this feature entirely as it won't help us creating any prediction model.

For the other features, as they have only a small portion of missing data, we will use them. However, we will drop the records containing missing data.


## Exploring and transforming the features

Now we will explore each feature individually.

The first thing to do is to understand what features should be considered as categories and what features should be considered as numeric. This is very important for building predictive models later.

Now that we have our categories properly addressed, lets write them down so we can use this information later.

We will new export the treated data.

Also, we will create a python script containing a function for running all the tasks we just did, so we can transform this and new data as well when the need arises.

# Data analysis

Now that our data is clean and ready, we will take a closer look on it.

In this section, we will cover:

- Analysis of sample distribution
- Normalizing the distribution
- Outliers
- Balancing the data


## Analysis of sample distribution

The goal here is to understand what distribution the variable prices follow.
Understanding the behavior of the data is essential for building good prediction models.


count      193.000000
mean     13285.025907
std       8089.082886
min       5118.000000
25%       7738.000000
50%      10245.000000
75%      16515.000000
max      45400.000000


Important characteristics of the prices distribution:

- mean: U$ 13285.02
- median: U$ 10245.00
- standard deviation: U$ 8089.08
- range: U$ 40282.00

The prices distribution is bimodal with peaks around U$8500.00 and U$34000.00 The prices go from $5118.00 to U$45400.00. There are outliers included in this sample: prices above U$38000.00 have only two data points.

Lets take a look on some stats:


## Discussion about outliers

There are 02 data points on the far end of the observed data which 01 observations each. For this exercise, we are assuming them to be outliers.

Because those points could be highly influential points and could leverage predictive models. Therefore, we are removing them.


## Log transformation on prices

As we saw in data analysis, the price variable has a really wide range and its highly skewed. Linear regression predictive algorithms will have some trouble, sometimes even predicting negative prices.

To better understand the patterns of the data and the correlation between the variable price and the independent variables, we will apply a log transformation on prices.

This transformation reshapes the distribution reducing its skewness.


## Balancing the data

### Splitting cars in classes according to its price

Just to take a look into the distribution of prices and into the samples available for each price range, lets define car classes according to price ranges:


### Balancing the data: bootstrap

Our dataset has only 197 observations and some price ranges are not well represented here.
We will fix this balance issue through bootstrap: lets get more samples for each price range through bootstrap:


From this brief analysis about prices, we found that:

- the distribution is not normal - could be bimodal as well
- there are outliers and we removed them
- a log transformation on prices would be useful for linear models, since it reduces the skewness in prices distribution
- there is no balance on price ranges: we addressed that through bootstrap.
