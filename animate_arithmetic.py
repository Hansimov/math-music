from manim import *
import numpy as np
import pyaudio
import wave

# 音频参数
RATE = 44100  # 采样率
T = 2.0  # 持续时间

# 初始化音频流
p = pyaudio.PyAudio()


# 定义场景
class MathScene(Scene):
    def construct(self):
        # 初始化文本和曲线
        text = MathTex("1").scale(2).to_edge(LEFT)
        self.add(text)

        # 第一步：显示数字 1，发出 144 Hz 的声音
        self.play_sound([144])
        self.wait(T)

        # 第二步：显示加号和数字 2，发出 144 Hz 和 288 Hz 的声音
        text2 = MathTex("+", "2").scale(2).next_to(text)
        self.play(Create(text2))
        self.play_sound([144, 288])
        self.wait(T)

        # 第三步：显示数字 3，发出 432 Hz 的声音
        text3 = MathTex("3").scale(2).to_edge(LEFT)
        self.play(FadeOut(text), FadeOut(text2), Create(text3))
        self.play_sound([432])
        self.wait(T)

    def play_sound(self, freqs):
        # 计算音频数据并保存为 wav 文件
        t = np.linspace(0, T, int(T * RATE), False)
        data = np.zeros_like(t)
        for f in freqs:
            data += np.sin(f * t * 2 * np.pi)
        data /= len(freqs)

        wf = wave.open("temp.wav", "wb")
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paFloat32))
        wf.setframerate(RATE)
        wf.writeframes(data.tobytes())
        wf.close()

        # 添加音频到场景中
        self.add_sound("temp.wav")


# 运行场景
MathScene().render()

# 关闭 PyAudio 对象
p.terminate()
