import sys
import re

from enum import Enum

class Mode(Enum):
    HEAD = 0
    BODY = 1

def check(source, dest, added, removed, source_ver, dest_ver):
    if source is None or dest is None:
        return False

    if removed and added:
        level = "Modified"
    if removed:
        level = "Removed"
    elif added:
        level = "Added"
    else:
        level = "Not Changed"

    if source_ver is None and dest_ver is None:
        update_mode = "No Update"
    elif source_ver is None:
        update_mode = "New"
    elif dest_ver is None:
        update_mode = "Delete"
    else:
        source_vers = source_ver.split(".")
        dest_vers = dest_ver.split(".")

        if int(source_vers[0]) != int(dest_vers[0]):
            update_mode = "Major"

        elif int(source_vers[1]) != int(dest_vers[1]):
            update_mode = "Minor"

        else:
            update_mode = "No Update"

    if update_mode == "No Update":
        if level != "Not Changed":
            result = "Failure"
        else:
            result = "OK"
    elif update_mode == "Minor":
        if removed:
            result = "Failure"
        else:
            result = "OK"
    elif update_mode == "Major":
        result = "OK"
    elif update_mode == "New":
        result = "OK"
    elif update_mode == "Delete":
        if added:
            result = "Failure"
        else:
            result = "OK"

    print("{} -> {} : version:{}({} -> {}) : {} ... {}".format(source, dest, update_mode, source_ver, dest_ver, level, result))
    return result != "OK"

mode = Mode.HEAD
failure = False
source = None
dest = None
added = False
removed = False
source_ver = None
dest_ver = None

ver_regex = re.compile(r"ver\:([0-9]+\.[0-9]+)");

while True:
    line = sys.stdin.readline()

    if mode == Mode.HEAD:
        if line.startswith("---"):
            source = line[4:-1]
        elif line.startswith("+++"):
            dest = line[4:-1]
        elif line.startswith("@@"):
            mode = Mode.BODY
            
    if mode == Mode.BODY:
        if line.startswith("-"):
            if source_ver is None and not removed:
                matched = ver_regex.search(line)
                if matched is not None:
                    source_ver = matched.group(1)
                else:
                    removed = True
            else:
                removed = True

        elif line.startswith("+"):
            if dest_ver is None and not added:
                matched = ver_regex.search(line)
                if matched is not None:
                    dest_ver = matched.group(1)
                else:
                    added = True
            else:
                added = True

        elif line.startswith("index"):
            if check(source, dest, added, removed, source_ver, dest_ver):
                failure = True

            source = None
            dest = None
            added = False
            removed = False
            source_ver = None
            dest_ver = None
            mode = Mode.HEAD

    if not line:
        break
    
if check(source, dest, added, removed, source_ver, dest_ver):
    failure = True

if failure:
    print("Failure")
    exit(1)
else:
    print("Success")