import pyaudio
import wave

def record_sound_from_pcm(pcm_file_path =  "/home/mrplastic/桌面/SR2.2-HR1.1.3/vvui/audio/mic_demo_vvui_deno.pcm", sample_rate=44100, channels=2, bit_depth=16):
    CHUNK = 1024

    # Read PCM file
    wf = wave.open(pcm_file_path, 'rb')
    wf.setnchannels(channels)
    wf.setsampwidth(bit_depth // 8)
    wf.setframerate(sample_rate)
    
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    print("偵測聲音中")

    while len(data) > 0:
        stream.write(data)
        data_chunk = array('h', data)
        vol = max(data_chunk)
        if vol >= 500:
            r = sr.Recognizer()
            with sr.AudioFile(pcm_file_path) as source:
                print("開始說話")
                audio = r.listen(source)
                print("關鍵字偵測結束")
            try:
                recognize = r.recognize_google(audio, language='zh-tw')
                print("辨識結果：", recognize)
                if "Siri" in recognize:
                    with sr.AudioFile(pcm_file_path) as source:
                        print("關鍵字觸發成功，請說話")
                        audio = r.listen(source)
                        try:
                            recognize = r.recognize_google(audio, language='zh-tw')
                            print("", recognize)
                            print()
                            if "溫度" in recognize:
                                print("Hello World！")
                        except:
                            break
                    break
                else:
                    break
            except:
                break

        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()
    p.terminate()

while True:
    # 请将PCM文件名替换成你想要使用的文件名，确保该文件在当前工作目录下
    pcm_file_path = "your_pcm_file.pcm"
    record_sound_from_pcm(pcm_file_path)
