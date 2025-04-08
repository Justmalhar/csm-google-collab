# app.py
import os 
import subprocess
import sys

# Clone the repository if it doesn't exist
if not os.path.exists("csm"):
    subprocess.run(["git", "clone", "https://github.com/SesameAILabs/csm.git"], check=True)
sys.path.insert(0, "csm")  # Make sure Python can find the module


from huggingface_hub import login
from generator import load_csm_1b
import gradio as gr
import torchaudio

# --- Setup ---
sys.path.append("csm")  # Ensure `csm` repo is accessible
login(token=os.environ["sea"], add_to_git_credential=True)  # Secure login
generator = load_csm_1b(device="cpu")  # Force CPU for Hugging Face Spaces

# --- Audio Generation ---
def generate_audio(text, speaker=0):
    audio = generator.generate(
        text=text,
        speaker=speaker,
        context=[],
        max_audio_length_ms=10_000,
    )
    output_file = "output_audio.wav"
    torchaudio.save(output_file, audio.unsqueeze(0).cpu(), generator.sample_rate)
    return output_file

# --- Gradio Interface (FULL UI from your notebook) ---
with gr.Blocks(title="Sesame CSM-1B Text-to-Speech") as demo:
    gr.Markdown("# 🎙️ Sesame CSM-1B Text-to-Speech")
    gr.Markdown("Generate high-quality audio from text using the Sesame CSM-1B model.")

    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(label="Enter Text", placeholder="Type your text here...", lines=5)
            speaker_input = gr.Number(
                label="Speaker ID (0-1000)",
                value=0,
                minimum=0,
                maximum=1000,  # Fixed max to 1000 (from your notebook)
                interactive=True
            )
            file_upload = gr.File(label="Or Upload a Text File", file_types=[".txt"])
            generate_button = gr.Button("Generate Audio 🎵")

        with gr.Column():
            audio_output = gr.Audio(label="Generated Audio", interactive=False)
            with gr.Row():
                play_button = gr.Button("▶️ Play")
                pause_button = gr.Button("⏸️ Pause")
                stop_button = gr.Button("⏹️ Stop")
            volume_slider = gr.Slider(minimum=0, maximum=100, value=50, label="Volume")

    # Store audio state (for playback controls)
    audio_state = gr.State(value=None)

    # --- Core Logic ---
    def process_input(text, file, speaker_id):
        if file:
            with open(file.name, "r") as f:
                text = f.read()
        speaker_id = max(0, min(int(speaker_id), 1000))  # Clamp to 0-1000
        audio_file = generate_audio(text, speaker_id)
        return audio_file, audio_file  # Output + state

    # --- Playback Controls (placeholders) ---
    # Note: Gradio's Audio component handles playback natively.
    # These buttons are cosmetic but kept for UI consistency.
    def play_audio(audio_state):
        return audio_state if audio_state else None

    def pause_audio():
        return None

    def stop_audio():
        return None

    # --- Event Bindings ---
    generate_button.click(
        fn=process_input,
        inputs=[text_input, file_upload, speaker_input],
        outputs=[audio_output, audio_state]
    )
    play_button.click(fn=play_audio, inputs=audio_state, outputs=audio_output)
    pause_button.click(fn=pause_audio, outputs=audio_output)
    stop_button.click(fn=stop_audio, outputs=audio_output)

demo.launch()