from pydub import AudioSegment
import os

# 获取当前脚本文件的目录
current_directory = os.path.dirname(os.path.realpath(__file__))

# 构建到 input 和 output 文件夹的路径
input_folder = os.path.join(current_directory, 'input')
output_folder = os.path.join(current_directory, 'output')

sample_rate = 44100

# 创建 output 文件夹，如果它不存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历 input 文件夹中的所有文件
for file_name in os.listdir(input_folder):
    if file_name.endswith(('.mp3', '.wav', '.flac')):
        file_path = os.path.join(input_folder, file_name)
        output_file_name = os.path.splitext(file_name)[0] + '.ogg'
        output_file_path = os.path.join(output_folder, output_file_name)

        audio = AudioSegment.from_file(file_path)
        mono_audio = audio.set_channels(1)  # 转换为单轨
        mono_audio = mono_audio.set_frame_rate(sample_rate)  # 设置采样率

        # 导出为 OGG 格式
        mono_audio.export(output_file_path, format='ogg')

print("Conversion completed!")
