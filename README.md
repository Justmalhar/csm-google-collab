# 🧠 Sesame CSM-1B Google Colab Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Justmalhar/csm-google-collab/blob/main/Sesame_AI_CSM_Notebook.ipynb)

> **Text-to-Speech Demo using Sesame's CSM-1B Model, Gradio UI, and HuggingFace Hub**


![Demo](demo.png)


---

## 📌 Overview

This notebook demonstrates how to set up and run **Sesame's CSM-1B** Text-to-Speech model on **Google Colab** using Gradio for a browser-based UI.

- 🔊 Input: Text  
- 🎙️ Output: Realistic speech audio via pretrained TTS model  
- 🤖 Model: [`sesame/csm-1b`](https://www.google.com/search?q=site%3Ahuggingface.co+sesame%2Fcsm-1b)

---

## 🚀 Quick Start

### 🔗 Run in Google Colab  
Click the badge above to launch the notebook directly in Google Colab.

### 🧩 Steps to Execute

1. **Install Gradio and dependencies**
2. **Clone the CSM repo** and install additional Python libraries via `requirements.txt`
3. **Authenticate** with HuggingFace using `notebook_login()`
4. **Load the model** using the helper from `generator.py`
5. **Launch Gradio** with either:
   - ✅ Simple `gr.Interface`
   - 💡 Full-featured `gr.Blocks` app

---

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

## 🧪 Model Source

- **Model**: [sesame/csm-1b](https://www.google.com/search?q=site%3Ahuggingface.co+sesame%2Fcsm-1b)
- **Repository**: https://github.com/SesameAILabs/csm
- **Audio Generation**: `generator.generate()` from cloned repo

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

## 🧬 License

MIT License (for the notebook). Model license terms apply as per [HuggingFace model card](https://huggingface.co/sesame/csm-1b).
