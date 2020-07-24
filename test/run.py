import glob
import subprocess
import os
import sys

test_dir = os.path.dirname(__file__)
out_files = set()

# code 以下の *.py ファイルを検索
for file in glob.glob(test_dir + "/code/**/*.py", recursive=True):
    relpath = os.path.relpath(file, test_dir + "/code")
    file_name = os.path.splitext(relpath)[0]

    extension = ".txt"

    if file_name.endswith("_svg"): 
        extension = ".svg"

    out_file_path = test_dir + "/out/" + file_name + extension
    
    os.makedirs(os.path.dirname(out_file_path), exist_ok=True) # 出力フォルダが無ければ作成
    out_file = open(out_file_path, "w")

    # `python *.py` のプロセスを実行
    subprocess.run([sys.executable, file], stdout=out_file)
    
    # 出力したファイルを記録
    out_files.add(os.path.abspath(out_file_path))

# 削除ずみのテストの出力を削除
for file in glob.glob(test_dir + "/out/**/*", recursive=True):
    if os.path.isfile(file):
        if not os.path.abspath(file) in out_files: # 出力ファイルに含まれてないファイルを削除
            os.remove(file)
