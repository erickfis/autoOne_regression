# Linear regression - OLS Model

In this section, we will cover:

- fitting an OLS linear regression model
- score analysis: MSE and variance explained: $R^2$
- residual analysis
- most important features


## Train-test split

To avoid overfitting, we will split our data on train and test sets.

The model will be trained with the train dataset and later we will evaluate it with the test set.

## Feature Selection

It is very important to carefully chose which features will be included into the model, because:

- including unnecessary features increases the standard error of the coefficients
- excluding necessary features results in bias

### Selection through correlation

We will start selecting features through their correlation with the dependent variable price: if it has correlation, the feature will be included in the model.


With an adjusted $R^2$ score of 0.9691 we can say that it is a really good model already!


## More feature selection: p-values

When we fit a linear regression model, we have to test the hypothesis that the evaluated coefficients for each regressor is actually zero, meaning we don't need the regressor at all.

In other words, we have:

- $H_0$: the coefficient is zero
- $H_1$: the coefficient is not zero

Therefore, let's look into the p-values for each coefficient for each regressor to understand if they should be zero:

*if a p-value of a given coefficient is larger than 5%, then we fail to reject the null hypothesis that the coefficient actually is zero*

As we can see, the p-values for some makers are larger than 5%. We are not removing this feature.

Also, hypothesis testing for variable horsepower coefficient shows it could be zero.

Lets remove this feature and fit the model again:



## Residual analysis

In a good model, we should expect that the residuals:

- have mean zero
- to be homoscedastic
- to be normal
- to have no correlation with the fitted values
- to have no correlation with any of the features


# Linear regression - sklearn

In this section, we will cover:

- fitting different linear regression models with sklearn
- normalization and encoding of features
- score analysis: MSE and variance explained: $R^2$
- residual analysis
- most important features
- comparing the models: conclusions

## Feature selection

This time we will not be manually selecting features. Some sklearn linear regressor models uses regularization, and that should address the lack of feature selection.

This has an important consequence, however: we will be using all features, even the ones which are not linearly correlated with the outcome. This means we will be trying to fit a linear model on a case that may be not strictly linear.

## Normalization and encoding of features

The range of the numeric features varies a lot for each one of them:

- bore range: ~2
- curb range: ~3500

Also, its easy to see that they are measuring completely different things and therefore are in different scales.

In order to properly fit linear regression models with regularization, we must account for those differences.

Also, it is import to encode the categories, like fuel-type, to sklearn can use them.


## Hyper parameter tuning and Cross Validation

It is important to note that we are going to use the gridsearchCV method, so we can iterate over a series of hyper parameters for each model in order to find the best combination of them through cross validation.

## Linear regression model

Lets start trying a simple sklearn linear regression model, without regularization


## Linear regression model - Ridge regularization

Ridge regression uses a penalty L2 factor for the least important regressors.

- L2: least squared deviation $resid = \sum{(y_i - \hat y_i)^2} + \lambda \sum{\beta^2}$

However, the least squares regularization is not robust: it is sensitive to outliers.


### Transformation on data

Preprocessing will be required here:

- feature normalization / scaling

## Regularized models - Lasso

Lasso regression uses a stronger penalty for the least important regressors, the L1.

That said, lasso will perform feature selection and it is not a stable solution.

- L1: least absolute deviation: $resid = \sum{(y_i - \hat y_i)^2} + \lambda \sum{|\beta|}$


## Huber Regressor

Huber uses L2 and L1 penalty. This makes it specially strong against outliers:


## Comparing the models - conclusions

- MSE analysis shows better results for the Linear model: smallest MSE
- $R^2$ analysis shows a tie between Ridge and Linear models
- Ridge model would be the safest choice:
- OLS has a worse performance because it was built on the assumption of a linear phenomena, using only linearly correlated variables.


## Modeling with machine learning

In this section, we will cover:

- fitting different machine learning regression models with sklearn
- score analysis: MSE and variance explained: 𝑅2
- comparing the models: conclusions

## Hyper-parameter tuning and Cross Validation

It is important to note that we are going to use the gridsearchCV method, so we can iterate over a series of hyper-parameters for each model in order to find the best combination of them through cross validation.

## Decision Tree Regressor


Lets start trying a simple sklearn decision tree regression model.


## k-nearest neighbors


## Random Forests

Random Forests are ensemble machine learning methods.

Ensemble methods are a combination of predictions from several learning algorithms. This makes them robust (not sensitive to outliers) and with improved power of generalization.

In particular, Random Forests is a averaging ensemble method: several estimators are built independently and then the predictions are averaged. This reduces variance and thus they perform better than any single estimator.


## Gradient tree boosting


The gradient tree boosting is an ensemble machine learning methods too, but this time we have the boosting class: several weak models are combined to produce a powerful estimator with reduced bias.

This method is very robust because it uses regularization.


Adaboost is another ensemble machine learning method of the boosting class.

This time, however, we can start with the best model we have so far. Then, copies of the original model will be fitted on the same dataset, but weights will be attributed to them according to the error of the prediction.

Lets use our previously trained Random Forests regressor.

## Conclusions

Considering the computation time and the error measured on the test set, we can conclude:

- OLS, with proper feature selection, would be chosen over sklearn. However, its important to consider the time it takes to manually choose those features
- Ridge Regression performs better than the alternative linear regressors: it produces the best model among them without, within a really good time while automatically adjusting the weights of each feature, so we don't need to manually select them
- among the ML models, its important to note that the KNN model took 30x less time to produce a model as good as the alternatives.
- among the ML models, its important to note that the KNN model took 10x less time to produce a model almost as good as the alternatives.
- ML have 5x improved performance (RMSE) over Linear Models because it doesn't rely on the linear correlations between predictors and the outcome.
- The linear models could have better performance if we added the contributions of interdependent terms or non-linear transformations of them.
