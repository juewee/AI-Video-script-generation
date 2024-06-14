# 导入模板
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper 
from api_key import ChatGPTConfig


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

# 调用函数
# print(generate_script(subject="人工智能", video_length=2, creativity=0.7,api_key=ChatGPTConfig.api_key))