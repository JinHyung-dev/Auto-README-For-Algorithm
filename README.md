# Auto-README-For-Algorithm
Automatically write README.md for Algorithm study
<br><br>

## 📔 목차
1. [개요](https://github.com/JinHyung-dev/Auto-README-For-Algorithm/edit/main/README.md#-%EA%B0%9C%EC%9A%94)
    1) [소개](https://github.com/JinHyung-dev/Auto-README-For-Algorithm/edit/main/README.md#%EC%86%8C%EA%B0%9C)
    2) [프로젝트 배경](https://github.com/JinHyung-dev/Auto-README-For-Algorithm/edit/main/README.md#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%B0%B0%EA%B2%BD)
    3) [라이센스](https://github.com/JinHyung-dev/Auto-README-For-Algorithm/edit/main/README.md#%EB%9D%BC%EC%9D%B4%EC%84%BC%EC%8A%A4)
2. [작동 예시](https://github.com/JinHyung-dev/Auto-README-For-Algorithm/edit/main/README.md#-%EC%9E%91%EB%8F%99-%EC%98%88%EC%8B%9C)
3. [사용 방법](https://github.com/JinHyung-dev/Auto-README-For-Algorithm/edit/main/README.md#-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95%ED%83%9D-1)
    1) [템플릿으로 생성](https://github.com/JinHyung-dev/Auto-README-For-Algorithm/edit/main/README.md#1-%ED%85%9C%ED%94%8C%EB%A6%BF%EC%9C%BC%EB%A1%9C-%EC%8B%A0%EA%B7%9C-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EC%83%9D%EC%84%B1%ED%95%98%EC%97%AC-%EC%9D%B4%EC%9A%A9%ED%95%98%EA%B8%B0)
    2) [기존 레포에 적용](https://github.com/JinHyung-dev/Auto-README-For-Algorithm/edit/main/README.md#2-%EA%B8%B0%EC%A1%B4-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC%EC%97%90-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0)
4. [커스텀](https://github.com/JinHyung-dev/Auto-README-For-Algorithm/edit/main/README.md#-%EC%BB%A4%EC%8A%A4%ED%85%80)
<br><br>

## 📌 개요
### 소개
GitHub Actions와 Python을 사용하여 알고리즘 문제 풀이의 README.md 파일을 자동으로 업데이트하는 도구입니다. 문제의 풀이일, 사이트, 난이도, 링크 등 정보를 자동으로 추가해 주는 GitHub 템플릿 레포지토리 입니다.

### 제작 배경
이 템플릿 레포지토리는 개인적으로 [백준 자동 푸시 익스텐션](https://github.com/BaekjoonHub/BaekjoonHub)(Auto Git Push for BOJ) 사용 중 풀이한 문제 목록이 README.md에 자동으로 정리되었으면 좋겠다는 마음으로 만들게 되었습니다.
[GitHub Actions 자동화](https://kimgabe.github.io/personal_study/git/githubaction_auto_readme/) 블로그에서 소개된 아이디어를 바탕으로 **알고리즘 문제 풀이 레포지토리의 구조에 맞춰 파싱**하고 **중복된 문제를 건너뛰는 기능**과 **한국 시간 기준 커밋 시간 반영** 등을 추가하여 사용자가 더 편리하게 사용할 수 있도록 개선했습니다.

### 라이센스
이 템플릿 레포지토리는 **MIT License** 하에 공개됩니다. 아래 내용을 참고하여 사용해 주세요.
- This project is developed by [JinHyung-dev](https://github.com/JinHyung-dev).
- You can freely use and modify this project under the terms of the [MIT License](https://github.com/JinHyung-dev/Auto-README-For-Algorithm/blob/main/LICENSE).

<br><br>

## 💬 작동 예시
* 파일 구조 :
  ```
  백준
  └── Bronze
      └── 10817. 세 수
          ├── README.md
          └── 세 수.java
  ```
* README.md에 작성되는 내용 :
  | 사이트 | 난이도 | 문제 | 풀이일(커밋 일시) | 링크(최하위 폴더 내 README.md로 연결) |
  | --- | --- | --- | --- | --- |
  | 백준 | Bronze | 10817. 세 수 | 2024-11-02 13:04 | [링크](https://github.com/JinHyung-dev/Algorithm/blob/main/백준/Bronze/10817. 세 수/README.md) |
👉 예시 [Repository](https://github.com/JinHyung-dev/Algorithm/blob/main/README.md) 보러 가기
<br><br>

## ✅ 사용 방법(택 1)
### 1) 템플릿으로 신규 레포지토리 생성하여 이용하기
1. 오른쪽 상단의 "Use this template" 버튼을 클릭하여 새로운 레포지토리를 생성
  - 프로젝트 이름과 설명을 입력한 후, "Create repository from template" 버튼을 클릭
2. 작동 테스트
  - 임의의 파일을 추가해보기 (ex. sample/test1/test2/test3.txt)
  - 자동 리드미 작동이 성공했다면 통과!
3. 백준 자동 푸시 익스텐션 설정시 해당 레포지토리를 선택
<br>

### 2) 기존 레포지토리에 적용하기
> "## 📑List📑" 섹션 이후 내용만 찾아서 변경되도록 설정되어있으므로 기존에 작성되어있는 README.md 내용은 변경되지 않습니다.

> 풀이사이트-난이도-문제명 순이어야 그대로 사용 가능합니다. 그외 커스텀 내용 참조
1. 자동 README를 적용할 레포지토리의 GitAction 활성화
  - 레포지토리 - Settings - Actions(General) 메뉴로 이동
  - Actions permissions 항목을 **Allow all actions and reusable workflows**로 체크
  - Workflow permissions 항목을 **Read and write permissions**로 체크
  - 변경사항 저장
2. 3가지 파일 다운로드
  - `.github/workflows/update-readme.yml`
  - `requirements.txt`
  - `update_readme.py`
3. GitAction 설정 파일 업로드
  - 레포지토리 내 `.github/workflows/update-readme.yml`를 추가
4. README.md 작성 설정 파일 업로드
  - 레포지토리 최상단에 `requirements.txt`, `update_readme.py` 파일을 추가
5. 작동 테스트
  - 임의의 파일을 추가해보기 (ex. sample/test1/test2/test3.txt)
  - 자동 리드미 작동이 성공했다면 통과입니다!
<br>

## 📍 커스텀
필요시 `update_readme.py` 파일을 수정하여 README에 작성할 내용을 프로젝트에 맞게 변경하여 사용하세요.
- README.md에 작성될 제목 및 첫 행 내용 변경 원할시 아래 부분을 수정
    ```
    # 새로운 테이블 생성
    new_table = "## 📑List📑\n\n"
    new_table += "| 사이트 | 난이도 | 문제 | 풀이일 | 링크 |\n"
    ```
- 링크는 해당 최하단 폴더 내 README.md 파일로 연결되도록 설정되어 있습니다. 변경 원할시 아래 부분을 수정
    ```
    # README.md 링크만 추출
    if "README.md" in item['path']:
        links.append(f"https://github.com/{user_repo}/blob/main/{item['path']}")
    else:
        links.append(f"https://github.com/{user_repo}/blob/main/{item['path']}")  # 다른 파일이 있다면 그대로 추가
    ```
