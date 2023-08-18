from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def wav_to_pcm(wav_file, pcm_file):
    sound = AudioSegment.from_file(wav_file, format="wav")
    sound.export(pcm_file, format="s16le")
def mp4_to_pcm(mp4_file, pcm_file):
    clip = VideoFileClip(mp4_file)
    clip.audio.write_audiofile(pcm_file)

def main():
    mp4_file = "北北基放颱風假「桃園沒」 張善政fb被灌爆｜TVBS新聞.mp4"
    wav_file = "output.wav"
    pcm_file = "output.pcm"

    mp4_to_pcm(mp4_file, wav_file)
    wav_to_pcm(wav_file, pcm_file)

if __name__ == "__main__":
    main()
