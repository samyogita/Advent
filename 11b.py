import re
s = open('input11.txt').read().split('\n\n')
class monkey:
    def __init__(self, s):
        s = s.splitlines()
        self.values = list(map(int, re.findall(r'\d+', s[1])))
        op1, op, op2 = s[2].split('=')[-1].split()
        self.operands = [op1, op2]
        self.operation = op
        self.test = int(re.findall(r'\d+', s[3])[0])
        self.true_throw = int(re.findall(r'\d+', s[4])[0])
        self.false_throw = int(re.findall(r'\d+', s[5])[0])
        self.inspected = 0
    
    def print(self):
       print(self.values)
       print(self.operands)
       print(self.operation)
       print(self.test)
       print(self.true_throw)
       print(self.false_throw)

    def operate(self, index):
        a, b = self.operands
        if a == 'old':
            a = str(self.values[index])
        if b == 'old':
            b = str(self.values[index])
        new = eval(a+self.operation+b) % mod
        if new % self.test == 0:
            return new, self.true_throw
        else:
            return new, self.false_throw

monkeys = [monkey(x) for x in s]
mod = 1
for x in monkeys:   
    mod *= x.test

for i in range(10000):
    for x in monkeys:
        x.inspected += len(x.values)
        for j in range(len(x.values)):
            value, throw_to = x.operate(j)
            monkeys[throw_to].values.append(value)
        x.values = []
inspect = [x.inspected for x in monkeys]
inspect = sorted(inspect, reverse=True)
print(inspect[0] * inspect[1] )