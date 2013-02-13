import requests
import getpass
from dateutil import parser
from pandas import Series, DataFrame

def getUserAndPass():
    '''Ask for username and password'''
    user=raw_input("Username: ")
    password=getpass.getpass()
    return (user, password)

def fetchCommitInfo(cred):
    '''Get the data from the pythonkurs repository and return it as a dataframe'''
    repositories = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=cred).json()
    
    repoDict = {} #To save Series in before converting to dataframe

    for repository in repositories:
        repoName = repository['name']
        commitURL = repository['commits_url'].replace("{/sha}","")
        commitSeries = getCommitSeries(commitURL, cred)
        repoDict[repoName] = (commitSeries)

    return DataFrame(repoDict)
                                             
def getCommitSeries(commitURL, cred):
    '''Extract time and message for every commit'''

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

def getCommonWeekdayAndHour(commitDataFrame):
    '''Find the most common day of the week and the most common hour to commit'''
    weekDays=['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'] 
    commitDates=commitDataFrame.count(1).resample("D", how='sum').fillna(0)
    commitWeekdayFreq=commitDates.groupby(commitDates.index.weekday).sum()
    comWeekday = weekDays[commitWeekdayFreq.idxmax()]
        
    commitTimes=commitDataFrame.count(1).resample("H", how='sum').fillna(0)
    commitHourFreq=commitTimes.groupby(commitTimes.index.hour).sum()
    comHour=commitHourFreq.idxmax()
    return comWeekday, comHour

    
def assignment4():
    cred = getUserAndPass()
    commitDataFrame=fetchCommitInfo(cred)
    (day,hour) = getCommonWeekdayAndHour(commitDataFrame)
    print "Most common weekday is", day, "and the most common hour is", hour


if __name__ == '__main__':
    assignment4()
