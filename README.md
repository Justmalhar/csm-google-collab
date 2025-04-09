# 🧠 Sesame CSM-1B Google Colab Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Justmalhar/csm-google-collab/blob/main/Sesame_AI_CSM_Notebook.ipynb)

> **Text-to-Speech Demo using Sesame's CSM-1B Model, Gradio UI, and HuggingFace Hub**


![Demo](demo.png)


---

## 📌 Overview

This notebook demonstrates how to set up and run **Sesame's CSM-1B** Text-to-Speech model on **Google Colab** using Gradio for a browser-based UI.

- 🔊 Text input → 🎧 audio output
- 🖥️ Simple Gradio interface
- 🧪 Experiment-ready Google Colab notebook
- 🌐 Deployed Hugging Face Space (no setup needed)
---

## 🚀 Quick Start

- ✅ Live Demo: [Hugging Face Space](https://huggingface.co/spaces/pallavi1428/seacsm)

- ⚡ Run in Colab: [Sesame_AI_CSM_Notebook.ipynb](https://colab.research.google.com/github/Justmalhar/csm-google-collab/blob/main/Sesame_AI_CSM_Notebook.ipynb)

---

## 🧩 Features

- 🤖 Model: [`sesame/csm-1b`](https://huggingface.co/sesame/csm-1b)
- 🎙️ Output: Speech via `generator.generate()`
- 🧰 Dependencies: `gradio`, `torch`, `transformers`, `huggingface_hub`, `moshi`, `silentcipher`, etc.
- 🧑‍💻 Author: [@justmalhar](https://github.com/justmalhar)

---

## 🌍 Deployment (Hugging Face)

A lightweight deployment is available here:  
🔗 https://huggingface.co/spaces/pallavi1428/seacsm

### Deployment Details

- `app.py`: Gradio app logic  
- `requirements.txt`: Minimal dependencies  
- 📱 Mobile-friendly + CPU-compatible

---

## 🧩 How It Works

1. **Install Gradio + dependencies**
2. **Clone the Sesame CSM repo**
3. **Authenticate** with Hugging Face using `notebook_login()`
4. **Load the model** with `generator.generate()`
5. **Launch Gradio UI** (choose from basic or advanced interface)

---
## 🖼️ UI Modes

### Simple Interface

```python
gr.Interface(
    fn=gradio_interface,
    inputs=[gr.Textbox(...), gr.Slider(...)],
    outputs=gr.Audio(...),
    title="Sesame CSM-1B Text-to-Speech"
).launch(share=True)
```

## 🛠️ Requirements

> All dependencies are pre-installed in the notebook via `pip install`

Main libraries:

- `gradio`
- `torch`, `torchaudio`
- `transformers`
- `huggingface_hub`
- `moshi`
- `torchtune`
- `torchao`
- `silentcipher` (from GitHub)

---
🌍 Deployment on Hugging Face
A ready-to-use deployment is hosted on Hugging Face Spaces:

👉 https://huggingface.co/spaces/pallavi1428/seacsm

📂 Files Included
app.py: Gradio application script

requirements.txt: Dependencies for deployment

✅ Deployment Features
Identical functionality to the Colab notebook

No installation needed – runs directly in the browser

Mobile-friendly UI

CPU-compatible for wider accessibility

🧬 Model Source
Model: sesame/csm-1b

Original Repo: github.com/SesameAILabs/csm

Audio Generation Code: generator.generate() from the repo


---

### Advanced Blocks UI

- 🔤 Text Input + File Upload
- 🎚️ Speaker Selector
- 🎛️ Audio Controls (play, pause, stop)
- 🔉 Volume Slider
- 🔁 Event Binding via `.click()`

---

## 🧑‍💻 Author

- 👤 Malhar Ujawane
- 🐦 [Twitter](https://x.com/justmalhar)
- 💻 [GitHub](https://github.com/justmalhar)

---

## ⚠️ Notes

- Ensure your HuggingFace account has access to the model before logging in.
- If you encounter `Model.__init__() missing required argument: 'config'`, verify model loading code inside `generator.py`.

---
-For a deployable version of this project, see (DEPLOYMENT.md).

## 🧬 License

MIT License (for the notebook). Model license terms apply as per [HuggingFace model card](https://huggingface.co/sesame/csm-1b).
