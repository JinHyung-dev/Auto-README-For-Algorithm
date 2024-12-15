# Auto-README-For-Algorithm
Automatically write README.md for Algorithm study
<br><br>

## 📔 목차
1. [개요](#-개요)
    1) [소개](#소개)
    2) [프로젝트 배경](#제작-배경)
    3) [라이센스](#라이센스)
2. [작동 예시](#-작동-예시)
3. [사용 전 체크리스트](#-사용-전-체크리스트)
4. [사용 방법](#-사용-방법택-1)
    1) [템플릿으로 생성](#1-템플릿으로-신규-레포지토리-생성하여-이용하기)
    2) [기존 레포에 적용](#2-기존-레포지토리에-적용하기)
5. [커스텀](#-커스텀)
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

## 👉 사용 전 체크리스트
1. Private 레포지토리로 사용하실 건가요?
 - 네: GITHUB_TOKEN 환경 변수가 필요합니다. 깃 허브 토큰을 생성한 적이 없으면 "PermissionError: Private 레포지토리에서 실행하려면 GITHUB_TOKEN이 필요합니다."라는 에러 메시지가 뜹니다. 이 경우 Public 레포지토리로 사용하거나 GITHUB_TOKEN을 설정하세요.
 - 아니요: 토큰이 없어도 정상 작동합니다. Public 레포지토리에서는 추가 설정 없이 바로 사용할 수 있습니다.
2. GITHUB_TOKEN 설정 방법
 - GitHub Settings > Developer settings > Personal access tokens에서 토큰을 생성하세요.
<br><br>

## ✅ 사용 방법(택 1)
### 1) 템플릿으로 신규 레포지토리 생성하여 이용하기
1. 오른쪽 상단의 "Use this template" 버튼을 클릭하여 새로운 레포지토리를 생성
  - 프로젝트 이름과 설명을 입력한 후, "Create repository from template" 버튼을 클릭
2. 해당 레포지토리의 GitAction 활성화
  - 레포지토리 - Settings - Actions(General) 메뉴로 이동
  - Actions permissions 항목을 **Allow all actions and reusable workflows**로 변경
  - Workflow permissions 항목을 **Read and write permissions**로 체크되어있는지 확인
  - 변경사항 저장
3. 작동 테스트
  - 임의의 파일을 추가해보기 (ex. sample/test1/test2/test3.txt)
  - 자동 리드미 작동이 성공했다면 통과!
4. 백준 자동 푸시 익스텐션 설정시 해당 레포지토리를 선택
<br>

### 2) 기존 레포지토리에 적용하기
> "## 📑List📑" 섹션 이후 내용만 찾아서 변경되도록 설정되어있으므로 기존에 작성되어있는 README.md 내용은 변경되지 않습니다.

> 🚨 레포지토리 폴더 구조가 풀이사이트-난이도-문제명 순이어야 그대로 사용 가능합니다. 그외 커스텀 내용 참조하여 수정해야할 수 있습니다.
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
