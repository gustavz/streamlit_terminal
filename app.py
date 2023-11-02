import subprocess

import streamlit as st

# Initialize session state variables
SESSION_DEFAULTS = dict(
    terminal_history=[],
)
for k, v in SESSION_DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

st.set_page_config(page_title="Insecure Streamlit Terminal", layout="centered")
st.title("Insecure Streamlit Terminal")
st.warning(
    """
⚠️ Security Warning: This app allows execution of arbitrary commands which can be used to compromise your system. 
Never run this in a production environment or on a system with sensitive data. 
Always use within a secure, controlled environment and only with trusted users.
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


def generate_terminal_output():
    output = []
    for element in reversed(st.session_state.terminal_history):
        output.append(f"> {element['command']}")
        if element["stdout"]:
            output.append(f"{element['stdout']}")
        if element["stderr"]:
            output.append(f"{element['stderr']}")
    return "\n".join(output)


command = st.text_input(
    label="Shell Command",
    placeholder="Type your command here and press enter. Chain commands with '&&' as the terminal is stateless.",
)

if command:
    stdout, stderr = run_shell_command(command)
    st.session_state.terminal_history.append(
        {"command": command, "stdout": stdout, "stderr": stderr}
    )
    st.text_area("Terminal Log", value=generate_terminal_output(), height=400)
