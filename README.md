# Auto-README-For-Algorithm

## 📌 개요
* [백준 자동 푸시 익스텐션](https://github.com/BaekjoonHub/BaekjoonHub)(Auto Git Push for BOJ) 사용중에 풀이한 문제들도 README.md에 자동으로 정리되었으면 좋겠다는 마음으로 만들게 되었습니다.
* 이 레포지토리는 GitHub 템플릿 레포지토리로 설정되어 있습니다.
* GitAction을 활용하여 해당 레포지토리에 push되었을 때, 레포지토리 내 **폴더 구조**를 확인하고 각 경로를 파싱하여 자동으로 표를 생성하여 README.md에 리스트업 해줍니다.

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

## ✅ 사용 방법(택 1)
### 1) 템플릿으로 신규 레포지토리 생성하여 이용하기
1. 오른쪽 상단의 "Use this template" 버튼을 클릭하여 새로운 레포지토리를 생성
  - 프로젝트 이름과 설명을 입력한 후, "Create repository from template" 버튼을 클릭
2. 작동 테스트
  - 임의의 파일을 추가해보기 (ex. sample/test1/test2/test3.txt)
  - 자동 리드미 작동이 성공했다면 통과입니다!

### 2) 기존 레포지토리에 적용하기
> "## 📑List📑" 섹션 이후 내용만 찾아서 변경되도록 설정되어있으므로 기존에 작성되어있는 README,md 내용은 변경되지 않습니다.
1. 자동 README를 적용할 레포지토리의 GitAction 활성화
  - 레포지토리 - Settings - Actions(General) 메뉴로 이동
  - Actions permissions 항목을 **Allow all actions and reusable workflows**로 체크
  - Workflow permissions 항목을 **Read and write permissions**로 체크
  - 변경사항 저장!
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

### 커스텀
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
