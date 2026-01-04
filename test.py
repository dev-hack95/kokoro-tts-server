import requests
import sounddevice as sd
import numpy as np
import io
import wave
import time


SERVER_URL = "http://localhost:8880"

def play_streaming_realtime():
    """Stream and play audio in real-time (lowest latency)"""
    print("Real-time streaming playback...")
    
    text = """Mara had always found comfort in the quiet rhythm of the archive's marble corridors, the scent of old paper and the soft click of her footsteps echoing off the high, vaulted ceilings. Her days were a measured procession of cataloguing forgotten letters, sorting brittle manuscripts, and preserving the fragile histories that had survived the ravages of time. To her, the archive was more than a place of work; it was a sanctuary where the past spoke in hushed tones, and every stack of books felt like a living organism. The archivists, a close-knit group of scholars and caretakers, shared a quiet camaraderie, and the archive itself seemed to exhale a sense of reverence. Mara's routine had never been disrupted by anything that would challenge the delicate equilibrium she had cultivated. Yet, as the autumn light filtered through the stained-glass windows and painted patterns across the polished floor, an unusual file caught her eye—a slim, unmarked volume tucked behind a stack of botanical illustrations. It was bound in a deep blue leather that seemed almost too vivid to be real, and when she ran her fingers over its surface, she felt a strange, almost electric pull. Curiosity, a quiet companion she had rarely allowed herself, stirred within her, whispering that perhaps some hidden story lay waiting to be uncovered.

When Mara slid the volume from the shelf, she found a thin sheet of parchment inside—a map, but not one she had seen before. The parchment was tattered at the edges, and ink lines had faded into a ghostly pale, yet a faint outline of a coastline was still discernible. The map seemed to depict an archipelago that did not exist on any modern charts, a cluster of islands scattered across a sea that looked like a reflection of the sky at dusk. In the center of the map, a single dot marked an island named 'Elias.' The island's shape was irregular, almost like a hand held in a closed fist, and beneath the dot was an inscription in a script that looked both familiar and alien: 'Sic mundus, sic historia.' Mara had never heard of this phrase, but it resonated with her on some deep, inexplicable level. The map didn't just show a place; it seemed to hint at a hidden truth. She could not shake the feeling that the archive had concealed this for a reason, and that the truth she was about to uncover could change the way she saw history forever.

Over the next few days, Mara poured over the map, comparing its outlines with satellite imagery and ancient navigation logs she had catalogued. The more she studied, the more she realized that the island, as described, did not exist in any known records. The map seemed to be a key, perhaps leading to a place that had slipped between the cracks of time. She felt a sudden surge of excitement, tempered by a professional caution that reminded her of the responsibilities she carried. Yet, the archive, her sanctuary, also housed countless mysteries that had never been solved. The thought of uncovering another one tugged at her. She decided, with a decisive nod to herself, that she would follow the map. She began to plan a trip to a coastal town that, according to the map's coordinates, lay at the edge of the known world, where the sea met the land in a place where legends were born and stories were lost.

The town she chose was called Valen, a small fishing village perched on a cliff overlooking a sea that shone like liquid glass. The locals spoke of a forgotten island that appeared only once every hundred years, an island that was said to be the keeper of ancient knowledge. Mara arrived at Valen on a crisp morning, the sky a pale blue that mirrored the sea below. The streets were narrow and lined with stone cottages, and the air was thick with the scent of salt and fish. She was greeted by the village elder, a gaunt man with silver hair, who looked at her with an air of wary curiosity. 'You seek the island, do you?' he asked, his voice rough as the waves. Mara nodded, explaining her mission in quiet terms, her mind racing with images of hidden doors and forgotten histories. The elder gave her a small, crinkled map that had been passed down through generations, and as he handed it to her, he whispered, 'Beware the tides, for they hold the truth you seek.'

Mara set off on a small boat at dawn, the wind tugging at her coat as she navigated toward the coordinates marked on the map. The sea was calm, and the sky was a clear, unblemished blue. As she approached the coordinates, the water grew darker and colder, as if the sea itself were breathing a sigh. Then, a sudden shift in the water's surface revealed a landmass—an island that matched the map's shape, a jagged silhouette of cliffs and green valleys hidden within a cloud of mist. She anchored her boat and stepped onto the shore, feeling the sand cool beneath her boots. The island was indeed a place out of time, a place that seemed to exist between reality and myth. The forest that rose from the shore was dense and thick, the trees towering high into the sky, and the air was heavy with an ancient, earthy perfume. The map's ink lines glowed faintly in the dusk, guiding her deeper into the island's heart.

Mara's footsteps echoed through the forest, and she soon found herself at the base of a massive stone structure that seemed to have been carved by the hands of an unknown civilization. The structure was a library, its walls made of weathered stone, covered in vines that clung like living ivy. The entrance was hidden behind a curtain of moss and a loose stone door. Mara pressed the stone with her palm, and the door creaked open, revealing an interior that was dimly lit by shafts of light that filtered through the canopy. Inside, the library was vast, with rows upon rows of wooden shelves that stretched into the darkness. The books and scrolls that lined these shelves were bound in leather and cloth, each one bearing a title that seemed to whisper the secrets of the world. A sense of awe flooded her as she walked further, her eyes drawn to a particular shelf that seemed to pulse with a faint, golden glow.

On that glowing shelf, Mara found a small, silver key, its design intricate and almost otherworldly. The key had a symbol etched along its shaft—a stylized representation of a compass rose, but with an additional star at its center. The moment she touched the key, a surge of heat and cold ran through her body, and she felt as though the key had become a conduit, a bridge between her and something beyond the library's walls. She clutched the key to her chest, and her mind filled with questions: What would it unlock? What hidden door or vault lay behind the walls of the library? She knew she had to find out. The key glowed brighter, as if it were reacting to her presence. Her heartbeat quickened, and she felt a sense of destiny tugging her toward the heart of the building.

Mara followed the faint glow to the center of the library, where a massive stone door stood, its surface etched with symbols that pulsed in a rhythm that matched her breathing. The door seemed to be a threshold, a portal between the known world and another realm of knowledge. She pressed the key into the lock, and the door began to open with a grinding sound that echoed through the library. As the door opened, a faint light spilled out, revealing a vault beneath the library. The vault was a chamber carved into the earth, its walls lined with ancient stone tablets that glowed with a soft, amber light. The air was thick with an ancient, earthy perfume, and the sound of distant wind echoed in the chamber. Mara felt as if she had stepped into the heart of the island, where all the secrets of history were kept.

Inside the vault, Mara found a single object at its center: a crystal orb that shimmered with an inner light. The orb seemed to contain the memory of the entire island, as if it held the thoughts and feelings of every person that had ever lived there. It was an artifact of immense power, a relic that had been hidden away to protect humanity from the knowledge it contained. The orb pulsed gently, as if it were breathing, and a voice, faint and ancient, began to speak to Mara. It told her that the island had been a sanctuary for those who had the courage to seek knowledge beyond the veil of reality. It told her that the map had been a test, a way to find those who were worthy to receive the knowledge that lay beyond the vault. The orb told her that she had been chosen, and that she was the first to uncover the secrets of the island. With a sense of awe and wonder, she listened to the voice as it spoke of the world beyond the veil and of the responsibility that came with such knowledge.

Mara's mind was a whirlwind of thoughts. She had spent years preserving the past, cataloguing the fragments of history that had survived. She had never imagined that she might be the one to bring them back to life. The orb offered her the chance to rewrite history, to bring knowledge that had been lost, to bring the truth to those who had forgotten. The voice urged her to take the orb and use its power to heal the wounds of the past, to mend the scars of humanity. She could use it to reveal the truth of the tragedies that had shaped the world. She could bring an end to the wars that had ravaged the world. She could bring peace, and she could bring a new era of knowledge and understanding. The world would become a different world. But she thought about the consequences. She would be carrying the weight of the knowledge and the responsibility that came with it.

Mara felt her heart beating faster, and she realized that she was standing at a crossroads. She could take the orb and use it to change the world, or she could leave it where it was, letting the secrets remain hidden. The voice in the orb warned her that any misuse of its power would bring disaster. The orb was a gift, but it was also a burden. She had to decide. She looked at the orb, its light dancing across her face, and she saw the reflection of all the histories she had preserved. She thought about the lives she had saved, the stories she had brought back to life, and the people who had come to her with their secrets. She realized that the knowledge she had preserved had become more than a collection of words; it had become a living entity that was now ready to be set free. The decision weighed heavily, but she felt a sense of resolve build inside her.

In the end, Mara chose to leave the orb in the vault, to keep the island's secrets hidden. She returned to the library and locked the heavy door with the key that had unlocked it. The library's walls seemed to breathe as if it was breathing a sigh of relief. She knew that the knowledge was too powerful to be wielded by any one person, and that the world was not yet ready to receive it. She decided to remain the guardian of the archive, to watch over the secrets she had found, and to keep them safe for future generations. She wrote a detailed note in the journal of the library, explaining everything she had discovered, and she sealed it inside a hidden, iron box. She left the key under the stone door, so that one day, someone else would find it and become the next guardian of the island. She went back to her work, cataloguing the histories she had once believed were lost, knowing that she would continue to preserve them for those who would one day seek the truth.

Mara's return to her daily routine was not an ordinary one. The quiet corridors of the archive now felt like an echo of the island, and she could feel the presence of the secret that she had left behind. She spent her days cataloguing the histories that had survived, but her mind was constantly drawn to the map and the island. She could not shake the feeling that the island's secrets were waiting for someone else to uncover them. Her thoughts drifted to the future, to the day when someone else would stumble upon the key and unlock the vault. She felt a sense of hope that the knowledge that lay hidden would one day be used for good. She also felt a sense of responsibility, knowing that the knowledge could bring both great power and great danger. In her heart, she knew that she had done the right thing, and that the archive would remain a sanctuary for all those who sought knowledge.

Months turned into years, and the archive grew with new discoveries. Mara watched as new scholars entered the archives, each with their own questions and dreams. She shared her story with those who were ready to hear it, but she did so with caution, knowing that the knowledge she had left behind was not meant for the unprepared. She kept her secret, her map, and her key hidden in a place only she knew, a place that she guarded with her life. Her legend grew, and people whispered stories about the archivist who had found a hidden island of knowledge. Her story became a legend, and the archive became a place where the past was kept safe and the future was always a possibility. The archive was no longer a silent sanctuary; it was a living memory, a place where history could be discovered and preserved for the next generation.

In the quiet of the archive, after the last visitor had left, Mara would sometimes look at the blue leather map that lay in the center of the desk. Its edges had frayed, but the ink lines still glowed faintly. She would close her eyes and imagine the island, the library, and the crystal orb that held the memory of all those who had lived there. She would think of the choice she had made, the knowledge she had left behind, and the future that was yet to unfold. In her mind, she could hear the island's whisper, telling her that she was not alone. The knowledge she had preserved was not just a collection of facts; it was a living, breathing entity that would one day find its way to a new guardian. She smiled, knowing that the archive would continue to hold its secrets until the day that someone else would be ready to hear the island's story. And until that day, Mara would keep the archive's silence, the history, and the hope alive, one book at a time.
    """
    
    response = requests.post(
        f"{SERVER_URL}/tts/stream/raw",
        params={
            "text": text,
            "voice": "af_sky",
            "speed": 0.9,
            "lang": "en-us"
        },
        stream=True
    )
    
    if response.status_code == 200:
        sample_rate = int(response.headers.get('X-Sample-Rate', 24000))
        stream = sd.OutputStream(
            samplerate=sample_rate,
            channels=1,
            dtype=np.float32
        )
        
        chunk_count = 0
        start_time = time.time()
        
        with stream:
            for chunk in response.iter_content(chunk_size=4096):
                print(chunk)
                if chunk:
                    chunk_count += 1
                    audio_chunk = np.frombuffer(chunk, dtype=np.int16).astype(np.float32) / 32767.0
                    
                    stream.write(audio_chunk)
                    
                    if chunk_count == 1:
                        print(f"First chunk played at {time.time() - start_time:.3f}s (latency)")
        
        print(f"Playback complete - {chunk_count} chunks in {time.time() - start_time:.2f}s")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def play_streaming_wav():
    print("Streaming WAV audio...")
    
    response = requests.post(
        f"{SERVER_URL}/tts/stream",
        params={
            "text": "This is a streaming WAV test. Audio is generated in real-time chunks.",
            "voice": "af_sarah",
            "speed": 1.0,
            "lang": "en-us"
        },
        stream=True
    )
    
    if response.status_code == 200:
        audio_data = b""
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                audio_data += chunk
        
        wav_file = io.BytesIO(audio_data)
        with wave.open(wav_file, 'rb') as wf:
            sample_rate = wf.getframerate()
            audio_bytes = wf.readframes(wf.getnframes())
            audio_array = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32) / 32767.0
            
            print(f"Playing: {len(audio_array)} samples at {sample_rate} Hz")
            sd.play(audio_array, sample_rate)
            sd.wait()
    else:
        print(f"Error: {response.status_code}")

