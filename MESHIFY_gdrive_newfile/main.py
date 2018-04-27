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

  directory = event['directory']
  params = urllib.parse.urlencode({'q': 'parents in \''+directory+'\''})
  print(params)
  request = urllib.request.Request(gdrive_url+'?'+params)
  request.add_header('Authorization','Bearer '+accesstoken)
  result = []
  with urllib.request.urlopen(request) as response:
    content = response.read()
    # {
    #      "kind": "drive#fileList",
    #      "incompleteSearch": false,
    #      "files": [
    #       {
    #        "kind": "drive#file",
    #        "id": "1qEXCqvQVNezQY6IiuQOebiARlq1SxUTC",
    #        "name": "blach.pdf",
    #        "mimeType": "application/pdf"
    #       }
    #      ]
    #     }
    filelist = json.loads(content)
    for fileentry in filelist['files']:
        fileentry['dedupid']=fileentry['id']
        result.append(fileentry)

  print(result)
  return result
