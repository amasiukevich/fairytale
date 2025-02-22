from dotenv import load_dotenv
from openai import OpenAI
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play, save

import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")


client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)



def create_a_story():

    FAIRYTALE_PROMPT = f"""
        Write a magical bedtime story for children with the following elements:
        - Main character: A small rabbit named Hoppy who lives in the Whispering Woods
        - Theme: Learning to be brave and make new friends
        - Story structure:
            * Hoppy is shy and afraid to play with other animals
            * One day, he discovers a lost baby bird
            * He must overcome his fears to help the bird find its way home
            * Along the way, he meets helpful forest creatures
        - Include friendly dialogue between animals
        - Add simple descriptions of the forest and its sounds
        - End with a heartwarming lesson about friendship
        - Keep the language simple and engaging for young children
        - Story should be around 100 words
    """

    client = OpenAI()
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": FAIRYTALE_PROMPT
            }
        ]
    )

    print(completion.choices[0].message)

    return completion



def narrate_story(story_text: str) -> bytes:
    """

    """
    elevenlabs_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))       

    # response = elevenlabs_client.voices.get_all()

    audio_generator = elevenlabs_client.text_to_speech.convert(
        voice_id="Se2Vw1WbHmGbBbyWTuu4",
        output_format="mp3_44100_128",
        text=story_text,
        model_id="eleven_multilingual_v2",
    )

    # audio_data = b"".join(list(audio_generator))
    # return audio_data
    return audio_generator

if __name__ == "__main__":

    response = create_a_story()
    story_text = response.choices[0].message.content
    
    narration = narrate_story(story_text)

    # Save the audio file
    output_path = "stories/story_narration.mp3"
    save(narration, output_path)

    play(narration)
    


