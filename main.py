import cv2
import time
import math
import numpy as np
import mediapipe as mp
import pyautogui

# Paksa OpenCV untuk hanya menggunakan CPU
cv2.setUseOptimized(False)
cv2.ocl.setUseOpenCL(False)
pyautogui.PAUSE = 0  # Hilangkan jeda tambahan

# Inisialisasi MediaPipe Hands dengan hanya satu tangan untuk optimasi
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.6, max_num_hands=1)

# Konfigurasi kamera dengan resolusi lebih rendah untuk meningkatkan performa
wcam, hcam = 320, 240
cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)
cap.set(cv2.CAP_PROP_FPS, 60)
pTime = 0
click_status = "Not Click"

screen_w, screen_h = pyautogui.size()

# Variabel untuk filter eksponensial (EMA) & dead zone
smooth_x, smooth_y = 0, 0
alpha = 0.2  # Faktor penghalusan lebih kecil agar lebih stabil
dead_zone = 5  # Hindari gerakan kecil yang tidak diinginkan

while True:
    success, img = cap.read()
    if not success:
        break
    
    img = cv2.flip(img, 1)  # Membalik gambar agar lebih natural
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = np.array([(int(lm.x * wcam), int(lm.y * hcam)) for lm in hand_landmarks.landmark])
            
            if len(lm_list) > 12:
                x_index, y_index = lm_list[8]  # Jari telunjuk
                x_middle, y_middle = lm_list[12]  # Jari tengah
                
                # Konversi posisi ke layar
                screen_x = np.interp(x_index, (20, wcam - 20), (0, screen_w))
                screen_y = np.interp(y_index, (20, hcam - 20), (0, screen_h))
                
                # Terapkan filter eksponensial untuk pergerakan lebih halus
                new_x = alpha * screen_x + (1 - alpha) * smooth_x
                new_y = alpha * screen_y + (1 - alpha) * smooth_y
                
                # Terapkan zona mati agar tidak terlalu sensitif
                if abs(new_x - smooth_x) > dead_zone or abs(new_y - smooth_y) > dead_zone:
                    smooth_x, smooth_y = new_x, new_y
                    pyautogui.moveTo(smooth_x, smooth_y, duration=0)
                
                # Jika jari telunjuk dan tengah terbuka (jaraknya lebih dari ambang batas), tahan klik kiri
                length = np.hypot(x_middle - x_index, y_middle - y_index)
                if length > 50:
                    pyautogui.mouseDown()
                    click_status = "Click"
                else:
                    pyautogui.mouseUp()
                    click_status = "Not Click"
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 1)
    cv2.putText(img, f'Status: {click_status}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    
    cv2.imshow("Img", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()