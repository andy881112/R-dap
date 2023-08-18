import speech_recognition as sr

def pcm_to_text(pcm_file_path):
    # 讀取PCM檔案
    with open(pcm_file_path, 'rb') as pcm_file:
        audio_data = pcm_file.read()

    # 使用CMU Sphinx進行語音轉文字
    recognizer = sr.Recognizer()
    try:
        # 轉換語音為文字
        text = recognizer.recognize_sphinx(audio_data, language='zh-TW') # 這裡使用了繁體中文
        return text
    except sr.UnknownValueError:
        return "無法辨識語音"
    except sr.RequestError:
        return "無法連接到語音辨識服務"

# 要轉換的PCM檔案路徑
pcm_file_path = '北北基放颱風假「桃園沒」 張善政fb被灌爆｜TVBS新聞.pcm'
result = pcm_to_text(pcm_file_path)
print(result)
