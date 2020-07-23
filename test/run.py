import glob
import subprocess
import os
import sys
import shutil

test_dir = os.path.dirname(__file__)

# 出力ディレクトリのクリーン
if os.path.isdir(test_dir + "/out"):
    shutil.rmtree(test_dir + "/out")

os.makedirs(test_dir + "/out", exist_ok=True)

for file in glob.glob(test_dir + "/code/*.py"):
    file_name = os.path.splitext(os.path.basename(file))[0]

    extension = ".txt"

    if file_name.endswith("_svg"): 
        extension = ".svg"

    out_file_path = test_dir + "/out/" + file_name + extension
    out_file = open(out_file_path, "w")

    # テストを実行
    python_executable = sys.executable
    subprocess.run([python_executable, file], stdout=out_file)
