import os

def get_valid_directory(prompt):
    while True:
        dir_name = input(prompt)
        if not os.path.exists(dir_name):
            print("에러: 존재하지 않는 경로입니다.")
            continue
        if not os.path.isdir(dir_name):
            print("에러: 디렉터리가 아닙니다.")
            continue
        return dir_name

def get_all_files_recursive(base_path, current_path, file_dict):
    try:
        # os.listdir() 또는 os.scandir() 활용 (여기서는 성능이 좋은 scandir 채택)
        with os.scandir(current_path) as entries:
            for entry in entries:
                if entry.is_dir():
                    # 하위 폴더를 만나면 재귀 호출로 끝까지 파고듦
                    get_all_files_recursive(base_path, entry.path, file_dict)
                elif entry.is_file():
                    # 기말고사 핵심: 두 폴더의 구조적 일치를 위해 상대 경로를 키(Key)로 사용
                    rel_path = os.path.relpath(entry.path, base_path)
                    file_size = entry.stat().st_size
                    file_dict[rel_path] = file_size
                    
    except PermissionError:
        # 교수님 요구사항: 접근 제한 폴더를 만나면 통과 처리
        pass
    except Exception:
        pass

def compare_directories_final():
    dir1 = get_valid_directory("첫 번째 디렉토리 이름을 입력하세요: ")
    dir2 = get_valid_directory("두 번째 디렉토리 이름을 입력하세요: ")
    
    dict1 = {}
    dict2 = {}
    
    get_all_files_recursive(dir1, dir1, dict1)
    get_all_files_recursive(dir2, dir2, dict2)
    
    if len(dict1) != len(dict2):
        print("다름")
        return False
        
    for rel_path, size1 in dict1.items():
        if rel_path not in dict2:
            print("다름")
            return False
            
        size2 = dict2[rel_path]
        if size1 != size2:
            print("다름")
            return False
            
    print("같음")
    return True

compare_directories_final()