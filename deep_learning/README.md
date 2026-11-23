# 딥러닝 실습 (deep_learning)

은닉층과 ReLU를 쌓은 심층 신경망(MLP)에서 출발해 MNIST·Fashion-MNIST, CNN, ResNet18 전이학습, 모델 저장·ONNX 배포, 단일 객체 위치 추정(YOLO 연결 1단계)까지 다루는 과정입니다. 학습 설정(출력층·Loss·Optimizer) 선택 원리는 [머신러닝 4장](../machine_learning/dist/ch04_training_setup_guide_v04.html)을 먼저 보면 좋습니다.

- 학습 안내서: [`dist/index.html`](dist/index.html)
- 이전 과정: [머신러닝 기초](../machine_learning/)

## 장 구성

| 장 | 제목 | 내용 | 안내서 |
|---|---|---|---|
| 01 | 심층 신경망 이진분류 | 단일 선형층 로지스틱 분류 → 은닉층·ReLU MLP | [`ch01_dnn_binary_classification_v03.html`](dist/ch01_dnn_binary_classification_v03.html) |
| 02 | MNIST MLP | 숫자 분류 → Optimizer 비교 → 과적합·Dropout → 오류 분석 | [`ch02_mnist_mlp_v03.html`](dist/ch02_mnist_mlp_v03.html) |
| 03 | Fashion-MNIST MLP | 의류 이미지 학습·평가 → 단일 이미지 예측 | [`ch03_fashion_mnist_mlp_v03.html`](dist/ch03_fashion_mnist_mlp_v03.html) |
| 04 | CNN | Fashion-MNIST CNN → 필터·특징맵 → CIFAR-10 기본·심층 CNN | [`ch04_cnn_v03.html`](dist/ch04_cnn_v03.html) |
| 05 | ResNet18·전이학습 | CIFAR-10 ResNet18 → 사전학습 가중치 전이학습 | [`ch05_resnet_transfer_learning_v03.html`](dist/ch05_resnet_transfer_learning_v03.html) |
| 06 | 모델 저장·ONNX | state_dict 저장·복원 → ONNX 내보내기·Runtime 추론 | [`ch06_model_deployment_v03.html`](dist/ch06_model_deployment_v03.html) |
| 07 | CNN→YOLO 위치 추정 | Bounding Box 회귀 → IoU → 함수·main() 구조 | [`ch07_single_object_localization_v03.html`](dist/ch07_single_object_localization_v03.html) |

## 노트북 순번 대응표

