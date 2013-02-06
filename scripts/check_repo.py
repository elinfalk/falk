from falk.session3 import CourseRepo, RepoDir

import sys
import os

''' Check that there is only one argument'''
if len(sys.argv) != 2:
    print "Error: Number of arguments are wrong!"
    print "Usage: check_repo.py <absolute path to repository>"
    sys.exit()
    
absolutePath = sys.argv[1]

(repoDir, lastname) = os.path.split(absolutePath)

with RepoDir(absolutePath):
    courseRepo = CourseRepo(lastname)
    if courseRepo.check():
        print "PASS"
    else:
        print "FAIL"
