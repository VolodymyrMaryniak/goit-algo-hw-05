# Homework 5

## Experiment results

** time - total time of 100 executions

### Experiment 1. Existing pattern
| Algorithm Name   | Text file    | Pattern                    |   Result |      Time |
|------------------|--------------|----------------------------|----------|-----------|
| Rabin-Karp       | article1.txt | елементів у відсортованому |     5988 | 0.344613  |
| KMP              | article1.txt | елементів у відсортованому |     5988 | 0.178611  |
| Boyer-Moore      | article1.txt | елементів у відсортованому |     5988 | 0.0197669 |
| Naive            | article1.txt | елементів у відсортованому |     5988 | 0.165195  |



### Experiment 2. Non-existing pattern
| Algorithm Name   | Text file    | Pattern                          |   Result |      Time |
|------------------|--------------|----------------------------------|----------|-----------|
| Rabin-Karp       | article1.txt | пошук елементів у відсортованому |       -1 | 0.731285  |
| KMP              | article1.txt | пошук елементів у відсортованому |       -1 | 0.367989  |
| Boyer-Moore      | article1.txt | пошук елементів у відсортованому |       -1 | 0.0359942 |
| Naive            | article1.txt | пошук елементів у відсортованому |       -1 | 0.345114  |



### Experiment 3. Existing pattern
| Algorithm Name   | Text file    | Pattern                          |   Result |      Time |
|------------------|--------------|----------------------------------|----------|-----------|
| Rabin-Karp       | article2.txt | Час доступу до окремого елементу |     1224 | 0.0817735 |
| KMP              | article2.txt | Час доступу до окремого елементу |     1224 | 0.0377684 |
| Boyer-Moore      | article2.txt | Час доступу до окремого елементу |     1224 | 0.0046744 |
| Naive            | article2.txt | Час доступу до окремого елементу |     1224 | 0.0334142 |



### Experiment 4. Non-existing pattern
| Algorithm Name   | Text file    | Pattern                          |   Result |      Time |
|------------------|--------------|----------------------------------|----------|-----------|
| Rabin-Karp       | article2.txt | Час доступу до окремого елемента |       -1 | 1.06352   |
| KMP              | article2.txt | Час доступу до окремого елемента |       -1 | 0.529472  |
| Boyer-Moore      | article2.txt | Час доступу до окремого елемента |       -1 | 0.0498219 |
| Naive            | article2.txt | Час доступу до окремого елемента |       -1 | 0.491646  |



## Conclusion
Boyer-Moore text search algorithm shows the best results.