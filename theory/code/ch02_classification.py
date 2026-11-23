"""제02장 분류 — 시그모이드·BCE·소프트맥스·크로스엔트로피의 수치 예제를 NumPy로 계산한다.

실행: python ch02_classification.py
필요: Python 3, NumPy
"""
import numpy as np


def section(title):
    print(f"\n[{title}]")


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def bce(p, y):
    # 이진 크로스엔트로피: 정답이 1이면 -log(p), 0이면 -log(1-p)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))


def softmax(z):
    # 가장 큰 값을 빼도 결과는 같고, exp 오버플로를 막는다
    e = np.exp(z - np.max(z))
    return e / e.sum()


section("1. 시그모이드: 어떤 실수든 0~1 사이로")
for z in [-10, -2, 0, 2, 10]:
    print(f"z={z:+3d}  sigmoid={sigmoid(z):.4f}")

section("2. BCE: 맞게 확신하면 작고, 틀리게 확신하면 크다")
for p, y in [(0.9, 1), (0.6, 1), (0.1, 1), (0.1, 0), (0.9, 0)]:
    print(f"p={p:.1f} y={y}  loss={bce(p, y):.4f}")

section("3. BCE 기울기 = (sigmoid(z) - y) * x  (수치 미분으로 확인)")
x, y, w, b = 2.0, 1.0, 0.3, -0.1
z = w * x + b
analytic = (sigmoid(z) - y) * x
eps = 1e-6
numeric = (bce(sigmoid((w + eps) * x + b), y) - bce(sigmoid((w - eps) * x + b), y)) / (2 * eps)
print(f"해석적 기울기 {analytic:.6f}  수치 기울기 {numeric:.6f}")

section("4. 소프트맥스: 점수 [2.0, 1.0, 0.1] → 확률")
logits = np.array([2.0, 1.0, 0.1])
s = softmax(logits)
print("확률 =", np.round(s, 4), " 합 =", round(float(s.sum()), 4))
print("시그모이드 각각 =", np.round(sigmoid(logits), 4), " 합 =", round(float(sigmoid(logits).sum()), 4))

section("5. 크로스엔트로피: 정답 클래스의 -log(확률)")
for k, name in enumerate(["a(정답 0번)", "b(정답 1번)", "c(정답 2번)"]):
    print(f"정답 {name}: 정확한 확률 사용 {-np.log(s[k]):.4f} / 반올림 확률 사용 {-np.log([0.7, 0.2, 0.1][k]):.4f}")

section("6. 크로스엔트로피 기울기 = 소프트맥스 확률 - 원핫 정답")
onehot = np.array([1.0, 0.0, 0.0])
print("s - y =", np.round(s - onehot, 4))

section("7. 큰 점수에서도 안전한 소프트맥스")
big = np.array([1000.0, 1001.0, 1002.0])
with np.errstate(over="ignore", invalid="ignore"):
    naive = np.exp(big) / np.exp(big).sum()
print("그대로 계산 =", naive)
print("최댓값을 빼고 계산 =", np.round(softmax(big), 4))
