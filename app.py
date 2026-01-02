import streamlit as st
import time
import os

# ================= 1. 界面与国际化配置 =================
LANG_PACK = {
    "zh": {
        "nav_home": "首页",
        "nav_user": "用户中心",
        "nav_recharge": "充值中心",
        "title": "📚 AI 全科试题专家解析系统",
        "welcome": "欢迎回来，尊贵的用户！",
        "subject_label": "第一步：选择解析学科",
        "upload_label": "第二步：上传试卷 (支持 Word/PDF)",
        "process_btn": "开始专家级解析",
        "footer": "© 2024 AI解析实验室 - 您的智能学习助手",
        "login": "登录",
        "register": "注册",
        "balance": "当前余额",
        "unit": "点位",
        "lang_name": "English"
    },
    "en": {
        "nav_home": "Home",
        "nav_user": "User Profile",
        "nav_recharge": "Recharge",
        "title": "📚 AI Multi-Subject Analysis System",
        "welcome": "Welcome back, User!",
        "subject_label": "Step 1: Select Subject",
        "upload_label": "Step 2: Upload Paper (Word/PDF)",
        "process_btn": "Start Expert Analysis",
        "footer": "© 2024 AI Lab - Your Intelligent Tutor",
        "login": "Login",
        "register": "Register",
        "balance": "Balance",
        "unit": "Credits",
        "lang_name": "中文"
    }
}

# 初始化语言状态
if 'lang' not in st.session_state:
    st.session_state.lang = 'zh'


def toggle_lang():
    st.session_state.lang = 'en' if st.session_state.lang == 'zh' else 'zh'


# ================= 2. 侧边栏：用户与充值 =================
def render_sidebar(t):
    with st.sidebar:
        st.button(t["lang_name"], on_click=toggle_lang)
        st.markdown("---")

        # 用户登录/注册模块
        st.subheader(t["nav_user"])
        tab_l, tab_r = st.tabs([t["login"], t["register"]])
        with tab_l:
            st.text_input("ID", placeholder="Email/Phone")
            st.text_input("Password", type="password")
            st.button(t["login"], use_container_width=True)

        # 充值模块接口
        st.markdown("---")
        st.subheader(t["nav_recharge"])
        st.metric(label=t["balance"], value=f"120 {t['unit']}")
        if st.button("💳 扫码充值"):
            st.info("支付接口回调中... (对接阿里云支付接口)")


# ================= 3. 主界面：学科路由与上传 =================
def render_main(t):
    st.title(t["title"])
    st.info(t["welcome"])

    # 学科选择接口
    subject = st.selectbox(
        t["subject_label"],
        ["英语 (English)", "数学 (Math)", "语文 (Chinese)", "物理 (Physics)", "其他 (Others)"]
    )

    # 文件上传
    uploaded_file = st.file_uploader(t["upload_label"], type=['docx', 'pdf'])

    if uploaded_file:
        st.success(f"已接收文件: {uploaded_file.name}")

        if st.button(t["process_btn"], type="primary"):
            # 路由逻辑
            if "英语" in subject:
                run_english_logic(uploaded_file)
            else:
                run_general_logic(subject, uploaded_file)


# ================= 4. 后端逻辑接口 (在这里接你之前的代码) =================
def run_english_logic(file):
    with st.status("正在调用英语名师模板...", expanded=True) as status:
        st.write("🔍 正在扫描试卷结构...")
        time.sleep(1)
        st.write("🚀 正在并发请求 DeepSeek 专家引擎...")
        time.sleep(2)
        status.update(label="解析完成！", state="complete", expanded=False)

    st.balloons()
    st.download_button("📩 下载专家解析报告", data="假装这是生成的word内容", file_name="Expert_Analysis.docx")


def run_general_logic(subj, file):
    st.warning(f"当前学科 [{subj}] 使用通用 AI 逻辑解析中...")
    # 这里接入你 V6.0 版本的“综合题型”自适应逻辑


# ================= 5. 程序入口 =================
t = LANG_PACK[st.session_state.lang]
render_sidebar(t)
render_main(t)
st.markdown("---")
st.caption(t["footer"])
