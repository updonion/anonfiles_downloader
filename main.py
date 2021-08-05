import re
import requests

pattern = r"(https:\/\/anonfiles.com\/)([\w]{10})(\/.*)"
search_file_id = re.compile(pattern=pattern)
user_file = input("Path to your file with links: ") 

rows = open(user_file, 'r')
print("file_id,size,name")
for i in rows:
    file_id = re.findall(pattern, i)
    if file_id:
        if_exist = requests.get(f"https://api.anonfiles.com/v2/file/{file_id[0][1]}/info").json()
        if if_exist['status']:
            print(if_exist['data']['file']['metadata']['id'], if_exist['data']['file']['metadata']['size']['bytes'], f"\"{if_exist['data']['file']['metadata']['name']}\"", sep=',')
