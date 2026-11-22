# ML_DL_pytorch — PyTorch 머신러닝·딥러닝 학습 자료

PyTorch(파이토치, 딥러닝 프레임워크) 실습 노트북을 **머신러닝**과 **딥러닝** 두 과정으로 나누고, 과정마다 장·절 순번을 새로 매겨 정리한 교재 저장소입니다. 각 과정은 Jupyter 노트북과 함께 [Yuul-Jung 교육용 HTML 표준](https://github.com/Yuul-Jung/rule_md/tree/main/web/education-html)에 맞춘 학습 안내서(HTML)를 제공합니다.

## 과정 구성

| 과정 | 폴더 | 장 구성 | 학습 안내서 |
|---|---|---|---|
| 머신러닝 기초 | [`machine_learning/`](machine_learning/) | 01 Tensor 기초 → 02 선형회귀 → 03 로지스틱·Softmax 분류 → 04 학습 설정 선택 기준 | [`machine_learning/dist/index.html`](machine_learning/dist/index.html) |
| 딥러닝 실습 | [`deep_learning/`](deep_learning/) | 01 심층 신경망 이진분류 → 02 MNIST MLP → 03 Fashion-MNIST MLP → 04 CNN → 05 ResNet18·전이학습 → 06 모델 저장·ONNX → 07 CNN→YOLO 위치 추정 | [`deep_learning/dist/index.html`](deep_learning/dist/index.html) |

**나누는 기준:** 은닉층 없이 선형 모델 하나로 푸는 회귀·분류(로지스틱·Softmax)와 그 기초(Tensor)는 머신러닝 과정에, 은닉층과 비선형 활성화 함수를 쌓는 MLP·CNN·ResNet과 그 배포·응용은 딥러닝 과정에 둡니다. 같은 심장질환 데이터도 단일 선형층 모델은 머신러닝 3장, MLP 모델은 딥러닝 1장으로 나뉩니다. 두 과정에 공통으로 쓰는 **학습 설정 선택 기준**(Target 형태 → 출력층 → Loss → Optimizer → Metric)은 머신러닝 4장에 두고 딥러닝 과정에서 참조합니다.

권장 학습 순서는 머신러닝 01 → 04, 이어서 딥러닝 01 → 07입니다.

## 폴더 구조

```text
ML_DL_pytorch/
├── README.md                  ← 지금 이 파일
├── AGENTS.md                  ← AI 코딩 에이전트 작업 규칙 (rule_md 참조)
├── machine_learning/
│   ├── README.md              ← 과정 안내, 새 순번 ↔ 원본 파일 대응표
│   ├── notebooks/             ← chNN_K_주제.ipynb, heart.csv, housing.csv, iris.csv, png/
│   ├── guide/                 ← 학습 설정 선택 기준 원본 문서, slides/ 발표 자료(PPTX)
│   ├── course.json            ← 과정 제목·장 목록·버전
│   ├── content/chNN.md        ← 장별 학습 안내서 원고
│   ├── assets/ · build.py     ← rule_md 공통 디자인·생성기 사본
│   └── dist/                  ← 생성된 HTML (index.html, chNN_주제_v03.html, img/)
└── deep_learning/
    ├── README.md
    ├── notebooks/             ← chNN_K_주제.ipynb, heart.csv, png/dog.jpg
    ├── course.json · content/ · assets/ · build.py
    └── dist/
```

## 순번 규칙

- 노트북: `chNN_K_주제.ipynb` — `NN`은 과정 안의 장 번호, `K`는 장 안의 실습 순번입니다. 두 과정은 각각 01장부터 시작합니다.
- 학습 안내서: `chNN_주제_vNN.html` (현재 v03, 내용을 고치면 STANDARD 6절에 따라 버전을 올림) — 장 하나가 HTML 한 페이지이며, 장 안의 노트북은 `chNN_K` 절로 들어갑니다.
- 딥러닝 노트북은 원본 번호(`ch03_2_..._DNN`, `ch04_1` ~ `ch07_2`)에서 새 번호로 바뀌었습니다. 노트북 제목과 **모델 저장·불러오기 파일 이름**(예: `ch04_5_best_fashion_mnist_mlp` → `ch03_1_best_fashion_mnist_mlp`)도 같은 번호로 함께 바꿔, 앞 노트북이 저장한 모델을 뒤 노트북이 그대로 찾을 수 있습니다. 전체 대응표는 각 과정 README에 있습니다.

## 실행 방법

```bash
# 1) 가상환경 생성과 활성화
python3 -m venv .venv
source .venv/bin/activate

# 2) 노트북 실행에 필요한 패키지 설치 (ONNX 실습은 onnx, onnxruntime 추가)
python -m pip install torch torchvision numpy pandas scikit-learn matplotlib jupyter
python -m pip install onnx onnxruntime

# 3) 과정 폴더의 notebooks/ 를 작업 폴더로 열어 순서대로 실행
cd deep_learning/notebooks
jupyter notebook
```

- CSV 데이터는 노트북과 같은 폴더에 있으므로 `notebooks/`를 작업 폴더로 실행합니다. Google Colab에서는 CSV 파일을 업로드한 뒤 실행합니다(대부분의 노트북에 업로드 코드가 들어 있습니다).
- MNIST·Fashion-MNIST·CIFAR-10은 `torchvision.datasets`가 `data/`에 자동으로 내려받고, 학습한 모델은 `models/`에 저장됩니다. 두 폴더는 `.gitignore`로 저장소에서 제외합니다.
- 딥러닝 2장 이후는 GPU 실행을 권장합니다.

## 학습 안내서(HTML) 다시 만들기

```bash
# 원고(content/*.md)나 course.json을 고친 뒤 과정 폴더에서 생성
python -m pip install mistune latex2mathml   # 수식은 빌드 때 MathML로 변환
cd machine_learning
python build.py        # dist/index.html, dist/chNN_*_v03.html 생성
```

GitHub Pages는 **main 브랜치 루트**로 게시합니다.

- 머신러닝: https://yuul-jung.github.io/ml_dl_pytorch/machine_learning/dist/index.html
- 딥러닝: https://yuul-jung.github.io/ml_dl_pytorch/deep_learning/dist/index.html

## 📘 교육용 HTML 공통 제작 규칙

이 저장소의 교육자료(웹페이지·강의 HTML)는 [Yuul-Jung 교육용 HTML 공통 표준](https://github.com/Yuul-Jung/rule_md/tree/main/web/education-html)을 적용합니다.

- [제작 규칙](https://github.com/Yuul-Jung/rule_md/blob/main/web/education-html/STANDARD.md)
- [다른 저장소 적용 안내](https://github.com/Yuul-Jung/rule_md/blob/main/web/education-html/INTEGRATION.md)
- [기준 디자인 사례](https://github.com/Yuul-Jung/ai-agent-engineering)

공통 책장 이미지, 컴팩트한 상단 배너, 좌측 전체 장/절 탐색, 모바일 메뉴, 파일 버전 및 검증 기준을 따릅니다. 적용 기준 커밋: [`rule_md@028248a`](https://github.com/Yuul-Jung/rule_md/commit/028248a19afc66e9aafdab393fbe0de10a3930ca) (2026-11-23, 좌측 탐색 4.1·보조 장 규칙).

이 저장소에서 공통 템플릿에 더한 부분(각 과정의 `build.py`·`assets/site.css`에 `(추가)` 주석으로 표시):

- 코드 박스 제목 줄에 **언어 · 파일명 · 코드 셀 번호 · 검증 상태** 표시 ([공통 코드 규칙](https://github.com/Yuul-Jung/rule_md/blob/main/common/code-style-rules.md) 10절)
- 실행 결과는 코드 박스와 구분되는 `OUTPUT` 상자로 표시하고 복사 버튼을 두지 않음
- 장마다 `전체 실습 흐름`에 개념 흐름도(단계 상자 + ↓)를 두고, 단계 이름은 실제 코드의 함수·클래스 이름을 사용
- 노트북 그림 폭 제한, 좁은 화면에서 긴 파일명 줄바꿈·넓은 표 가로 스크롤
- 수식(`$...$`, `$$...$$`, `\[...\]`)은 빌드할 때 `latex2mathml`로 MathML로 바꿔 브라우저가 수식으로 표시 (JavaScript·외부 수식 라이브러리 불필요)
- 한글 조사 바로 앞에서 닫히지 않는 굵은 글씨(`**무엇인가?**에`)를 굵게 표시되도록 보정
- 코드 박스마다 바로 아래에 **코드 풀이** 상자(그 코드가 하는 일, 처음 보는 함수·인자의 뜻)를 두고, 장 첫 절에 **쉽게 이해하기**·**꼭 기억할 점** 상자를 둠

## 검증 상태

| 항목 | 판정 | 근거 |
|---|---|---|
| 노트북 실행 결과 | 원본 기록 | 페이지의 실행 결과·그림은 원본 노트북에 저장된 기록입니다. 이번 정리에서 노트북을 다시 실행하지 않았습니다(재실행 **미검증**). |
| 원본에 실행 결과가 없는 노트북 | 미검증 | 머신러닝 `ch01_1`~`ch01_3`, `ch03_5` |
| 원본 실행 기록의 오류 | 실패 | 딥러닝 `ch03_2` 원본 기록에 `FileNotFoundError`(앞 노트북의 모델 파일 없이 실행). `ch03_1`을 먼저 실행하면 해결되는 순서 문제로, 코드는 바꾸지 않았습니다. |
| 순번 변경 후 모델 파일 이름 대응 | 통과 | 딥러닝 노트북 13건의 저장·불러오기 이름이 같은 번호를 가리키는지 스크립트로 확인 |
| 코드 풀이 | 통과 | 코드 셀 553개 중 534개에 풀이를 붙임. 딥러닝 `ch07_1`은 원저자의 풀이 문단이 코드마다 이미 있어 그대로 둠 |
| 원본 소제목 바로잡기 | 통과 | 딥러닝 노트북 12개에서 코드 내용과 맞지 않던 소제목(예: 정확도 계산 코드 위의 `모델 구성`)을 내용에 맞게 고침. 코드·순서는 그대로 |
| HTML 생성 | 통과 | 두 과정 `build.py` 실행, HTML 13개 생성, 수식 변환 실패 0개 |
| Markdown 깨짐 검사 | 통과 | 전체 13쪽 본문에서 코드·수식 밖에 남은 `$`, LaTeX 명령, `**`, 원시 태그, 표 구분선, 코드 울타리, 이미지 문법이 0건 (Chromium 자동 검사) |
| 화면 폭 1366·390px 가로 넘침, 이미지 깨짐 | 통과 | Chromium(Playwright)로 전체 페이지 점검. 넓은 표는 표 안에서 가로 스크롤 |
| 개인정보·로컬 경로 노출 | 통과 | 실행 결과의 로컬 사용자 경로를 `~`로 가림, 이메일·토큰 검색 결과 없음 |
| GitHub Pages 실제 배포 | 통과 | [머신러닝](https://yuul-jung.github.io/ml_dl_pytorch/machine_learning/dist/index.html) · [딥러닝](https://yuul-jung.github.io/ml_dl_pytorch/deep_learning/dist/index.html) 접속 확인 |
