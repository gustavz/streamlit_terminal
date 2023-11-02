import subprocess

import streamlit as st


SESSION_DEFAULTS = dict(
    terminal_log=[],
)
for k, v in SESSION_DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

HELP = """
This unrestricted terminal let's you do whatever you want.
For example, you can use it to rewrite the app while it's running.
Try starting with these two simple commands and let your imagination take off from there:
```
echo "app = st.text_area('Modify the running app',  open('app.py').read(), height=500)" >> app.py
echo "open('app.py', 'w').write(app)" >> app.py
```
"""

st.set_page_config(page_title="Insecure Streamlit Terminal", layout="centered")
st.title("Insecure Streamlit Terminal")
st.warning(
    """
⚠️ Security Warning: This app allows execution of arbitrary commands which can be used to compromise your system. 
Never run this in a production environment or on a system with sensitive data. 
Always use within a secure, controlled environment and only with trusted users.

This is a hosted terminal with internet access. The possibilties are endless. Use with caution.
"""
)


def run_shell_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return e.stdout, e.stderr


def generate_terminal_log_string():
    output = []
    for element in reversed(st.session_state.terminal_log):
        output.append(f"> {element['command']}")
        if element["stdout"]:
            output.append(f"{element['stdout']}")
        if element["stderr"]:
            output.append(f"{element['stderr']}")
    return "\n".join(output)


command = st.text_input(
    label="Shell Command",
    placeholder="Type your command here and press enter. Chain commands with '&&' as the terminal is stateless.",
    help=HELP,
)

if command:
    stdout, stderr = run_shell_command(command)
    log = {"command": command, "stdout": stdout, "stderr": stderr}
    print(log)
    st.session_state.terminal_log.append(log)
    st.text_area("Terminal Log", value=generate_terminal_log_string(), height=400)
