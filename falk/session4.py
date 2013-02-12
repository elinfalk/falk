import requests
import getpass
from dateutil import parser
from pandas import Series, DataFrame

def getUserAndPass():
#    user=raw_input("Username: ")
    user='elinfalk'
    password=getpass.getpass()
    return (user, password)

def fetchCommitInfo(cred):

    repositories = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=cred).json()
    
    repoDict = {} #To save Series in before converting to dataframe

    for repository in repositories:
        repoName = repository['name']
        commitURL = repository['commits_url'].replace("{/sha}","")
        commitSeries = getCommitSeries(commitURL, cred)
        repoDict[repoName] = (commitSeries)

    return DataFrame(repoDict)
                                             
def getCommitSeries(commitURL, cred):

    commits = requests.get(commitURL, auth=cred).json()
    if type(commits) == list: # Didn't find any other better way to make sure there is something to parse
        times=[]
        messages=[]
    
        for commit in commits:
            commitMessage = commit['commit']['message']
            commitTime = parser.parse(commit['commit']['committer']['date'])
            times.append(commitTime)
            messages.append(commitMessage)
        return Series (messages, index=times)



if __name__ == '__main__':
    cred = getUserAndPass()
    commitDataFrame=fetchCommitInfo(cred)

