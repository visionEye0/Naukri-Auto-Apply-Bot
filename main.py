import requests
import asyncio
import json
import sys
import argparse
from rich.progress import track
from rich.console import Console

console = Console()


# command line arguments reading

parser = argparse.ArgumentParser(prog="Naukri JBOT")

parser.add_argument("-k", help="input the jobs you want to apply for comma (,) seperated (required)", metavar="[keywords]", dest="keyword", required=True )
parser.add_argument("-e", metavar='[experience]', dest="experience", help="Job Experience in numbers (optional)", required=False)
parser.add_argument("-l", metavar='[location]', dest="location", help="Location of the job, (use comma seperated values for multiple locations) (optional)", required=False)
parser.add_argument("-n", metavar='[no of applies]', dest="no_of_applies", help="Total amount of job applies you want to send, default is 10 (optional)", default=10)
parser.add_argument("-u", metavar='[username/email]', dest="username", help="Your naukri account's username/ email", required=True)
parser.add_argument("-p", metavar='[password]', dest="password", help="Your naukri account's password", required=True)

args = parser.parse_args()

# global variables
host = "https://www.naukri.com"

async def userAuthentication(username, password):
    loginEndpoint = "/central-login-services/v1/login"
    data = {
        "username": username,
        "password": password
    }

    headers = {
        'Content-type':'application/json', 
        'Accept':'application/json',
        'Systemid': 'jobseeker',
        'Appid': '103'
    }

    response = requests.post(url=f'{host}{loginEndpoint}', json=data, headers=headers)
    responseDict = json.loads(response.text)
    try:
        responseDict['cookies']
    except:
        console.print(f'[bold red]{responseDict["message"]}')
        sys.exit()

    console.print(f'[green]Naukri Auth Successful!')
    return response.cookies

async def searchJobs(keyword, location="", experience="", pageNo=1, noOfResults=10):
    jobSearchEndpoint = "/jobapi/v3/search"

    params = {
        "noOfResults": noOfResults,
        "urlType": "search_by_key_loc",
        "searchType": "adv",
        "keyword": keyword,
        "location": location,
        "experience": experience,
        "pageNo": pageNo,
    }

    headers = {
        "Appid": '109',
        "Systemid": '109'
    }

    response = requests.get(url=f'{host}{jobSearchEndpoint}', params=params, headers=headers)
    return response.text


async def applyJobs(jobId, cookies):
    jobApplyEndpoint = "/ims/intercept"

    params = {
        "jobid": jobId,
        "appid": '107'
    }

    response = requests.get(url=f"{host}{jobApplyEndpoint}", params=params, cookies=cookies)
    return response.text

async def main():
    successfulApplies = 0
    failedApplies = 0
    authCookies = await userAuthentication(args.username, args.password)
    jobsData = await searchJobs(noOfResults=args.no_of_applies, keyword=args.keyword, location=args.location, experience=args.experience)
    jobsDataDict = json.loads(jobsData)
    jobDetails = jobsDataDict['jobDetails']
    
    for jobObj in track(jobDetails, description="[bold cyan]Jobs applying ..."):
        jobApplyStatus = await applyJobs(jobId=jobObj['jobId'], cookies=authCookies)
        jobApplyStatusDict = json.loads(jobApplyStatus)
        console.print(f'[cyan] applying for {jobObj["title"]}')
        try:
            isJobAppliedSuccessfully = jobApplyStatusDict['redirectURL']
            successfulApplies = successfulApplies + 1
        except:
            failedApplies = failedApplies + 1

    console.print(f'[green]Total Job Applies: {args.no_of_applies}\nSuccessful Job Applies: {successfulApplies}\nFailed Job Applies: {failedApplies}\n[cyan]Note: Failed applies are jobs which needs to be applied outside naukri website.')




asyncio.run(main())



