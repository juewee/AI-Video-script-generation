# 导入库
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