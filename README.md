# AI-Video-script-generation
# AI视频脚本生成器

## 项目使用部署
### 克隆仓库
首先克隆仓库到本地

### 安装依赖
```shell
pip install -r requirements.txt
```

### 启动项目
```shell
streamlit run main.py
```


## 项目制作流程
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
# 导入模板
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper 


#定义输出脚本函数
def generate_script(subject, video_length, creativity,api_key):
    '''
    subject: 主题
    video_length: 视频时长
    creativity: 创造性
    api_key: OpenAI API密钥
    '''
    # 创建模板
    title_template = ChatPromptTemplate.from_messages([
        ("human", "请为'{subject}'这个主题像一个吸引人的标题"),
    ])
    script_template = ChatPromptTemplate.from_messages([
        ("human",
        """
        你是一位短视频频道的博主。根据以下标题和相关信息，为短视频频道写一个视频脚本。
        视频标题：{title}，视频时长：{duration}分钟，生成的脚本的长度尽量遵循视频时长的要求。
        要求开头抓住限球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头、中间，结尾】分隔。
        整体内容的表达方式要尽量轻松有趣，吸引年轻人。
        脚本内容可以结合以下维基百科搜索出的信息，但仅作为参考，只结合相关的即可，对不相关的进行忽路:
        ```{wikipedia_search}```
        """)])
    
    # 导入模型
    model = ChatOpenAI(temperature=creativity, openai_api_key=api_key,base_url=ChatGPTConfig.base_url)

    # 创建链
    title_chain = title_template | model
    script_chain = script_template | model

    # 调用链
    title = title_chain.invoke({"subject": subject}).content
    search = WikipediaAPIWrapper(lang="zh")
    search_result = search.run(subject)

    # 调用方法
    script = script_chain.invoke({
        "title": title,
        "duration": video_length,
        "wikipedia_search": search_result
    }).content

    # 返回结果
    return search_result, title, script
```

### 创建文件`main.py`用于构建Web应用
#### 
```python
import streamlit as st
from utils import generate_script

st.title("📽️ 视频脚本生成器")

with st.sidebar:
    openai_base_url = st.text_input("API 基础URL:",value="https://free.gpt.ge/v1")
    openai_api_key = st.text_input("请输入OpenAI API 密钥:",type="password")
    st.markdown("[获取api密钥链接](https://platform.openai.com/account/api-keys)")

shubject = st.text_input("💡 请输入视频主题:")
vedio_length = st.number_input("📝 请输入视频时长大致（分钟）:",min_value=0.1,step=0.1)
creativity = st.slider("请输入视频脚本的创造力(数字小说明更严谨，数字大说明更多样)",min_value=0.1,max_value=1.0,step=0.1,value=0.3)

submit = st.button("生成脚本")

if submit and not openai_base_url:
    st.info("请输入API 基础URL")
    st.stop()
elif submit and not openai_api_key:
    st.info("请输入OpenAI API 密钥")
    st.stop()
elif submit and not shubject:
    st.info("请输入视频主题")
    st.stop()
elif submit and not vedio_length >= 0.1:
    st.info("视频长度需要大于或等于0.1")
    st.stop()
if submit:
    with st.spinner(("AI正在思考中，请稍等...")):
        search_result, title, script = generate_script(shubject,vedio_length,creativity,openai_api_key)

    st.success("脚本生成成功!")
    st.subheader("🔥 标题:")
    st.write(title)
    st.subheader("📝 视频脚本:")
    st.write(script)
```
