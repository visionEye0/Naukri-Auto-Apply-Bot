import requests
import asyncio
import json


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

    return response.cookies

async def searchJobs(noOfResults, keyword, location="", experience="", pageNo=1):
    jobSearchEndpoint = "/jobapi/v3/search"

    params = {
        "noOfResults": noOfResults,
        "urlType": "search_by_key_loc",
        "searchType": "adv",
        "keyword": keyword,
        "location": location,
        "experience": experience,
        "pageNo": pageNo,
        # "sort": "p"
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
    authCookies = await userAuthentication("pranavsayshii@gmail.com", "my_password")
    jobsData = await searchJobs(pageNo=3, noOfResults=10, keyword="penetration tester, developer", location="hyderabad, bangalore", experience=2)
    jobsDataDict = json.loads(jobsData)
    jobDetails = jobsDataDict['jobDetails']
    
    for jobObj in jobDetails:
        jobApplyStatus = await applyJobs(jobId=jobObj['jobId'], cookies=authCookies)
        jobApplyStatusDict = json.loads(jobApplyStatus)
        try:
            isJobAppliedSuccessfully = jobApplyStatusDict['redirectURL']
            print('job success === ', isJobAppliedSuccessfully)
        except:
            print('job fail')




asyncio.run(main())



