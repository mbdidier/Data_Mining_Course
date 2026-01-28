# Exercise 5 Solution
## Linear Regression without Intercept

**Problem:** Consider the fitted values from linear regression without an intercept. The ith fitted value takes the form:

$$\hat{y}_i = x_i\hat{\beta}$$

where

$$\hat{\beta} = \frac{\sum_{i=1}^{n} x_i y_i}{\sum_{i'=1}^{n} x_{i'}^2}$$

Show that we can write:

$$\hat{y}_i = \sum_{i'=1}^{n} a_{i'} y_{i'}$$

**What is $a_{i'}$?**

---

## Solution

### Step 1: Start with the fitted value formula

$$\hat{y}_i = x_i\hat{\beta}$$

### Step 2: Substitute the expression for $\hat{\beta}$

$$\hat{y}_i = x_i \cdot \frac{\sum_{i'=1}^{n} x_{i'} y_{i'}}{\sum_{i'=1}^{n} x_{i'}^2}$$

### Step 3: Distribute $x_i$ into the summation

Since $x_i$ and the denominator are constants with respect to the summation over $i'$:

$$\hat{y}_i = \frac{x_i}{\sum_{i'=1}^{n} x_{i'}^2} \sum_{i'=1}^{n} x_{i'} y_{i'}$$

$$\hat{y}_i = \sum_{i'=1}^{n} \frac{x_i x_{i'}}{\sum_{i'=1}^{n} x_{i'}^2} y_{i'}$$

### Step 4: Identify $a_{i'}$

Comparing with $\hat{y}_i = \sum_{i'=1}^{n} a_{i'} y_{i'}$, we get:

$$\boxed{a_{i'} = \frac{x_i x_{i'}}{\sum_{j=1}^{n} x_j^2}}$$

---