def play_non_streaming():
    """Traditional non-streaming approach"""
    print("Non-streaming audio (complete generation)...")
    
    start_time = time.time()
    
    response = requests.post(
        f"{SERVER_URL}/tts",
        params={
            "text": "This is non-streaming audio. The entire file is generated before playback starts.",
            "voice": "am_adam",
            "speed": 1.0,
            "lang": "en-us"
        }
    )
    
    generation_time = time.time() - start_time
    
    if response.status_code == 200:
        with open("output.wav", "wb") as f:
            f.write(response.content)
        
        print(f"Generated in {generation_time:.2f}s")

        wav_file = io.BytesIO(response.content)
        with wave.open(wav_file, 'rb') as wf:
            sample_rate = wf.getframerate()
            audio_bytes = wf.readframes(wf.getnframes())
            audio_array = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32) / 32767.0
            
            duration = len(audio_array) / sample_rate
            print(f"Playing {duration:.2f}s of audio...")
            sd.play(audio_array, sample_rate)
            sd.wait()
    else:
        print(f"Error: {response.status_code}")

def server_side_playback():
    """Let server play the audio (server must have audio output)"""
    print("Server-side streaming playback...")
    
    text = """
    Despite it looking as though the storm is slowly moving eastwards, 
    the situation in Kansas and Missouri remains serious.
    """
    
    response = requests.post(
        f"{SERVER_URL}/tts/play",
        params={
            "text": text,
            "voice": "bf_emma",
            "speed": 1.0,
            "lang": "en-us"
        }
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"Server response: {result}")
    else:
        print(f"Error: {response.status_code}")



if __name__ == "__main__":
    print("=== Kokoro-ONNX TTS Streaming Client ===\n")
    
    print("\n" + "="*50)
    print("1. Real-time streaming (LOWEST LATENCY):")
    print("="*50)
    play_streaming_realtime()