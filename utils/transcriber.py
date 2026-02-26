from faster_whisper import WhisperModel


def transcribe_audio(audio_path):
    """
    Transcribes audio using faster-whisper.
    Returns transcript text and detected language.
    """

    model = WhisperModel("small")  # small model = good balance speed/accuracy

    segments, info = model.transcribe(audio_path)

    full_text = " ".join([segment.text for segment in segments])

    return full_text, info.language