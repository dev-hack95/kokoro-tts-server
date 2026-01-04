import io
import wave
import uvicorn
import numpy as np
import onnxruntime as ort
from kokoro_onnx import Kokoro
from audio.stream import StreamGenerator
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, Response


app = FastAPI()

sess_options = ort.get_available_providers()
providers = [
    ('ROCMExecutionProvider', {
        'device_id': 0,
    }),
    'CPUExecutionProvider'
]

kokoro = Kokoro(
    "models/kokoro-v1.0.onnx", 
    "models/voices-v1.0.bin"
)

stream_client = StreamGenerator(kokoro=kokoro)


@app.get("/")
async def root():
    return {
        "status": "Kokoro TTS Server Running on AMD GPU with Streaming",
        "version": "kokoro_onnx"
    }

@app.post("/tts")
async def generate_speech(text: str, voice: str = "af_sarah", speed: float = 1.0, lang: str = "en-us"):
    try:
        samples, sample_rate = await kokoro.create(text, voice=voice, speed=speed, lang=lang)
        
        buffer = io.BytesIO()
        with wave.open(buffer, 'wb') as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(sample_rate)
            audio_int16 = (samples * 32767).astype(np.int16)
            wav_file.writeframes(audio_int16.tobytes())
        
        buffer.seek(0)
        return Response(
            content=buffer.read(),
            media_type="audio/wav",
            headers={"Content-Disposition": "attachment; filename=speech.wav"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/tts/stream")
async def stream_speech(text: str, voice: str = "af_sarah", speed: float = 1.0, lang: str = "en-us"):
    return StreamingResponse(
        stream_client.stream_audio_chunks(text, voice, speed, lang),
        media_type="audio/wav",
        headers={
            "Content-Disposition": "inline; filename=speech.wav",
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no"
        }
    )

@app.post("/tts/stream/raw")
async def stream_raw_audio(text: str, voice: str = "af_sarah", speed: float = 1.0, lang: str = "en-us"):
    return StreamingResponse(
        stream_client.stream_raw_pcm(text, voice, speed, lang),
        media_type="audio/pcm",
        headers={
            "Content-Disposition": "inline",
            "X-Sample-Rate": "24000",
            "X-Channels": "1",
            "X-Bit-Depth": "16",
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no"
        }
    )


@app.get("/voices")
async def list_voices():
    voices = [
        "af_sarah", "af_nicole", "af_sky", "af_bella", "af_jessica", "af_heart",
        "am_adam", "am_michael", 
        "bf_emma", "bf_isabella", "bf_lily",
        "bm_george", "bm_lewis"
    ]
    return {
        "voices": voices
        }

@app.get("/health")
async def health_check():
    return {
        "status": "OK"
    }

if __name__ == "__main__":
    print("Available ONNX Runtime providers:", ort.get_available_providers())
    
    uvicorn.run(app, host="0.0.0.0", port=8880)