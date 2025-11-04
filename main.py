from gtts import gTTS
import os


def textfile_to_audio(input_file='conan.txt', lang='en', output_file='output.mp3'):
    """
    Read text from a file and convert it to audio (MP3).

    Args:
        input_file (str): Path to the text file.
        lang (str): Language code, e.g., 'en', 'zh-CN', 'es', etc.
        output_file (str): Output audio file name.
    """
    try:
        # Read text content
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read().strip()

        if not text:
            print("❌ The file is empty!")
            return

        # Convert text to speech
        tts = gTTS(text=text, lang=lang)
        tts.save(output_file)
        print(f"✅ Audio saved as '{output_file}'")

        # Play audio automatically
        if os.name == 'posix':
            os.system(f"open {output_file}")  # macOS
        elif os.name == 'nt':
            os.system(f"start {output_file}")  # Windows

    except FileNotFoundError:
        print(f"❌ File not found: {input_file}")
    except Exception as e:
        print("❌ Error:", e)


# Example usage
if __name__ == "__main__":
    textfile_to_audio('input.txt', lang='en', output_file='output.mp3')
