"""제01장 선형회귀 — 강의 슬라이드의 수치 예제를 NumPy로 다시 계산한다.

실행: python ch01_linear_regression.py
필요: Python 3, NumPy
"""
import numpy as np


def section(title):
    print(f"\n[{title}]")


# 1) 비용 함수 cost(W): H(x) = Wx, 데이터 (1,1) (2,2) (3,3)
x = np.array([1.0, 2.0, 3.0])
y = np.array([1.0, 2.0, 3.0])


def cost(w):
    # 평균 제곱 오차(MSE): 오차를 제곱해 평균한다
    return np.mean((w * x - y) ** 2)


section("1. W에 따른 비용")
for w in [0.0, 1.0, 2.0, -3.0, 5.0]:
    print(f"W={w:+.1f}  cost={cost(w):.4f}")

# 2) 경사하강법: cost(W) = (1/m)Σ(Wx-y)² 의 기울기는 (2/m)Σ(Wx-y)x
section("2. 경사하강법 (W=5에서 시작, 학습률 0.1)")
w = 5.0
lr = 0.1
for step in range(1, 11):
    grad = 2 * np.mean((w * x - y) * x)   # 1/m 평균 기준 기울기
    w = w - lr * grad
    if step in (1, 2, 3, 5, 10):
        print(f"step {step:2d}  W={w:.4f}  cost={cost(w):.6f}")

# 3) 학습률이 너무 크면 발산한다
section("3. 학습률 비교 (W=5에서 5번 갱신)")
for lr in [0.01, 0.1, 0.25]:
    w = 5.0
    for _ in range(5):
        w -= lr * 2 * np.mean((w * x - y) * x)
    print(f"lr={lr:<5} W={w:.4f}")

# 4) 다변수 선형회귀: H(X) = XW + b, X는 [5,3], W는 [3,1]
section("4. 행렬로 계산한 다변수 가설")
X = np.array([[73, 80, 75],
              [93, 88, 93],
              [89, 91, 90],
              [96, 98, 100],
              [73, 66, 70]], dtype=float)
Y = np.array([[152], [185], [180], [196], [142]], dtype=float)
W = np.array([[1.0], [0.5], [0.5]])   # 설명용 임의 가중치
b = 0.0
H = X @ W + b
print("X shape", X.shape, "W shape", W.shape, "H shape", H.shape)
print("H =", H.ravel())

# 5) 정답에 가장 가까운 W, b: 최소제곱해(정규방정식)로 확인
section("5. 최소제곱해로 찾은 W, b")
X1 = np.hstack([X, np.ones((5, 1))])          # 편향 b를 위한 1 열 추가
theta, *_ = np.linalg.lstsq(X1, Y, rcond=None)
pred = X1 @ theta
print("W =", np.round(theta[:3].ravel(), 4), " b =", round(float(theta[3, 0]), 4))
print("예측 =", np.round(pred.ravel(), 2))
print("MSE =", round(float(np.mean((pred - Y) ** 2)), 4))

# 6) 출력이 2개일 때 W의 모양: [n,3] @ [3,2] = [n,2]
section("6. 출력 2개일 때의 W 모양")
W2 = np.ones((3, 2))
print("[5,3] @", list(W2.shape), "=", list((X @ W2).shape))
