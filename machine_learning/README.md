# 머신러닝 기초 (machine_learning)

NumPy·PyTorch Tensor에서 출발해 선형회귀, 로지스틱·Softmax 분류, 학습 설정 선택 기준까지 다루는 과정입니다. 은닉층 없는 선형 모델로 **학습의 기본 원리**(순전파 → 손실 → 경사하강법 → 평가)를 익힙니다.

- 학습 안내서: [`dist/index.html`](dist/index.html)
- 다음 과정: [딥러닝 실습](../deep_learning/)

## 장 구성

| 장 | 제목 | 내용 | 안내서 |
|---|---|---|---|
| 01 | Tensor 기초 | NumPy 배열 → PyTorch Tensor → 연산 → 자동 미분 | [`ch01_tensor_basics_v03.html`](dist/ch01_tensor_basics_v03.html) |
| 02 | 선형회귀 | 순전파·손실 → 비용 최소화 → 실제 데이터 → 주택가격 예측 | [`ch02_linear_regression_v03.html`](dist/ch02_linear_regression_v03.html) |
| 03 | 로지스틱·Softmax 분류 | 이진분류 → 실제 CSV → 다중분류 → 학습 최적화 | [`ch03_classification_v03.html`](dist/ch03_classification_v03.html) |
| 04 | 학습 설정 선택 기준 | Target 형태 → 출력층 → Loss → Optimizer → Metric | [`ch04_training_setup_guide_v04.html`](dist/ch04_training_setup_guide_v04.html) |

## 노트북 순번 대응표

| 새 순번 | 노트북 | 원본 파일 | 비고 |
|---|---|---|---|
| ch01_1 | [`ch01_1_numpy_torch.ipynb`](notebooks/ch01_1_numpy_torch.ipynb) | `ch01_1_numpy_torch.ipynb` | 원본에 실행 결과 없음 |
| ch01_2 | [`ch01_2_numpy_and_tensor.ipynb`](notebooks/ch01_2_numpy_and_tensor.ipynb) | `ch01_2_numpy_and_tensor.ipynb` | 원본에 실행 결과 없음 |
| ch01_3 | [`ch01_3_tensor_operations.ipynb`](notebooks/ch01_3_tensor_operations.ipynb) | `ch01_3_tensor_operations.ipynb` | 원본에 실행 결과 없음 |
| ch02_1 | [`ch02_1_linear_forward_and_loss.ipynb`](notebooks/ch02_1_linear_forward_and_loss.ipynb) | `ch02_1_linear_forward_and_loss.ipynb` | — |
| ch02_2 | [`ch02_2_linear_regression_neural_network.ipynb`](notebooks/ch02_2_linear_regression_neural_network.ipynb) | `ch02_2_linear_regression_neural_network.ipynb` | — |
| ch02_3 | [`ch02_3_minimizing_cost.ipynb`](notebooks/ch02_3_minimizing_cost.ipynb) | `ch02_3_minimizing_cost.ipynb` | — |
| ch02_4 | [`ch02_4_linear_regression.ipynb`](notebooks/ch02_4_linear_regression.ipynb) | `ch02_4_linear_regression.ipynb` | — |
| ch02_5 | [`ch02_5_multi_variable_linear_regression.ipynb`](notebooks/ch02_5_multi_variable_linear_regression.ipynb) | `ch02_5_multi_variable_linear_regression.ipynb` | — |
| ch02_6 | [`ch02_6_housing_price_prediction.ipynb`](notebooks/ch02_6_housing_price_prediction.ipynb) | `ch02_6_housing_price_prediction.ipynb` | `housing.csv` 경로 수정 |
| ch03_1 | [`ch03_1_logistic_classification.ipynb`](notebooks/ch03_1_logistic_classification.ipynb) | `ch03_1_logistic_classification.ipynb` | — |
| ch03_2 | [`ch03_2_heart_disease_classification.ipynb`](notebooks/ch03_2_heart_disease_classification.ipynb) | `ch03_2_heart_disease_classification.ipynb` | — |
| ch03_3 | [`ch03_3_softmax_classification.ipynb`](notebooks/ch03_3_softmax_classification.ipynb) | `ch03_3_softmax_classification.ipynb` | — |
| ch03_4 | [`ch03_4_iris_multiclass_classification.ipynb`](notebooks/ch03_4_iris_multiclass_classification.ipynb) | `ch03_4_iris_multiclass_classification.ipynb` | — |
| ch03_5 | [`ch03_5_heart_training_optimization.ipynb`](notebooks/ch03_5_heart_training_optimization.ipynb) | `ch03_5_heart_training_optimization.ipynb` | 원본에 실행 결과 없음 |

- 머신러닝 과정은 원본 번호 체계(01~03장)가 이미 순서대로여서 번호를 유지했습니다.
- `ch02_6`: 원본의 `Path("../housing.csv")`는 정리본 폴더 구조에서 파일을 찾지 못하므로 노트북과 같은 폴더의 `housing.csv`를 읽도록 바꾸고 코드 위에 `# (변경)` 주석을 달았습니다.

## 4장 자료 (`guide/`)

| 파일 | 원본 파일 |
|---|---|
| `guide/ml_dl_training_setup_guide.md` | `PyTorch 머신러닝·딥러닝 학습 설정 선택 기준.md` |
| `guide/slides/ml_dl_techtree_v01.pptx` | `PyTorch_머신러닝_딥러닝_테크트리_jung.pptx` (15장) |
| `guide/slides/ml_dl_techtree_v02.pptx` | `PyTorch_머신러닝_딥러닝_테크트리_jung_수정.pptx` (16장, Target 자료형·Metric Map 보강) |
| `guide/slides/ml_dl_training_setup_diagram.pptx` | `PyTorch_학습설정_도식화_프레젠테이션.pptx` (15장) |

## 데이터

`notebooks/` 폴더에 `heart.csv`(심장질환, 303행), `housing.csv`(주택가격, 506행), `iris.csv`(붓꽃, 150행)와 `png/`(ch02_1 그래프)를 둡니다. 노트북은 `notebooks/`를 작업 폴더로 실행합니다.
