import gradio as gr
def welcome_message(name):
    return f"Welcome, {name}!"
iface = gr.Interface(fn=welcome_message, inputs="text", outputs="text", title="Welcome App")
if __name__ == "__main__":
    iface.launch()