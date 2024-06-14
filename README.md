# AI-Video-script-generation
# AI视频脚本生成器


## 环境部署
首先要创建并启动一个虚拟环境，用于隔离项目依赖。

### 使用的python版本
- Python 3.12.1

### 创建虚拟环境
```shell
python -m venv venv
```
### 激活虚拟环境
```shell
venv/Scripts/activate
```

### 安装基本依赖

```shell
pip install langchain langchain_openai langchain_community streamlit
```
依赖介绍
- langchain: 用于构建AI应用的框架
- langchain_openai: 用于连接OpenAI API的库
- langchain_community: 用于连接社区API的库
- streamlit: 用于构建Web应用的库


### 创建`.gitignore`文件排除venv文件夹
```gitignore
venv/
```

### 新建文件`utils.py`用于存储工具函数
#### 
```python

```