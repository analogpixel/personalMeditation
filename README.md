# ChatGPT Meditation Script Generator

This project provides a script to generate guided meditation scripts using ChatGPT (Version 4) and converts them into a fully narrated mp3 file. The user can specify the type of meditation they're interested in, for instance, focusing on improving cookie making skills. The generated meditation script will then be rendered as an mp3 audio file which layers the spoken script at the correct times , with backing music and any other sound effects you wanted added during the session.

## Features

- Uses ChatGPT v4 to generate custom meditation scripts based on user preferences.
- Conversion of meditation scripts to mp3 audio files.
- Allows users to specify the focus of their meditation.

## Prerequisites

To use this program, you'll need:

- Access to ChatGPT (v4 or higher recommended)
- An API key from [Eleven Labs](https://beta.elevenlabs.io) (A free trial is sufficient for generating a few prompts)
- your own backing track `backing_track.mp3` for the music that plays in the background

## Usage

1. Start with the provided include prompt for ChatGPT v4. [gpt_prompt txt](gpt_prompt.txt)
2. Modify the top of the prompt to specify the type of meditation you desire. The more specific, the better. For instance, if you want a meditation to improve your cookie making skills, specify this in the sample prompt.
3. After obtaining the output from ChatGPT, execute the `render_meditation.py <filename.yaml>` script. This script will process your meditation script and generate an mp3 file for your use.

## Output

The program will output a fully narrated mp3 file of your custom meditation script.

## Notes

Please note that the accuracy and relevance of the meditation script will highly depend on the clarity and specificity of your initial prompt. Also, the number of meditation scripts you can generate during the free trial on Eleven Labs is limited.

## Contributions

Feel free to fork this project, make changes, and open pull requests. We appreciate your contributions and suggestions to improve this script.

## Disclaimer

This project is not affiliated with, maintained, authorized, endorsed, or sponsored by OpenAI or any of its affiliates. It is an independent project that utilizes the ChatGPT model.

## License

MIT

## Contact

If you have any questions, feel free to open an issue or contact us directly. We'll be happy to help.
