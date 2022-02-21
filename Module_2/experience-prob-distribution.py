#!/usr/bin/env python
# coding: utf-8

# ##### Q.1 
# 
# Consider the loaded die with the following probabilities:
# ```
#     p(1) = 0.3/6
#     p(2) = 0.7/6
#     p(3) =   2/6
#     p(4) = 0.5/6
#     p(5) = 0.2/6
#     p(6) = 2.3/6
# ```
# 

# ##### Q.2 
# * Plot the probability distribution above
#   * Select the most appropriate visualization to do so.

# In[3]:


# Add your plot code here
#Code followed from class
def loaded_die_distribution (face):
    try:
        dist = {1:0.3/6, 2:0.7/6, 3:2/6, 4:0.5/6, 5:0.2/6, 6:2.3/6}
        return dist[face]
    except:
        raise("%s is not a valid die face %d" % face)
sample_space = list(range(1,7))
p_x = [loaded_die_distribution (f) for f in sample_space]

plt.figure(figsize=(10, 4))
plt.bar(sample_space, p_x)

plt.xlabel('Die face obtained')
plt.ylabel('probability')


# ##### Q.3 
# * Based only on the plot above, can you predict the mean value of a random variable consisting of values obtaining from rolling a die  that follows the probability distribution given above? Explain your reasoning.

# # Write you answer here
# You are able to predict the mean value of a random variable vonsisting of values obtaining from rolling a die that follows the probability distribution by looking at where the data seems to center/ This would be more towards 6. It is between 3 and 6.

# ##### Q.4
# * Sample 5000 die rolls such that the probabilities of obtaining the values 1 through 6 are distributed according probabilities above. Use these samples to estimate the mean of the random variable. 
# 

# In[6]:


# Write you code here
import random
for _ in range(5000):
    print (np.random.choice([1, 2, 3, 4, 5, 6], 
                            p=[0.3/6, 0.7/6, 2/6, 0.5/6, 0.2/6, 2.3/6]
                           ), 
           end= ' ')
from collections import Counter
roll_random_var_list = []
for i in range(5000):
    roll_random_var = np.random.choice([1, 2, 3, 4, 5, 6], 
                                       p=[0.3/6, 0.7/6, 2/6, 0.5/6, 0.4/6, 2.1/6])
    roll_random_var_list.append(roll_random_var)

counts = Counter(roll_random_var_list)

sorted_counts = dict(sorted(counts.items()))
print(sorted_counts)
plt.figure(figsize=(12,4))
_ = plt.bar(sorted_counts.keys(), sorted_counts.values())


# ##### Q.5 
# 
# * Does the mean match your prediction in Q.3 above? Explain your answer.
# 

# # Write you answer here
# The code does somewhat support my prediction in !uestion 3, as it shows most of the data focusing on the value of 6 being a common occurence.
