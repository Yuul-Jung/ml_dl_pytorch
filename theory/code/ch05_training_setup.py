"""제05장 학습 설정 선택 기준 — Target 판별, 데이터 분리 비율, 불균형 데이터의 지표, 전처리 누수를 NumPy로 확인한다.

실행: python ch05_training_setup.py
필요: Python 3, NumPy
"""
import numpy as np

rng = np.random.default_rng(0)


def section(title):
    print(f"\n[{title}]")


def choose(y):
    # 정답 y의 자료형과 모양만 보고 문제 유형과 손실함수를 고른다
    y = np.asarray(y)
    if np.issubdtype(y.dtype, np.integer) and y.ndim == 1:
        return "다중분류 → 출력 C개 Logit, CrossEntropyLoss"
    if y.ndim == 2 and set(np.unique(y)) <= {0.0, 1.0}:
        if y.shape[1] == 1:
            return "이진분류 → 출력 1개 Logit, BCEWithLogitsLoss"
        return "다중레이블 → 출력 C개 Logit, BCEWithLogitsLoss"
    return "회귀 → 출력 1개 실수, MSELoss 또는 L1Loss"


section("1. Target 모양으로 문제 유형 고르기")
examples = {
    "집값 [N,1] float": np.array([[3.5], [2.1]]),
    "합격 [N,1] 0/1 float": np.array([[1.0], [0.0]]),
    "숫자 [N] long": np.array([7, 2, 1]),
    "태그 [N,4] 0/1 float": np.array([[1.0, 1.0, 0.0, 1.0]]),
}
for name, y in examples.items():
    print(f"{name:<22} → {choose(y)}")

section("2. 데이터 분리: Train 80% / Test 20%, 다시 Train의 20%를 Validation")
n = 10_000
n_test = int(n * 0.2)
n_val = int((n - n_test) * 0.2)
print(f"Train {n - n_test - n_val:,} ({(n - n_test - n_val) / n:.0%})  "
      f"Validation {n_val:,} ({n_val / n:.0%})  Test {n_test:,} ({n_test / n:.0%})")

section("3. 불균형 데이터: 양성 5%인데 전부 0이라고 예측하면")
y = np.zeros(1000, dtype=int)
y[:50] = 1
pred = np.zeros(1000, dtype=int)
tp = int(((pred == 1) & (y == 1)).sum())
fn = int(((pred == 0) & (y == 1)).sum())
fp = int(((pred == 1) & (y == 0)).sum())
acc = (pred == y).mean()
recall = tp / (tp + fn)
precision = tp / (tp + fp) if tp + fp else 0.0
print(f"Accuracy {acc:.3f}  Precision {precision:.3f}  Recall {recall:.3f}")

section("4. 표준화: Train 통계만 쓰기 vs Test 통계를 쓰는 누수")
train = rng.normal(50, 10, 800)
test = rng.normal(60, 10, 200)            # Test 분포가 조금 다르다고 가정
mu, sd = train.mean(), train.std()
right = (test - mu) / sd
leak = (test - test.mean()) / test.std()
print(f"Train 기준 변환 후 Test 평균 {right.mean():+.3f}  (분포 차이가 그대로 드러난다)")
print(f"Test 기준 변환 후 Test 평균 {leak.mean():+.3f}  (차이가 지워져 성능을 잘못 평가한다)")
