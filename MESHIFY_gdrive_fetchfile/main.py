import os
import boto3
import json
import urllib.request

gdrive_url = "https://www.googleapis.com/drive/v3/files"

def handler(event, context):
  print("event")
  print(event)
  result = []
  accesstoken = event['accesstoken']
  fileid = event['fileid']
  targeturl = event['targeturl']

  request = urllib.request.Request(gdrive_url+'/'+fileid+'?alt=media')
  request.add_header('Authorization','Bearer '+accesstoken)

  with urllib.request.urlopen(request) as response:
    data = response.read()
    #put file to s3
    request2 = urllib.request.Request(targeturl,data=data,method='PUT')
    with urllib.request.urlopen(request2) as response2:
      data2 = response2.read()
      print(data2)

  return {"status":"done"}
