'''
확률 변수(random variable):
    어떤 확률 분포와 연관되어 있느 변수
    (예) 동전 1개를 던지는 확률 분포에서, 동전 앞면의 개수 X
    P(X=1) = 1/2, p(X=0) = 1/2
    (예) 주사위 1개를 던지는 확률 분포에서, 주사위 눈의 개수 X
    X = 1, 2, 3, 4, 5, 6

기대값(expected value)
    확률 변수의 확률에 확률 변수의 값을 가중 평균한 값
    E(x) = sum(x_i * p(X = x_i))
    (예) 주사위 1개를 던질 때, 주사위 눈의 기대값
    E = 1 * 1/6 + 2 * 1/6 + ... + 6 * 1/6 = 3.5

'''

# 동전 3개를 던질 때, 확률 변수를 동전의 앞면의 개수
# X = 0, 1, 2, 3
# 동전 3개를 10,000번 던지는 실험 -> P(X=0), P(X=1), ...
# -> P(X=0) = 1/8, P(X=1) = 3/8, P(X=2) = 3/8, P(X=3) = 1/8
import random
from collections import Counter

experiments = []    # 동전 3개를 10_000 던질때, 동전 앞면의 개수
coin = (0, 1)   # 1 = 앞, 0 = 뒤
trials = 10_000
n_coins = 3
for i in range(trials):
    heads = 0   # 동전 앞면의 개수
    for j in range(n_coins):
        heads += random.choice(coin)
    experiments.append(heads)

head_count = Counter(experiments)
print(head_count)

expected_value = 0
for x, cnt in head_count.items():
    expected_value += x * cnt / trials

print('기대값 =', expected_value)

print()
#########
# 주사위 눈의 기대값
dice = (1, 2, 3, 4, 5, 6)
experiments = [random.choice(dice) for i in range(trials)]
print(experiments)
head_count = Counter(experiments)
print(head_count)
expected_value = 0
for x, cnt in head_count.items():
    expected_value += x * cnt/trials

print('기대값 =', expected_value)