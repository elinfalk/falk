import os

''' Class which checks that all required files are present'''
class CourseRepo(object):
    def __init__(self, surname):
        self.required=[]
        self.surname = surname
    
    @property 
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname(self, lastname):
        del self.required[:]
        self.required.append(".git")
        self.required.append("setup.py")
        self.required.append("README.md")
        self.required.append("scripts/getting_data.py")
        self.required.append("scripts/check_repo.py")
        self.required.append(lastname + "/__init__.py")
        self.required.append(lastname + "/session3.py")
        self._surname = lastname
    
    ''' Method checks if all files in the required list exist'''
    def check(self):
        for fil in self.required:
            if not os.path.exists(fil) :
                return False
        return True
    
    ''' A context manager which switches dir to the given path when executing and then back when done'''
class RepoDir(object):
    def __init__(self, p):
        self.originalPath = os.getcwd()
        self.newPath = p

    # Changing to the path given path
    def __enter__(self):
        os.chdir(self.newPath)

    # Changing back to original path    
    def __exit__(self, type, value, traceback):
        os.chdir(self.originalPath)
