# 머신러닝·딥러닝 이론 (theory)

강의 2~5강 슬라이드와 학습 설정 테크트리를 기존 실습 과정과 엮어, 선형회귀에서 CNN까지 **학습이 왜 그렇게 동작하는지**를 수식·그림·검증 코드로 설명하는 이론 교재입니다. 장마다 끝에서 실습 과정의 해당 장으로 이어집니다.

- 학습 안내서: [`dist/index.html`](dist/index.html)
- 실습 과정: [머신러닝 기초](../machine_learning/) · [딥러닝 실습](../deep_learning/)

## 장 구성

| 장 | 제목 | 내용 | 원본 자료 | 안내서 | 이어지는 실습 |
|---|---|---|---|---|---|
| 01 | 선형회귀 | 가설·손실함수 → 경사하강법 → 여러 입력과 행렬 표현 | 강의 2강 | [`ch01_linear_regression_v01.html`](dist/ch01_linear_regression_v01.html) | 머신러닝 02장 |
| 02 | 분류 | 시그모이드·BCE → 소프트맥스·크로스엔트로피 → 다중분류 | 강의 3강 | [`ch02_classification_v01.html`](dist/ch02_classification_v01.html) | 머신러닝 03장, 딥러닝 01장 |
| 03 | 다층 퍼셉트론(MLP) | 은닉층·활성화 → 데이터 분리·배치 → 학습 루프·역전파 → 평가 | 강의 4강 | [`ch03_mlp_v01.html`](dist/ch03_mlp_v01.html) | 딥러닝 02·03장 |
| 04 | 합성곱 신경망(CNN) | 합성곱·패딩·스트라이드·풀링 → 채널 → 2단 CNN Shape 추적 | 강의 5강 | [`ch04_cnn_v01.html`](dist/ch04_cnn_v01.html) | 딥러닝 04·05장 |
| 05 | 학습 설정 선택 기준 | Target 형태 → 출력층 → Loss → Optimizer → Validation → Metric | 테크트리 수정본 | [`ch05_training_setup_v01.html`](dist/ch05_training_setup_v01.html) | 머신러닝 04장 |

각 장은 같은 순서로 읽습니다: 이 장의 목표 → 개념과 슬라이드 → 수식 유도 → 코드로 확인하기 → PyTorch로 옮기기 → 강의 자료 바로잡기 → 스스로 점검 → 실습으로 이어가기.

## 폴더 구조

```text
theory/
├── README.md              ← 지금 이 파일
├── course.json            ← 과정 제목·장 목록·버전·INDEX 안내 문구
├── content/chNN.md        ← 장별 원고
├── code/chNN_*.py         ← 장별 검증 코드 (Python 3 + NumPy)
├── assets/ · build.py     ← rule_md 공통 디자인·생성기 사본 (이론 과정용 보완은 (변경)·(추가) 주석)
└── dist/                  ← 생성된 HTML (index.html, chNN_주제_v01.html, img/chNN_slideMM.jpg)
```

- 슬라이드 그림 `img/chNN_slideMM.jpg`의 `MM`은 원본 강의 PDF의 쪽 번호입니다. 강의 PDF를 192dpi(2560×1440)로 다시 렌더링한 것으로, 모양과 색은 원본 그대로입니다.
- 수식은 그림이 아니라 `content/*.md`의 LaTeX를 빌드할 때 MathML로 바꿔 표시합니다.

## 다시 만들기

```bash
python -m pip install mistune latex2mathml
cd theory
python build.py                      # dist/ 생성, 수식 변환 실패 개수 출력
python code/ch01_linear_regression.py  # 장별 검증 코드 실행 (NumPy 필요)
```

## 강의 자료에서 바로잡은 내용

슬라이드를 적대적으로 검증해 찾은 오류는 본문에서 고친 내용으로 설명하고, 장마다 마지막 부분의 **강의 자료 바로잡기** 표에 원본 표기·바로잡은 내용·근거를 남겼습니다. 주요 항목은 다음과 같습니다.

| 장 | 위치 | 바로잡은 내용 |
|---|---|---|
| 01 | 2강 23쪽 | 선형회귀 MSE는 볼록 함수라 최솟값이 하나뿐 (시작점 의존은 신경망의 이야기) |
| 02 | 3강 25·26·31쪽 | 소프트맥스 확률 0.7/0.2/0.1은 반올림 값 (정확히 0.659/0.242/0.099), 손실도 다시 계산 |
| 03 | 4강 4쪽 | `nn.Linear(1, 8), nn.Linear(8, 1)` 사이에 활성화 함수가 없으면 선형 모델과 같음 → `nn.ReLU()` 필요 |
| 03 | 4강 22쪽 | `display_logits`와 `logits` 변수 이름 불일치 (`NameError`) |
| 03 | 4강 9쪽 | 85/15% 분리는 예시, 실습은 55,000/5,000장 |
| 04 | 5강 14·15쪽 | 세로 필터 ReLU 결과 한 칸 오류 (−1 → 0이어야 함) |
| 04 | 5강 19쪽 | PyTorch 인자는 `strides`가 아니라 `stride` |
| 04 | 5강 18쪽 | 필터 개수 = 출력 채널 수, 필터 한 개의 깊이 = 입력 채널 수 |

## 검증 상태

| 항목 | 판정 | 근거 |
|---|---|---|
| 본문 NumPy 코드와 실행 결과 일치 | 통과 | 본문의 `실행 통과` 코드 박스 6개를 그대로 실행해 바로 아래 결과 상자와 글자 단위로 비교 (Python 3.13, NumPy 2.5) |
| 장별 검증 코드 `code/*.py` | 통과 | 5개 파일 실행, 슬라이드 수치(비용 14/3, 합성곱 15·16·6·15, 패딩 결과, 파라미터 101,770·9,098 등)와 일치 |
| PyTorch 예시 코드 | 미검증 | 문법 검사만 통과. 이 정리 환경에 PyTorch가 없어 실행하지 않음 |
| HTML 생성·수식 변환 | 통과 | `build.py` 실행, HTML 6개 생성, 수식 변환 실패 0개 |
| 남은 표기·링크·그림 | 통과 | 본문에 남은 `$`·LaTeX·상자 표식 0건, 내부 링크 깨짐 0건, 참조 없는 그림·없는 그림 0건 |
| 화면 폭 1280·390px 가로 넘침, 스크립트 오류 | 통과 | Chromium(Playwright) 점검 |
| GitHub Pages 실제 배포 | 미검증 | 푸시 후 접속 확인 필요: https://yuul-jung.github.io/ml_dl_pytorch/theory/dist/index.html |
