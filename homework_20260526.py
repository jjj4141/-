import os

def get_file_info_dict(dir_path):
    file_dict = {}
    try:
        with os.scandir(dir_path) as entries:
            for entry in entries:
                if entry.is_file():
                    file_size = os.stat(entry.path).st_size
                    with open(entry.path, 'rb') as f:
                        file_content = f.read()
                    file_dict[entry.name] = (file_size, file_content)
    except Exception:
        pass
    return file_dict

def compare_directories():
    dir1 = input("첫 번째 하위 디렉터리 이름을 입력하세요: ")
    dir2 = input("두 번째 하위 디렉터리 이름을 입력하세요: ")
    
    dict1 = get_file_info_dict(dir1)
    dict2 = get_file_info_dict(dir2)
    
    if len(dict1) != len(dict2):
        print("결과: 두 디렉터리의 파일 개수가 다릅니다.")
        return False
        
    for file_name, (size1, content1) in dict1.items():
        if file_name not in dict2:
            print(f"결과: {file_name} 파일이 두 번째 디렉터리에 없습니다.")
            return False
            
        size2, content2 = dict2[file_name]
        
        if size1 != size2:
            print(f"결과: '{file_name}' 파일의 크기가 다릅니다.")
            return False
            
        if content1 != content2:
            print(f"결과: '{file_name}' 파일의 내용이 다릅니다.")
            return False
            
    print("결과: 두 디렉터리의 파일 수, 이름, 크기, 내용이 모두 완벽히 일치합니다.")
    return True

compare_directories()
