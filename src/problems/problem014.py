
import numpy as np

cutoff = 10  # only numbers smaller than this value are tested
table = np.zeros((cutoff,), dtype="int")  # table[0] is not used

# faster but failing strategy
# doesn't work, since we leave the table,
# use the old strategy for the 3n steps, the new strategy for the 2n steps
#queue = [1]
#while queue:
#    num = queue.pop()
#    new_num1 = 2*num
#    if 0 < new_num1 < cutoff and not table[new_num1]:
#        table[new_num1] = table[num] + 1
#        queue.append(new_num1)
#    if not (num - 1) % 3:
#        new_num2 = (num - 1) // 3
#        if 0 < new_num2 < cutoff and not table[new_num2]:
#            table[new_num2] = table[num] + 1
#            queue.append(new_num2)

for i in range(cutoff):
    if table[i]:
        continue  # already reached that number
    number = i
    history = [number]
    while number > 1:
        if number % 2:
            number = 3*number + 1
        else:
            number = number // 2
        history.append(number)
    for counter, number in enumerate(history[::-1]):
        if number < cutoff:
            table[number] = counter

print np.argmax(table)