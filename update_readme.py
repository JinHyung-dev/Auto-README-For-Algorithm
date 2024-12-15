import os
from datetime import datetime
import pytz
import requests

# 한국 시간대 설정
KST = pytz.timezone('Asia/Seoul')

# 날짜와 시간 포맷을 'YYYY-MM-DD HH:mm' 형식으로 변환
def get_kst_time(commit_time):
    # 커밋 시간을 한국 시간대로 변환
    utc_time = datetime.strptime(commit_time, "%Y-%m-%dT%H:%M:%SZ")
    kst_time = utc_time.replace(tzinfo=pytz.utc).astimezone(KST)
    return kst_time.strftime('%Y-%m-%d %H:%M')

# GitHub API 응답에서 파일 목록을 처리하는 코드
def get_data(user_repo):
    token = os.getenv('GITHUB_TOKEN')  # GITHUB_TOKEN 환경 변수에서 토큰을 가져옵니다.
    headers = {}
    
    # private 레포일 때만 Authorization 헤더 추가
    if token:
        headers = {'Authorization': f'token {token}'}
    else:
        print("Warning: GITHUB_TOKEN이 설정되지 않았습니다. Public 레포지토리에서만 작동합니다.")
        if not is_public_repo(user_repo):
            raise PermissionError("Private 레포지토리에서 실행하려면 GITHUB_TOKEN이 필요합니다.")
    
    # GitHub API를 사용하여 파일 목록 가져오기
    url = f"https://api.github.com/repos/{user_repo}/git/trees/main?recursive=1"
    response = requests.get(url, headers=headers)
    response_data = [item for item in response.json().get('tree', []) if item['type'] == 'blob' and not item['path'].startswith('.')]

    sites = []
    difficulties = []
    problems = []
    commit_times = []
    links = []

    seen_problems = set()  # 이미 본 문제를 추적할 set

    # 파일 경로에서 사이트, 난이도, 문제번호/이름 추출
    for item in response_data:
        path_parts = item['path'].split('/')
        if len(path_parts) >= 3:
            site = path_parts[0]
            difficulty = path_parts[1]
            problem = path_parts[2]  # 문제 이름 전체(확장자 포함) 가져오기
            # 이미 본 문제는 건너뜀
            problem_key = (site, difficulty, problem)
            if problem_key in seen_problems:
                continue  # 중복된 문제는 추가하지 않음
            seen_problems.add(problem_key)
            
            sites.append(site)
            difficulties.append(difficulty)
            problems.append(problem)

            # 각 파일의 마지막 커밋 시간 가져오기
            file_url = f"https://api.github.com/repos/{user_repo}/commits?path={item['path']}"
            commit_response = requests.get(file_url, headers=headers)
            commit_data = commit_response.json()

            if commit_data:
                commit_time = commit_data[0].get('commit', {}).get('committer', {}).get('date', None)
                if commit_time:
                    commit_times.append(get_kst_time(commit_time))
                else:
                    # 커밋 시간 정보가 없는 경우, 기본 시간을 사용
                    commit_times.append("Unknown time")
            else:
                commit_times.append("No commits found")  # 커밋이 아예 없는 경우

            # README.md 링크만 추출
            if "README.md" in item['path']:
                links.append(f"https://github.com/{user_repo}/blob/main/{item['path']}")
            else:
                links.append(f"https://github.com/{user_repo}/blob/main/{item['path']}")  # 다른 파일이 있다면 그대로 추가

    return sites, difficulties, problems, commit_times, links

# 업데이트된 README 내용 생성
def update_readme(repo, sites, difficulties, problems, commit_times, links, original_content):
    # "## 📑List📑" 섹션 찾기
    start_index = original_content.find("## 📑List📑")
    if start_index != -1:
        # "## 📑List📑" 이후 내용을 삭제
        end_index = original_content.find("\n", start_index + 1)
        original_content = original_content[:start_index] + original_content[end_index:]

    # 새로운 테이블 생성
    new_table = "## 📑List📑\n\n"
    new_table += "| 사이트 | 난이도 | 문제 | 풀이일 | 링크 |\n"
    new_table += "| --- | --- | --- | --- | --- |\n"

    # 문제에 대한 정보 테이블 생성
    for i in range(len(sites)):
        site = sites[i]
        difficulty = difficulties[i]
        problem = problems[i]
        commit_time = commit_times[i]
        link = links[i]
        new_table += f"| {site} | {difficulty} | {problem} | {commit_time} | [링크]({link}) |\n"

    # 난이도와 풀이일을 기준으로 정렬 (먼저 난이도, 그다음 풀이일)
    sorted_table = sorted(zip(sites, difficulties, problems, commit_times, links), key=lambda x: (x[1], x[3]))

    # 정렬된 데이터로 새로운 테이블 생성
    sorted_new_table = "## 📑List📑\n\n"
    sorted_new_table += "| 사이트 | 난이도 | 문제 | 풀이일 | 링크 |\n"
    sorted_new_table += "| --- | --- | --- | --- | --- |\n"
    for site, difficulty, problem, commit_time, link in sorted_table:
        sorted_new_table += f"| {site} | {difficulty} | {problem} | {commit_time} | [링크]({link}) |\n"

    # 기존 내용에 새로 정렬된 표를 추가
    updated_content = original_content + sorted_new_table
    return updated_content

# 기존 README.md 내용 읽기
try:
    with open("README.md", "r") as file:
        original_content = file.read()
except FileNotFoundError:
    original_content = ""

start_tag = "<!-- TEMPLATE_START -->"
end_tag = "<!-- TEMPLATE_END -->"
user_repo = os.getenv('GITHUB_REPOSITORY')

# 데이터 가져오기
sites, difficulties, problems, commit_times, links = get_data(user_repo)

# 최초 실행 여부 확인
if "<!-- INIT_DONE -->" not in original_content:
    print("README 초기 설정 중...")
    
    if start_tag in original_content and end_tag in original_content:
        start_index = original_content.find(start_tag)
        end_index = original_content.find(end_tag) + len(end_tag)
        original_content = original_content[:start_index] + original_content[end_index:]

    # 최초 실행 완료 태그 추가
    updated_content += "\n\n<!-- INIT_DONE -->"

    # 업데이트된 내용을 README 파일에 저장
    with open("README.md", "w") as file:
        file.write(updated_content)
else:
    print("README 초기 설정 이미 완료됨.")

# 리드미 업데이트
updated_content = update_readme(user_repo, sites, difficulties, problems, commit_times, links, original_content)

# 업데이트된 내용을 리드미 파일에 저장
with open("README.md", "w") as file:
    file.write(updated_content)
