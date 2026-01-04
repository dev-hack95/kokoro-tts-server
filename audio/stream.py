import io
import wave
import numpy as np
from kokoro_onnx import Kokoro


class StreamGenerator:
    def __init__(self, kokoro: Kokoro):
        self.client = kokoro

    async def stream_raw_pcm(
            self,
            text: str, voice: str = "af_sarah", 
            speed: float = 1.0, lang: str = "en-us"
            ):
        try:
            stream = self.client.create_stream(text, voice=voice, speed=speed, lang=lang)
        
            async for samples, sample_rate in stream:
                audio_int16 = (samples * 32767).astype(np.int16)
                yield audio_int16.tobytes()
            
        except Exception as e:
            print(f"Error in raw PCM streaming: {e}")
            raise
        
    async def stream_audio_chunks(
            self,
            text: str, voice: str = "af_sarah", 
            speed: float = 1.0, lang: str = "en-us"
            ):
        try:
            stream = self.client.create_stream(text, voice=voice, speed=speed, lang=lang)
        
            is_first_chunk = True
            sample_rate = None
        
            async for samples, sr in stream:
                sample_rate = sr
            
                audio_int16 = (samples * 32767).astype(np.int16)
            
                if is_first_chunk:
                    buffer = io.BytesIO()
                    with wave.open(buffer, 'wb') as wav_file:
                        wav_file.setnchannels(1)
                        wav_file.setsampwidth(2)
                        wav_file.setframerate(sample_rate)
                        wav_file.writeframes(audio_int16.tobytes())
                
                    buffer.seek(0)
                    yield buffer.read()
                    is_first_chunk = False
                else:
                    yield audio_int16.tobytes()
                
        except Exception as e:
            print(f"Error in audio streaming: {e}")
            raise
