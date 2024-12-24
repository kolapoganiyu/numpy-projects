from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a random integer from 0 to 100
x=random.randint(100, size=( 5))
print(x)

# Generating a 3 rows of 5 random integers from 0 to 100
x = random.randint(100, size=(3, 5))
print(x)

# Generating 3 rows of 5 random integer from the inserted list
x = random.choice([5,6,7,8,10], size=(3,5))
print(x)

# Generating random float numbers
x = random.rand()
print(x)

# Generating random numbers using probability density
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(10))
print(x)

# shuffling the array itself
random.shuffle(x)
print(x)

# making the permutation of the array
print(random.permutation(x))


# plotting a DistPlot
sns.distplot([0,1,2,3,4,5], hist=False)

plt.show()

# Differences between normal and Binomial Distribution

sns.distplot(random.normal(loc=50, scale=5, size=100,), hist=False, label="normal")
sns.distplot(random.binomial(n=100,p=0.5, size=1000), hist=False, label="binomial")

plt.show()

# poisson Distribution

sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()

