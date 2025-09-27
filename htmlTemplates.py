css = '''
<style>
    /* Background setup with placeholder comment */
    .stApp {
        background-image: url('https://img.pikbest.com/wp/202343/sleek-contemporary-abstract-grid-black-background-with-geometric-patterns_9971045.jpg!w700wp');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
        min-height: 100vh;
    }
    
    /* Semi-transparent overlay to ensure text readability */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(15, 17, 22, 0.85);
        z-index: -1;
    }
    
    /* Chat message enhancements for better visibility on backgrounds */
    .chat-message {
        padding: 1.5rem; 
        border-radius: 12px; 
        margin-bottom: 1.5rem; 
        display: flex;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
        transition: all 0.3s ease;
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .chat-message:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        border-color: rgba(255, 255, 255, 0.2);
    }
    
    .chat-message.user {
        background: linear-gradient(135deg, rgba(43, 49, 62, 0.9) 0%, rgba(58, 66, 82, 0.95) 100%);
        border-left: 4px solid #4f8bf9;
    }
    
    .chat-message.bot {
        background: linear-gradient(135deg, rgba(71, 80, 99, 0.9) 0%, rgba(86, 101, 122, 0.95) 100%);
        border-left: 4px solid #f94f7b;
    }
    
    .chat-message .avatar {
        width: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 1rem;
    }
    
    .chat-message .avatar img {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .chat-message .message {
        flex: 1;
        padding: 0.75rem 1.25rem;
        color: #ffffff;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        line-height: 1.7;
        font-size: 1rem;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
    }
    
    /* Sidebar styling to match */
    .stSidebar {
        background: rgba(20, 23, 30, 0.85) !important;
        backdrop-filter: blur(8px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.freepik.com/free-vector/cartoon-style-robot-vectorart_78370-4103.jpg?semt=ais_hybrid&w=740&q=80">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrT9QfTWesZk1IklGxsaH7hioyMTC7oLyTYg&s">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''