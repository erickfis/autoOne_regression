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
