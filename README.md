# Minecraft Mod Audio Conversion Tool

## 1. Introduction

The **Minecraft Mod Audio Conversion Tool** is a specialized Python-based application designed to simplify the process of converting various audio file formats to `.ogg` with single audio channels (mono) for use in **Minecraft Mods**. This tool eliminates the need for complex operations in software like Audacity, providing a quick and efficient way to standardize audio files for Minecraft modding.

## 2. Why this tool is necessary

When developing Minecraft Mods, audio files need to be in a specific format (`.ogg` and mono) to be compatible with the game. Manually converting multiple audio files using advanced tools like Audacity can be time-consuming and cumbersome. This tool provides a streamlined solution with the following features:

- **Batch Processing**: Convert multiple audio files at once.
- **Automatic Format Conversion**: Converts all audio files to `.ogg` format and ensures they are single-channel (mono).
- **Sample Rate Adjustment**: Sets all files to a sample rate of 44100 Hz, ensuring compatibility with Minecraft.
- **Optional Length Limiting and Fade-Out**: Trim audio files to a maximum length (e.g., 20 minutes) with a fade-out effect, ideal for lengthy sounds.
- **Logging**: Automatically logs each conversion, including file names and their lengths in seconds and Minecraft "ticks."

## 3. Installation

### Prerequisites

Make sure Python (version 3.6 or higher) is installed on your system. Additionally, you will need the following Python dependencies, which can be installed using `pip`:

```bash
pip install pydub
pip install ffmpeg-python
```

You also need to have `ffmpeg` installed and added to your system’s PATH. You can download `ffmpeg` from [here](https://ffmpeg.org/download.html).

### Folder Setup

Ensure your project directory is set up as follows:

```
project/
│
├── input/         # Place your raw audio files here (supports .mp3, .wav, .flac, etc.)
├── output/        # Converted .ogg files will be saved here
├── conversion_log.txt  # Log file (auto-generated)
├── main.py        # The main Python script
├── README.md      # Documentation
```

## 4. How to use the tool

### Step 1: Prepare your audio files

Place all audio files you wish to convert into the `input` folder. The tool is tested to supports the following file formats: `.mp3`, `.wav`, `.flac`, `.ogg`, `.m4a`, `.mp4`, `.wmv`, and `.xwm`. Other formats may also work. 

### Step 2: Run the conversion script

Execute the Python script `main.py` to begin the conversion process:

```bash
python main.py
```

### Step 3: Access the output files

Once the conversion is complete, you will find all converted `.ogg` files in the `output` folder. These files are now in the proper format (mono `.ogg`) for Minecraft Mod development.

### Optional: Limiting audio length

If you want to limit the length of the audio files (e.g., cutting to a maximum of 20 minutes with a fade-out effect), set the `limit_length` flag in the script to `True`. By default, it is set to `False`.

### Step 4: Review the logs for tick length. 

Each time the script runs, a log entry will be added to `conversion_log.txt`, which keeps track of file names, their lengths in seconds, and their length in Minecraft game "ticks" (20 ticks per second). **This information is needed when you create a disc item!**

## 5. License

This project is open-source under the MIT License. You are free to use, modify, and distribute the software as per the terms of the license.
