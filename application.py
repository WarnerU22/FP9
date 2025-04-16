import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env and get API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Safety check
if not api_key:
    raise ValueError("❌ API key not found. Please set OPENAI_API_KEY in your .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Function to generate completion
def get_completion():
    prompt = prompt_box.get("1.0", tk.END).strip()
    if not prompt:
        output_box.insert(tk.END, "⚠️ Please enter a prompt.\n")
        return

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content.strip()
        output_box.insert(tk.END, f"💬 {reply}\n\n")

    except Exception as e:
        output_box.insert(tk.END, f"❌ Error: {e}\n\n")

# --- GUI Setup ---
root = tk.Tk()
root.title("Mini GPT GUI")
root.geometry("600x500")

tk.Label(root, text="Enter your prompt:", font=("Arial", 12)).pack(pady=5)

prompt_box = scrolledtext.ScrolledText(root, height=6, width=70, font=("Arial", 10))
prompt_box.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=get_completion)
submit_button.pack(pady=10)

tk.Label(root, text="Response:", font=("Arial", 12)).pack()

output_box = scrolledtext.ScrolledText(root, height=15, width=70, font=("Arial", 10))
output_box.pack(pady=5)

root.mainloop()


