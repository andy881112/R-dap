import os
import moviepy.editor as mp

def play_videos_in_folder(path):
    # 讀取資料夾內的所有影片
    videos = [file for file in os.listdir(path) if file.endswith('.mp4')]
    # 檢查是否有影片
    if not videos:
        print("該資料夾沒影片！")
        return
    # 循環播放
    else :
        while True:
            for video in videos:
                video_path = os.path.join(path, video)
                # 載入影片
                clip = mp.VideoFileClip(video_path)
                clip = clip.resize((1920,1080))
                # 播放影片
                clip.preview()
                
if __name__ == '__main__':
    path = r'./video/' #資料夾路徑
    play_videos_in_folder(path)
