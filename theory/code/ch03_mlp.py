"""제03장 다층 퍼셉트론(MLP) — 파라미터 수, 배치·반복 수, 순전파 Shape, Dropout, 역전파를 NumPy로 확인한다.

실행: python ch03_mlp.py
필요: Python 3, NumPy
"""
import math

import numpy as np

rng = np.random.default_rng(0)


def section(title):
    print(f"\n[{title}]")


section("1. 파라미터 수: 784 → 128 → 10")
layers = [(784, 128), (128, 10)]
total = 0
for n_in, n_out in layers:
    count = n_in * n_out + n_out          # 가중치 + 편향
    total += count
    print(f"Linear({n_in}, {n_out}): {n_in}×{n_out} + {n_out} = {count:,}")
print(f"합계 = {total:,}")

section("2. 배치·반복·에폭")
n_train, batch, epochs = 55_000, 64, 5
iters = math.ceil(n_train / batch)
print(f"에폭당 반복 = ceil({n_train:,} / {batch}) = {iters}")
print(f"마지막 배치 크기 = {n_train - (iters - 1) * batch}")
print(f"{epochs} 에폭 총 갱신 = {iters * epochs:,}")

section("3. 순전파 Shape: [N,1,28,28] → [N,10]")
N = 4
images = rng.random((N, 1, 28, 28))
W1, b1 = rng.normal(0, 0.05, (784, 128)), np.zeros(128)
W2, b2 = rng.normal(0, 0.05, (128, 10)), np.zeros(10)
h0 = images.reshape(N, -1)                # Flatten: 배치 차원 N은 유지
h1 = np.maximum(0, h0 @ W1 + b1)          # Linear + ReLU
logits = h1 @ W2 + b2
print("Flatten", h0.shape, "→ 은닉층", h1.shape, "→ Logits", logits.shape)

section("4. Dropout(p=0.2): 학습 때만 끄고, 남은 값은 1/(1-p)배")
a = np.ones(10)
mask = rng.random(10) >= 0.2
print("학습 모드 출력 =", np.round(a * mask / 0.8, 2))
print("평가 모드 출력 =", a)
many = (rng.random((100_000, 10)) >= 0.2) / 0.8
print("학습 모드 평균 ≈", round(float(many.mean()), 3), "(평가 모드와 기대값이 같다)")

section("5. 역전파: 연쇄법칙 기울기와 수치 기울기 비교 (작은 MLP)")
x = rng.normal(size=(3, 4))
t = np.array([0, 2, 1])
A, B = rng.normal(size=(4, 5)), rng.normal(size=(5, 3))


def loss_fn(A, B):
    h = np.maximum(0, x @ A)
    z = h @ B
    z = z - z.max(axis=1, keepdims=True)
    p = np.exp(z) / np.exp(z).sum(axis=1, keepdims=True)
    return -np.log(p[np.arange(3), t]).mean(), h, p


loss, h, p = loss_fn(A, B)
dz = p.copy()
dz[np.arange(3), t] -= 1
dz /= 3                                   # 평균 손실이므로 배치 크기로 나눈다
dB = h.T @ dz
dh = dz @ B.T
dA = x.T @ (dh * (h > 0))                 # ReLU 기울기: 양수면 1, 아니면 0
eps = 1e-6
A2 = A.copy()
A2[0, 0] += eps
A3 = A.copy()
A3[0, 0] -= eps
numeric = (loss_fn(A2, B)[0] - loss_fn(A3, B)[0]) / (2 * eps)
print(f"손실 {loss:.4f}")
print(f"dL/dA[0,0]  연쇄법칙 {dA[0, 0]:.6f}  수치 {numeric:.6f}")

section("6. 활성화 함수 없이 Linear 두 개를 쌓으면 Linear 하나와 같다")
x1 = rng.normal(size=(5, 1))
L1_W, L1_b = rng.normal(size=(1, 8)), rng.normal(size=8)
L2_W, L2_b = rng.normal(size=(8, 1)), rng.normal(size=1)
stacked = (x1 @ L1_W + L1_b) @ L2_W + L2_b
merged_W = L1_W @ L2_W                    # [1,8] @ [8,1] = [1,1]
merged_b = L1_b @ L2_W + L2_b
single = x1 @ merged_W + merged_b
print(f"두 층 결과와 합친 한 층 결과의 최대 차이 = {np.abs(stacked - single).max():.1e}")
with_relu = np.maximum(0, x1 @ L1_W + L1_b) @ L2_W + L2_b
print("ReLU를 넣으면 최대 차이 =", round(float(np.abs(with_relu - single).max()), 4))
