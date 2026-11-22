# GitHub 교육용 HTML 작성 규칙

이 저장소에서 새 HTML 교재를 만들거나 기존 교재를 수정할 때는 먼저 다음 문서를 확인한다.
- https://github.com/Yuul-Jung/rule_md/blob/main/AGENTS.md
- https://github.com/Yuul-Jung/rule_md/blob/main/web/education-html/STANDARD.md
- https://github.com/Yuul-Jung/rule_md/blob/main/web/education-html/INTEGRATION.md
- https://github.com/Yuul-Jung/rule_md/blob/main/common/code-style-rules.md

적용 사항:
1. 책장 배너 이미지는 중앙 표준의 hero-bookshelf.jpg와 동일하게 유지한다.
2. 좌측 전체 장 목차와 현재 페이지 절 목차 및 모바일 메뉴를 구현한다.
3. 기존 학습 내용·코드·이미지는 보존하고, 차이가 있는 부분만 수정한다.
4. 수정 시 장별 파일명을 _v01 → _v02로 올리고 이전 생성본은 결과 폴더에서 정리한다.
5. 코드 문법, 내부 링크, 개인정보, 접근성과 브라우저 표시를 검증한다.
6. 확인하지 못한 실행 결과는 미검증으로 표기한다.
7. 원격 문서를 읽을 수 없으면 추정 적용하지 않고 로컬 규칙 사본을 요구한다.

이 저장소 전용 사항:
- 과정은 `machine_learning/`(선형 모델·기초)과 `deep_learning/`(은닉층 신경망과 응용) 두 폴더로 나눈다.
- 노트북 이름은 `chNN_K_주제.ipynb`, 과정마다 01장부터 번호를 매긴다. 번호를 바꾸면 노트북 제목과 모델 저장·불러오기 파일 이름의 번호도 함께 바꾼다.
- HTML은 각 과정 폴더의 `course.json` + `content/chNN.md`를 고친 뒤 `python build.py`로 `dist/`에 생성한다.
