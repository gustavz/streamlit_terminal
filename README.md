# Insecure Streamlit Terminal

> ⚠️ Security Warning: This app allows execution of arbitrary commands which can be used to compromise your system. 
Never run this in a production environment or on a system with sensitive data. 
Always use within a secure, controlled environment and only with trusted users.<br><br>
This is a hosted terminal with internet access. The possibilties are endless. Use with caution.

## Getting Started

1. Build image: `docker build -t streamlit_terminal .`
2. Run container: `docker run -p 80:80 streamlit_terminal`
3. Check if app works: http://0.0.0.0/
4. Export the app: `docker save streamlit_terminal > streamlit_terminal.tar`
5. Deploy to any server and explore the possibilties


## A little help to understand the potential

This unrestricted terminal let's you do whatever you want.<br>
For example, you can use it to rewrite the app while it's running.<br>
Try starting with these two simple commands and let your imagination take off from there:
```
echo "app = st.text_area('Modify the running app',  open('app.py').read(), height=500)" >> app.py
echo "open('app.py', 'w').write(app)" >> app.py
```