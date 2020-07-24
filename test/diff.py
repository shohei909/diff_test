
import subprocess
import os

# Git で差分を表示
test_dir = os.path.dirname(__file__)
subprocess.run(["git", "add", "-N", test_dir + "/out"])
subprocess.run(["git", "--no-pager", "diff", "--relative=test/out", "--ignore-space-change"])
