import requests

username = "需要获取的用户名称"
token = "您自己的Token"

try:
    url = f"https://api.github.com/users/{username}/starred"

    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        
        # 获取第一页的收藏项目信息
        projects = response.json()
        all_projects = projects

        # 获取收藏项目的总数
        total_count = response.headers.get('X-Total-Count')
        if total_count:
            total_count = int(total_count)
        else:
            total_count = len(projects)

        # 检查是否有更多的页面
        while 'next' in response.links.keys():
            # 获取下一页的项目信息
            url = response.links['next']['url']
            response = requests.get(url, auth=(username, token))
            projects = response.json()
            all_projects.extend(projects)

            # 更新进度
            current_count = len(all_projects)
            print(f"获取项目进度: {current_count}/{total_count}")
        print(f"{username}共有Stars数量: {current_count}")

        # 创建Markdown文件并倒序写入项目信息
        filename = f"{username}_starred_projects.md"
        with open(filename, "w") as file:
            file.write(f"# {username} Starred Projects\n\n")
            for project in reversed(all_projects):
                # file.write(f"- [{project['name']}]({project['html_url']})\n")
                file.write(f"# {project['name']}\n\n")
                file.write(f"**项目链接:**{project['html_url']}\n\n")
                file.write(f"**项目全名:**{project['full_name']}\n\n")   
                file.write(f"**项目简介:**{project['description']}\n\n")
            
    else:
        print("未获取到Stars项目信息")
except requests.exceptions.RequestException as e:
    print("发生错误:", e)
