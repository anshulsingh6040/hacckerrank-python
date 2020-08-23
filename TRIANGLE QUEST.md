# TRIANGLE QUEST

You are given a positive integer N . Print a numerical triangle of height N-1 lines like the one below:

![image.png](attachment:image.png)

#### Can you do it using only arithmetic operations, a single for loop and print statement?

Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.


```python
for i in range(6):
    for j in range(i):
        print(i,end='')
    print('\n',end='')
```


```python
for i in range(1,6):
    print((pow(10,i)//9)*i)
```
