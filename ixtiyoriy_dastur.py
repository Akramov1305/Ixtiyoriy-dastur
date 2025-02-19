# -*- coding: utf-8 -*-
"""Ixtiyoriy dastur

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1plQCxW0bRFpZnUR_7Gm0ipwFNkWy20_H
"""

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("1655351678_32-furman-top-p-ronaldo-oboi-38.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("robert-lewandowski-fc-barcelona-2024-25-1730103967-152589.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("Messi-Inter-Miami-hubpage_v2-4b134ac84a3d1ddc5c023f61ad832659.webp")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("kaka-ac-milan-24-1511513149.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("01ja8g7vsyy718t4qq8r.webp")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("zlatan-ibrahimovic-paris-saint-germain-psg_3450181.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

import pandas as pd
df = pd.read_excel("Futbol.xlsx")
print(df.head())

import pandas as pd
df = pd.read_excel("Futbol.xlsx")

yoshdan_kichiklar = df[df['Yoshi'] < 40]

print(yoshdan_kichiklar)

import pandas as pd
df = pd.read_excel("Futbol.xlsx")

yoshdan_kichiklar = df[df['Yoshi'] > 40]

print(yoshdan_kichiklar)

from google.colab.patches import cv2_imshow
import cv2

def Akramov_futbol(belgi):
    if belgi == "goat":
        rasm = cv2.imread("Krishtianu_Ronaldu_Al_Nasr_Getty_Images2_2c913c3124.webp")
        if rasm is not None:
            cv2_imshow(rasm)
        else:
            print("Rasm topilmadi.")
    else:
        return "Transfer qiling"

belgi = input("Belgini kiriting: ")
natija = Akramov_futbol(belgi)
print(natija)

import matplotlib.pyplot as plt
import numpy as np

years = np.array([2016, 2017, 2018, 2019, 2020, 2021])
goals = np.array([55, 53, 49, 45, 41, 47])

plt.plot(years, goals, marker='o', color='red', label='Gollar')

plt.title("Cristiano Ronaldoning Yillik Gollari")
plt.xlabel("Yillar")
plt.ylabel("Gollar soni")
plt.grid(True)
plt.legend()

plt.show()

import matplotlib.pyplot as plt
import numpy as np

years = np.array([2016, 2017, 2018, 2019, 2020, 2021])
goals = np.array([51, 54, 45, 50, 31, 38])

plt.plot(years, goals, marker='o', color='red', label='Gollar')

plt.title("Lionel Messining Yillik Gollari")
plt.xlabel("Yillar")
plt.ylabel("Gollar soni")
plt.grid(True)
plt.legend()

plt.show()

import matplotlib.pyplot as plt
import numpy as np

years = np.array([2016, 2017, 2018, 2019, 2020, 2021])
goals = np.array([50, 28, 22, 31, 16, 20])

plt.plot(years, goals, marker='o', color='gold', label='Gollar')

plt.title("Zlatan Ibrahimovichning Yillik Gollari")
plt.xlabel("Yillar")
plt.ylabel("Gollar soni")
plt.grid(True)
plt.legend()

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    sample_rate, data = wavfile.read(wav_file)

    if len(data.shape) > 1:
        data = data[:, 0]

    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)
    plt.ylim(0, sample_rate / 2)
    plt.grid(True)
    plt.show()
wav_file_path = 'bubbles_sfx.wav'
generate_spectrogram(wav_file_path)

!pip install gtts

from gtts import gTTS
import os

text = " Cristiano Ronaldo is a Portuguese football legend, born on February 5, 1985, in Madeira, Portugal. Renowned for his incredible skill, athleticism, and work ethic, he is one of the greatest players in football history. Career Highlights: Manchester United (2003–2009, 2021–2022): Won 3 Premier League titles and a Champions League. Real Madrid (2009–2018): Scored 450 goals, won 4 Champions League titles, and 4 Ballon d'Ors. Juventus (2018–2021): Won 2 Serie A titles. Portugal: Won Euro 2016 and the Nations League 2019. All-time leading scorer in international football. Ronaldo has won 5 Ballon d’Ors and holds records for the most goals in the Champions League and international football. Beyond the pitch, he is a philanthropist and global icon with the famous CR7 brand."
language = 'en'
tts = gTTS(text=text, lang=language, slow=False)

audio_file = "output.mp3"
tts.save(audio_file)

from IPython.display import Audio
Audio(audio_file)

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    sample_rate, data = wavfile.read(wav_file)

    if len(data.shape) > 1:
        data = data[:, 0]

    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)
    plt.ylim(0, sample_rate / 2)
    plt.grid(True)
    plt.show()
wav_file_path = 'mixkit-classic-alarm-995.wav'
generate_spectrogram(wav_file_path)

!pip install gtts

from gtts import gTTS
import os

text = " Lionel Messi is an Argentine football superstar, born on June 24, 1987, in Rosario, Argentina. Widely regarded as one of the greatest players ever, he is known for his extraordinary skill, vision, and goal-scoring ability. Career Highlights: Barcelona (2000–2021): Scored 672 goals, won 10 La Liga titles, 4 Champions League titles, and 7 Ballon d’Ors. Paris Saint-Germain (2021–2023): Won domestic trophies in France. Inter Miami (2023–Present): Continues to shine in Major League Soccer. International Career: Won the Copa América 2021, the Finalissima 2022, and the FIFA World Cup 2022, cementing his legacy as Argentina’s hero. Messi is celebrated for his humility, consistency, and unmatched achievements on the field."
language = 'en'
tts = gTTS(text=text, lang=language, slow=False)

audio_file = "output.mp3"
tts.save(audio_file)

from IPython.display import Audio
Audio(audio_file)

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    sample_rate, data = wavfile.read(wav_file)

    if len(data.shape) > 1:
        data = data[:, 0]

    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)
    plt.ylim(0, sample_rate / 2)
    plt.grid(True)
    plt.show()
wav_file_path = 'mixkit-game-show-suspense-waiting-667.wav'
generate_spectrogram(wav_file_path)

!pip install gtts

from gtts import gTTS
import os

text = " Kaká (Ricardo Izecson dos Santos Leite) is a Brazilian football legend, born on April 22, 1982, in Gama, Brazil. Known for his exceptional dribbling, vision, and playmaking ability, Kaká is regarded as one of the best midfielders of his generation.  Career Highlights: São Paulo (2001–2003): Kaká started his professional career in Brazil, where he won domestic titles and made his name. AC Milan (2003–2009): Achieved great success, winning 1 Champions League title (2007), 1 Serie A title**, and 1 FIFA Club World Cup. He also won the Ballon d'Or in 2007. Real Madrid (2009–2013): Although his time was marred by injuries, he won 1 La Liga title and 1 Copa del Rey with the club. Orlando City (2014–2017): Played in MLS for a few seasons before retiring. International Career: Brazil National Team: Won the FIFA World Cup 2002 and the Copa América 2007. Kaká is admired for his elegance on the ball, leadership, and sportsmanship, and he remains one of Brazil's most iconic footballers."
language = 'en'
tts = gTTS(text=text, lang=language, slow=False)

audio_file = "output.mp3"
tts.save(audio_file)

from IPython.display import Audio
Audio(audio_file)