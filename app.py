import streamlit as st

# Configure page settings first (must be the first Streamlit command in the script)
st.set_page_config(
    page_title="PDF Intelligence HuB - AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import state manager and layouts
from src.session_manager import SessionManager
from src.constants import PAGE_HOME, PAGE_QUIZ, PAGE_CHAT, SS_CURRENT_PAGE
from ui.components import apply_custom_css
from ui.sidebar import render_sidebar
from ui.home import render_home_page
from ui.quiz_page import render_quiz_page
from ui.chatbot_page import render_chatbot_page

def main():
    # 1. Initialize states
    SessionManager.initialize_session()
    
    # 2. Inject global custom CSS
    apply_custom_css()
    
    # 3. Render settings sidebar panel
    render_sidebar()
    
    # 4. View Page Routing
    current_page = st.session_state.get(SS_CURRENT_PAGE, PAGE_HOME)
    
    if current_page == PAGE_HOME:
        render_home_page()
    elif current_page == PAGE_QUIZ:
        render_quiz_page()
    elif current_page == PAGE_CHAT:
        render_chatbot_page()

if __name__ == "__main__":
    main()
