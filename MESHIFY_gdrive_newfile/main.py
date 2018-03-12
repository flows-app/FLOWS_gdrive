import os
import boto3
import json
import urllib.request

gdrive_url = "https://www.googleapis.com/drive/v3/files"

def handler(event, context):
  print("event")
  print(event)

  directory = event['directory']
  params = urllib.parse.urlencode({'q': 'parents in \''+directory+'\''})
  print(params)
  request = urllib.request.Request(gdrive_url+'?'+params)
  request.add_header('Authorization','Bearer '+event['accesstoken'])
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
      id = fileentry['id']
      request2 = urllib.request.Request(gdrive_url+'/'+id+'?fields=modifiedTime,kind,id,name,mimeType')
      request2.add_header('Authorization','Bearer '+event['accesstoken'])
      response2 = urllib.request.urlopen(request2)
      content2 = response2.read()
      fileitem = json.loads(content2)
      fileitem['dedupid']=fileitem['id']+fileitem['modifiedTime']
      result.append(fileitem)
      print(content2)
  print(result)
  return result
