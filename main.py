import re
import requests

pattern = r"(https:\/\/anonfiles.com\/)([\w]{10})(\/.*)"
dl_name_pat = r"(https:\/\/cdn-[\d]*.anonfiles.com\/)([\w]{10})(\/[\w-]{19}\/)(.*.txt)" # TODO Works only with text files

# search_file_id = re.compile(pattern=pattern)
user_file = input("Path to your file with links: ") 

rows = open(user_file, 'r')
print("file_id,size,name")
for i in rows:
    file_id = re.findall(pattern, i)
    if file_id:
        if_exist = requests.get(f"https://api.anonfiles.com/v2/file/{file_id[0][1]}/info").json()
        if if_exist['status']:
            file_link_id = if_exist['data']['file']['metadata']['id']
            file_page = requests.get(f"https://anonfiles.com/{file_link_id}/").text
            download_link = re.findall(dl_name_pat, file_page)
            ready_download_link = download_link[0][0] + download_link[0][1] + download_link[0][2]
            print(ready_download_link)
            file_name = f"[{file_link_id}]_{download_link[0][3]}"
            print("File name: ", file_name)
            # download_to = 
            print(if_exist['data']['file']['metadata']['id'], if_exist['data']['file']['metadata']['size']['bytes'], f"\"{if_exist['data']['file']['metadata']['name']}\"", sep=',')
