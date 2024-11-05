### Puzzle 2

Alok has three daughters. His friend Shyam wants to know the ages of his daughters. Alok gives him a first hint. 

![puz2](img|folder/Find-agesof-daughters.png)

1. The product of their age is 72. 

Shyam says this is not enough information Alok gives him a second hint. 

2. The sum of their ages is equal to my house number. 

Shyam goes out and looks at the house number and tells “I still do not have enough information to determine the ages”. 
Alok admits that Shyam can not guess and gives him the third hint 

3. The oldest girl likes strawberry ice cream. 

Shyam is able to guess after the third hint. Can you guess what are the ages of the three daughters? 



### Step 1: List Possible Age Combinations
Since the product of the daughters' ages is 72, let's list all combinations of three positive integers that multiply to 72:

- **(1, 1, 72)** with sum 74
- **(1, 2, 36)** with sum 39
- **(1, 3, 24)** with sum 28
- **(1, 4, 18)** with sum 23
- **(1, 6, 12)** with sum 19
- **(1, 8, 9)** with sum 18
- **(2, 2, 18)** with sum 22
- **(2, 3, 12)** with sum 17
- **(2, 4, 9)** with sum 15
- **(2, 6, 6)** with sum 14
- **(3, 3, 8)** with sum 14
- **(3, 4, 6)** with sum 13

### Step 2: Apply the Second Hint
Alok’s house number (the sum of the ages) didn’t help Shyam determine the ages immediately, meaning there must be multiple combinations with the same sum. From our list, the only sums that repeat are 14:

- **(2, 6, 6)** with sum 14
- **(3, 3, 8)** with sum 14

This implies that Alok's house number is 14.

### Step 3: Apply the Third Hint
The third hint mentions an "oldest" daughter, implying there is one unique oldest daughter. This rules out **(2, 6, 6)** because there isn't a distinct oldest daughter in this combination (two daughters share the age of 6). 

Thus, the only possible ages are **(3, 3, 8)**.

### Conclusion
The ages of Alok’s daughters are **3, 3, and 8**.
