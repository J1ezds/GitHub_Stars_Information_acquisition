# GitHub_Stars_Information_acquisition

通过GitHub Api获取指定用户 Stars 过的仓库列表，并输出为 Markdown 格式的文件

## 使用方法

1. 克隆此仓库：

   ```bash
   git clone https://github.com/Weske5/GitHub_Stars_Information_acquisition.git
   ```

2. 在 `stars.py` 文件中修改 `username` 变量，将其设置为你要获取 Star 列表的 Github 用户名

3. 在 `token` 处填入您自己GitHub的Token

   申请access token认证方式
   
   进入GitHub   =>  点击头像  =>  点击 Settings  =>  Developer Settingss  =>
   =>   Personal access tokens  =>  tokens (classic)   => 点击右侧 Generate new token (classic)
   
   在Select scopes里把 user 打勾就可以了

   ps：为什么需要您自己 GitHub 的 Token ？
   
      GitHub 对每小时可以发送的请求数量有限制。通常，GitHub API的标准限制为：
   
      未经身份验证 - 每个原始 IP 地址每小时60个请求；
   
      已验证 – 每个用户每小时可发送 5,000 个请求。

5. 安装python依赖：

   ```bash
   pip install requests
   ```

6. 运行程序：

   ```bash
   python stars.py
   ```

运行成功后，你将在项目里下看到一个名为 `starred_projects.md` 的 Markdown 文件

其中包含了你所选用户的所有 Stars 过的仓库列表