| 새 순번 | 노트북 | 원본 파일 | 비고 |
|---|---|---|---|
| ch01_1 | [`ch01_1_heart_disease_dnn_classification.ipynb`](notebooks/ch01_1_heart_disease_dnn_classification.ipynb) | `ch03_2_heart_disease_classification_DNN.ipynb` | 순번·파일명 변경 |
| ch02_1 | [`ch02_1_mnist_mlp_classification.ipynb`](notebooks/ch02_1_mnist_mlp_classification.ipynb) | `ch04_1_mnist_mlp_classification.ipynb` | 순번·파일명 변경 |
| ch02_2 | [`ch02_2_mnist_optimizer_comparison.ipynb`](notebooks/ch02_2_mnist_optimizer_comparison.ipynb) | `ch04_2_mnist_optimizer_comparison.ipynb` | 순번·파일명 변경 |
| ch02_3 | [`ch02_3_mnist_mlp_overfitting_dropout.ipynb`](notebooks/ch02_3_mnist_mlp_overfitting_dropout.ipynb) | `ch04_3_mnist_mlp_overfitting_dropout.ipynb` | 순번·파일명 변경 |
| ch02_4 | [`ch02_4_mnist_prediction_error_analysis.ipynb`](notebooks/ch02_4_mnist_prediction_error_analysis.ipynb) | `ch04_4_mnist_prediction_error_analysis.ipynb` | 순번·파일명 변경 |
| ch03_1 | [`ch03_1_fashion_mnist_mlp_training_evaluation.ipynb`](notebooks/ch03_1_fashion_mnist_mlp_training_evaluation.ipynb) | `ch04_5_fashion_mnist_mlp_training_evaluation.ipynb` | 순번·파일명 변경, 실행 결과의 로컬 경로 가림 |
| ch03_2 | [`ch03_2_fashion_mnist_simple_prediction.ipynb`](notebooks/ch03_2_fashion_mnist_simple_prediction.ipynb) | `ch04_6_fashion_mnist_simple_prediction.ipynb` | 순번·파일명 변경, 원본 기록에 FileNotFoundError |
| ch04_1 | [`ch04_1_fashion_mnist_cnn_training_evaluation.ipynb`](notebooks/ch04_1_fashion_mnist_cnn_training_evaluation.ipynb) | `ch05_1_fashion_mnist_cnn_training_evaluation.ipynb` | 순번·파일명 변경, 실행 결과의 로컬 경로 가림 |
| ch04_2 | [`ch04_2_cnn_filter_feature_map_visualization.ipynb`](notebooks/ch04_2_cnn_filter_feature_map_visualization.ipynb) | `ch05_2_cnn_filter_feature_map_visualization.ipynb` | 순번·파일명 변경, 실행 결과의 로컬 경로 가림 |
| ch04_3 | [`ch04_3_cifar10_basic_cnn_training_evaluation.ipynb`](notebooks/ch04_3_cifar10_basic_cnn_training_evaluation.ipynb) | `ch05_3_cifar10_basic_cnn_training_evaluation.ipynb` | 순번·파일명 변경 |
| ch04_4 | [`ch04_4_cifar10_deep_cnn_improvement_comparison.ipynb`](notebooks/ch04_4_cifar10_deep_cnn_improvement_comparison.ipynb) | `ch05_4_cifar10_deep_cnn_improvement_comparison.ipynb` | 순번·파일명 변경 |
| ch05_1 | [`ch05_1_cifar10_resnet18_training_evaluation.ipynb`](notebooks/ch05_1_cifar10_resnet18_training_evaluation.ipynb) | `ch05_5_CIFAR10_ResNet18_Training_Evaluation.ipynb` | 순번·파일명 변경, 실행 결과의 로컬 경로 가림 |
| ch05_2 | [`ch05_2_resnet18_transfer_learning.ipynb`](notebooks/ch05_2_resnet18_transfer_learning.ipynb) | `ch05_6_ResNet18_Transfer_Learning.ipynb` | 순번·파일명 변경, 실행 결과의 로컬 경로 가림 |
| ch06_1 | [`ch06_1_model_save_load_inference.ipynb`](notebooks/ch06_1_model_save_load_inference.ipynb) | `ch06_1_PyTorch_Model_Save_Load_Inference.ipynb` | 순번·파일명 변경, 실행 결과의 로컬 경로 가림 |
| ch06_2 | [`ch06_2_onnx_export_runtime_inference.ipynb`](notebooks/ch06_2_onnx_export_runtime_inference.ipynb) | `ch06_2_PyTorch_ONNX_Export_Runtime_Inference.ipynb` | 순번·파일명 변경, 실행 결과의 로컬 경로 가림 |
| ch07_1 | [`ch07_1_cnn_to_yolo_single_object_localization.ipynb`](notebooks/ch07_1_cnn_to_yolo_single_object_localization.ipynb) | `ch07_1_cnn_to_yolo_single_object_localization.ipynb` | 제목에 번호 추가 |
| ch07_2 | [`ch07_2_cnn_to_yolo_single_object_localization_main.ipynb`](notebooks/ch07_2_cnn_to_yolo_single_object_localization_main.ipynb) | `ch07_2_cnn_to_yolo_single_object_localization.ipynb` | 순번·파일명 변경, 제목에 번호 추가 |

- 순번을 바꾸면서 노트북 제목과 **모델 저장·불러오기 파일 이름**의 번호도 함께 바꿨습니다. 예: `ch04_3_best_mnist_mlp` → `ch02_3_best_mnist_mlp`, `ch05_6_best_resnet18_transfer_learning` → `ch05_2_best_resnet18_transfer_learning`.
- 실행 결과(출력 기록) 안에 찍힌 저장 경로는 원본 실행 당시의 옛 번호로 남아 있습니다. 다시 실행하면 새 번호로 저장됩니다.
- 노트북 사이 의존 관계: `ch02_4` ← `ch02_3`, `ch03_2` ← `ch03_1`, `ch04_2` ← `ch04_1`, `ch04_4` ← `ch04_3`, `ch06_1` ← `ch05_2` (앞 노트북이 저장한 모델 사용).

## 데이터

`notebooks/heart.csv`(01장), `notebooks/png/dog.jpg`(06_2 예제 이미지). MNIST·Fashion-MNIST·CIFAR-10은 `torchvision.datasets`가 실행 중 `data/`에 내려받습니다.
