"""제04장 합성곱 신경망(CNN) — 슬라이드의 합성곱·패딩·풀링·특징 추출 예제와 출력 크기·파라미터 수를 NumPy로 계산한다.

실행: python ch04_cnn.py
필요: Python 3, NumPy
"""
import numpy as np


def section(title):
    print(f"\n[{title}]")


def conv2d(x, k, stride=1, pad=0):
    # 딥러닝 프레임워크의 합성곱: 필터를 뒤집지 않고 겹친 원소끼리 곱해 더한다
    x = np.pad(x, pad)
    kh, kw = k.shape
    oh = (x.shape[0] - kh) // stride + 1
    ow = (x.shape[1] - kw) // stride + 1
    out = np.zeros((oh, ow), dtype=x.dtype)
    for i in range(oh):
        for j in range(ow):
            out[i, j] = (x[i * stride:i * stride + kh, j * stride:j * stride + kw] * k).sum()
    return out


def pool2x2(x, how=np.max):
    h, w = x.shape
    return how(x.reshape(h // 2, 2, w // 2, 2), axis=(1, 3))


section("1. 합성곱 + 편향 → 특징 맵 (4×4 입력, 3×3 필터)")
x = np.array([[1, 2, 3, 0],
              [0, 1, 2, 3],
              [3, 0, 1, 2],
              [2, 3, 0, 1]])
k = np.array([[2, 0, 1],
              [0, 1, 2],
              [1, 0, 2]])
c = conv2d(x, k)
print("합성곱 결과\n", c)
print("편향 3을 더한 특징 맵\n", c + 3)

section("2. 패딩 1: 4×4 → 4×4")
print(conv2d(x, k, pad=1))

section("3. 2×2 풀링: [[15,16],[6,15]]")
p = np.array([[15, 16], [6, 15]])
print("max", p.max(), " min", p.min(), " average", p.mean())

section("4. 숫자 2 이미지(6×6)에 필터 3개 적용, 편향 -1 → ReLU → 2×2 최대 풀링")
img = np.array([[0, 0, 1, 1, 0, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 1, 1, 1, 1, 0]])
filters = {
    "가로": np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]]),
    "대각선": np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]),
    "세로": np.array([[0, 0, 1], [0, 0, 1], [0, 0, 1]]),
}
for name, f in filters.items():
    fmap = conv2d(img, f) - 1
    relu = np.maximum(fmap, 0)
    print(f"{name} 필터 ReLU 결과 {relu.tolist()}  풀링 {pool2x2(relu).tolist()}")

section("5. 출력 크기 = floor((입력 - 필터 + 2×패딩) / 스트라이드) + 1")
for p_, s_ in [(0, 1), (1, 1), (0, 2), (1, 2)]:
    out = (28 - 3 + 2 * p_) // s_ + 1
    print(f"28×28, 필터 3, padding={p_}, stride={s_} → {out}×{out}")

section("6. 2단 CNN의 Shape와 파라미터 수")
shape = [1, 28, 28]
total = 0
for kind, arg in [("conv", (1, 8)), ("pool", None), ("conv", (8, 16)), ("pool", None)]:
    if kind == "conv":
        cin, cout = arg
        n = cin * cout * 3 * 3 + cout     # 필터 가중치 + 출력 채널별 편향
        total += n
        shape = [cout, shape[1], shape[2]]
        print(f"Conv2d({cin},{cout},3,padding=1) → {shape}  파라미터 {n:,}")
    else:
        shape = [shape[0], shape[1] // 2, shape[2] // 2]
        print(f"MaxPool2d(2,2) → {shape}")
flat = shape[0] * shape[1] * shape[2]
n = flat * 10 + 10
total += n
print(f"Flatten → [{flat}]  Linear({flat},10) 파라미터 {n:,}")
print(f"전체 파라미터 {total:,}")

section("7. 입력 채널이 2개일 때: 채널별 결과를 더해 출력 채널 1개")
x2 = np.stack([x, x.T])
k2 = np.stack([k, np.eye(3, dtype=int)])
per_channel = [conv2d(x2[i], k2[i]) for i in range(2)]
print("채널 1 결과\n", per_channel[0])
print("채널 2 결과\n", per_channel[1])
print("합 = 출력 채널 1개\n", per_channel[0] + per_channel[1])
