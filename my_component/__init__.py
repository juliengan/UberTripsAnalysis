import os
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "my_component",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("my_component", path=build_dir)

#bi directional component
def my_component(greeting, name, key=None):
    component_value = _component_func(greeting = greeting, name=name, key=key, default=0)
    return component_value


if not _RELEASE:
    import streamlit as st
    st.subheader("Say Hello !")
    num_clicks = my_component("What's up","Beautiful")
    st.markdown("You've clicked %s times!" % int(num_clicks))
    st.markdown("---")
    st.subheader("Chat 📱")
    greeting_input = st.text_input("Enter a greeting message",value="Hello")
    name_input = st.text_input("Enter a name", value="Jeanne")
    num_clicks = my_component(greeting_input, name_input, key="foo")
    st.markdown("You've clicked %s times!" % int(num_clicks))
