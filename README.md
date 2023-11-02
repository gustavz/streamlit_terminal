# Insecure Streamlit Terminal

> ⚠️ Security Warning: This app allows execution of arbitrary commands which can be used to compromise your system. 
Never run this in a production environment or on a system with sensitive data. 
Always use within a secure, controlled environment and only with trusted users.

## Getting Started

1. Build image: `docker build -t streamlit_terminal .`
2. Run container: `docker run -p 80:80 streamlit_terminal`
3. Check if app works: http://0.0.0.0/
4. Export the app: `docker save streamlit_terminal > streamlit_terminal.tar`
5. Deploy to any server and make the admins cry