from faster_whisper import WhisperModel
from pathlib import Path

root_dir = Path(__file__).parent.parent
models_dir = root_dir / "models"
if not models_dir.exists():
    models_dir.mkdir(parents=True)

stt_model = WhisperModel(
    "small.en", device="cpu", compute_type="int8", download_root=models_dir
)


def transcribe(audio_blob):
    transcript = ""
    segments, _ = stt_model.transcribe(audio_blob)
    for s in segments:
        transcript = f"{transcript} {s.text}"

    return transcript
