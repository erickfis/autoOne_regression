# Data cleaning

In this notebook we will explore the dataset characteristics in order to clean and prepare it for analysis and modeling.

## Getting the data

This dataset has handled to me through e-mail. I not sure whether or where it can be found over the web. I saw Microsoft using the same dataset on a training. In the future I'll try to include the source here.

As we can see, the missing data is marked as '?' in this dataset.
Lets start by replacing it with proper missing data indicators. After that we can check the data types for each feature.

## Missing data

With proper missing data indicators, we can have a better understanding of the quality of each record in the dataset and in each one of its features

### Strategies for dealing with missing data

A number of different strategies can be used for dealing with missing data:

- data imputation, filling NANs through mean or median by feature
- same as above, but taking data structure in consideration, ie, the mean of normalized losses grouped by make
- just dropping the data

It is important to notice that some knowledge on the business domain would be required for making the proper assumptions for executing data imputation.

As this is not the case, we don't have any understanding on the business rules here, we chose to deal with the missing data by just dropping it.

Therefore:

- With 20% of missing data for normalized_losses, we will just drop this feature entirely
- for the other features, as they have only a small portion of missing data, 2% max, we will use them but we will drop the observations containing missing data.


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

The prices distribution is bimodal with peaks around U$8500.00 and U$34000.00 The prices go from $5118.00 to U$45400.00.


Prices above \\$38000.00 have only 03 observations. While it is very tempting to call them outliers, this is not really the case. We have sales at

- \\$41315.00
- \\$40960.00
- \\$45400.00

As those prices are in the same level as the prices of the regular sales, it becomes clear that they are not recorded by mistake. Those observations are just really rare on this sample.


Lets take a look on some stats:


## Discussion about outliers

There are 02 data points on the far end of the observed data which 01 observations each. For this exercise, we are assuming them to be outliers.

If there was outliers among the observations we would remove them because outliers could be highly influential points and could leverage predictive models.


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
