import streamlit as st
from utils import generate_script

st.title("📽️ 视频脚本生成器")

with st.sidebar:
    openai_base_url = st.text_input("API 基础URL:",value="https://free.gpt.ge/v1")
    openai_api_key = st.text_input("请输入OpenAI API 密钥:",type="password",value="sk-6Ghj6HzVcpCZ9tPpCd63526512Ca4523Ab25F19f3d77AeB0")
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