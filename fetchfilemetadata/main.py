import os
import boto3
import json
import urllib.request

gdrive_url = "https://www.googleapis.com/drive/v3/files"

def handler(event, context):
  #remove credentials from event
  accesstoken = event['accesstoken']
  event['accesstoken'] = '***'

  print("event")
  print(event)
  result = []
  fileid = event['fileid']

  request = urllib.request.Request(gdrive_url+'/'+id+'?fields=*')
  request.add_header('Authorization','Bearer '+accesstoken)

  with urllib.request.urlopen(request) as response:
    data = response.read().decode('utf-8')
    print(data)
    result = json.loads(data)
  print(result)
  return result
