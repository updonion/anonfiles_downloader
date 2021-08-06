import re
import requests
import os.path

pattern = r"(https:\/\/anonfiles.com\/)([\w]{10})(\/.*)?"
dl_name_pat = r"(https:\/\/cdn-[\d]*.anonfiles.com\/)([\w]{10})(\/[\w-]{19}\/)(.*)\""

# search_file_id = re.compile(pattern=pattern)
user_file = input("Path to your file with links: ") 

rows = open(user_file, 'r')
for i in rows:
    file_id = re.findall(pattern, i)
    if file_id:
        if_exist = requests.get(f"https://api.anonfiles.com/v2/file/{file_id[0][1]}/info").json()
        if if_exist['status']:
            file_link_id = if_exist['data']['file']['metadata']['id']
            file_page = requests.get(f"https://anonfiles.com/{file_link_id}/").text
            download_link = re.findall(dl_name_pat, file_page)
            if download_link[0][0] and download_link[0][1] and download_link[0][2]:
                ready_download_link = download_link[0][0] + download_link[0][1] + download_link[0][2]
                
                file_name = f"[{file_link_id}]_{download_link[0][3]}"
                
                #Checking if the file exist
                if os.path.isfile(file_name):
                    print(f"{file_name} already exist")
                else:
                    # Downloading file
                    file = requests.get(ready_download_link)
                    with open(f"downloads/{file_name}", 'wb') as download_to:
                        download_to.write(file.content)
                        print(f"File {file_name} downloaded")
            else:
                print(f"Error with file https://anonfiles.com/{file_link_id}")
