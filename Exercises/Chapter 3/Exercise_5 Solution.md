# Exercise 5 Solution
## Linear Regression without Intercept


### Question

Consider the fitted values that result from performing linear regression **without an intercept**.  
In this setting, the *i*th fitted value takes the form

$$
\hat{y}_i = x_i \hat{\beta},
$$

where

$$
\hat{\beta} = \frac{\sum_{i=1}^{n} x_i y_i}{\sum_{i'=1}^{n} x_{i'}^2}.
$$

Show that we can write

$$
\hat{y}_i = \sum_{i'=1}^{n} a_{i'} y_{i'}.
$$

What is $a_{i'}$?

---

### Solution

We begin from the definition of the fitted value:

$$
\hat{y}_i = x_i \hat{\beta}.
$$

#### Step 1: Substitute the estimator for $\hat{\beta}$

$$
\hat{y}_i
= x_i \left( \frac{\sum_{i'=1}^{n} x_{i'} y_{i'}}{\sum_{i'=1}^{n} x_{i'}^2} \right).
$$

#### Step 2: Factor out constants

Since $x_i$ and the denominator do not depend on the summation index $i'$, we can write:

$$
\hat{y}_i
= \frac{x_i}{\sum_{k=1}^{n} x_k^2}
\sum_{i'=1}^{n} x_{i'} y_{i'}.
$$

#### Step 3: Distribute the constant inside the sum

$$
\hat{y}_i
= \sum_{i'=1}^{n}
\left(
\frac{x_i x_{i'}}{\sum_{k=1}^{n} x_k^2}
\right)
y_{i'}.
$$

#### Step 4: Identify the coefficients

Comparing with the required form

$$
\hat{y}_i = \sum_{i'=1}^{n} a_{i'} y_{i'},
$$

we identify

$$
\boxed{
a_{i'} = \frac{x_i x_{i'}}{\sum_{k=1}^{n} x_k^2}
}
$$

---

### Interpretation

Each fitted value $\hat{y}_i$ is a **linear combination** of the observed responses $y_1, \dots, y_n$.  
The weights depend only on the predictor values.
