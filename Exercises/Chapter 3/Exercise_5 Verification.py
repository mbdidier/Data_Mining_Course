"""
Exercise 5: Verification of Linear Regression Property
Showing that fitted values are linear combinations of response values
"""

import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample data
n = 50
x = np.random.randn(n)
y = 2 * x + np.random.randn(n) * 0.5

print("=" * 60)
print("Exercise 5: Linear Regression without Intercept")
print("=" * 60)

# Fit regression without intercept
# β̂ = (Σ xi*yi) / (Σ xi²)
beta_hat = np.sum(x * y) / np.sum(x**2)
print(f"\nEstimated β̂ = {beta_hat:.4f}")

# Method 1: Direct calculation of fitted values
# ŷi = xi * β̂
y_hat_direct = x * beta_hat

# Method 2: Using weights a_i' 
# ŷi = Σ a_i' * y_i'
# where a_i' = (xi * xi') / (Σ xj²)
y_hat_weighted = np.zeros(n)
for i in range(n):
    # Calculate weights for observation i
    a = (x[i] * x) / np.sum(x**2)
    # Fitted value is weighted sum of all y values
    y_hat_weighted[i] = np.sum(a * y)

# Verify they're identical
max_diff = np.max(np.abs(y_hat_direct - y_hat_weighted))
print(f"\nMaximum difference between methods: {max_diff:.2e}")
print("(Should be very close to 0)")

# Display the formula for a_i'
print("\n" + "=" * 60)
print("The weight a_i' is:")
print("a_i' = (xi * xi') / (Σ xj²)")
print("=" * 60)

# Example: Show weights for first observation
i = 0
weights = (x[i] * x) / np.sum(x**2)
print(f"\nExample: Weights for observation 1 (x={x[i]:.3f}):")
print(f"Sum of weights: {np.sum(weights):.4f}")
print(f"Fitted value ŷ₁ = {y_hat_direct[i]:.4f}")
print(f"As weighted sum: {y_hat_weighted[i]:.4f}")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Regression line
axes[0].scatter(x, y, alpha=0.6, label='Observed data')
axes[0].plot(x, y_hat_direct, 'r-', linewidth=2, label=f'Fitted line (β̂={beta_hat:.3f})')
axes[0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
axes[0].axvline(x=0, color='k', linestyle='--', alpha=0.3)
axes[0].set_xlabel('x', fontsize=12)
axes[0].set_ylabel('y', fontsize=12)
axes[0].set_title('Linear Regression without Intercept', fontsize=14, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot 2: Weights visualization for a specific point
i_example = 15  # Choose a point to analyze
weights_example = (x[i_example] * x) / np.sum(x**2)
axes[1].scatter(x, weights_example, alpha=0.6, c=np.abs(weights_example), cmap='viridis')
axes[1].axhline(y=0, color='r', linestyle='--', alpha=0.5)
axes[1].axvline(x=x[i_example], color='r', linestyle='--', alpha=0.5, 
                label=f'Point i (x={x[i_example]:.2f})')
axes[1].set_xlabel('xi\' (predictor values)', fontsize=12)
axes[1].set_ylabel('ai\' (weights)', fontsize=12)
axes[1].set_title(f'Weights ai\' for Point {i_example+1}', fontsize=14, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/claude/exercise_3_5_visualization.png', dpi=300, bbox_inches='tight')
print(f"\nVisualization saved to: exercise_3_5_visualization.png")

print("\n" + "=" * 60)
print("Conclusion:")
print("=" * 60)
print("✓ Fitted values can be written as: ŷi = Σ ai' * yi'")
print("✓ where ai' = (xi * xi') / (Σ xj²)")
print("✓ This shows fitted values are LINEAR COMBINATIONS of response values")
print("=" * 60)
