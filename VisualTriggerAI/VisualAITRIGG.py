from ultralytics import YOLO
import cv2
import pygetwindow as gw
import mss
import serial
import time
import random
import keyboard
import numpy as np
import torch

# === DEVICE DETECTION ===
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"💻 Detected device: {device.upper()}")

# === CONFIGURATION ===
WINDOW_TITLE_FRAGMENT = "Moonlight"
COM_PORT = "COM3"
BAUD_RATE = 9600
TRIGGER_RADIUS = 20
OFFSET_Y = 10
SCALED_WIDTH = 640
SCALED_HEIGHT = 480

# === LOAD YOLO MODEL ===
print("⏳ Loading YOLOv9c model...")
model = YOLO('Vombit/yolov9c_cs2')  # Custom object detection
model.fuse()
print("✅ Model loaded and fused!")

# === UART SETUP ===
ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=0)

# === GLOBAL STATE ===
headshot_only = False
tab_pressed = False

# === FRAME CAPTURE ===
def capture_frame():
    window = None
    for w in gw.getAllWindows():
        if WINDOW_TITLE_FRAGMENT in w.title and w.visible:
            window = w
            break
    if window is None:
        print("❌ Stream window not found:", WINDOW_TITLE_FRAGMENT)
        return None, 0, 0

    x, y, width, height = window.left, window.top, window.width, window.height

    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": width, "height": height}
        img = sct.grab(monitor)
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        center_x = SCALED_WIDTH // 2
        center_y = (SCALED_HEIGHT // 2) + OFFSET_Y
        return frame, center_x, center_y

# === CENTER CHECK ===
def is_in_center(x_min, y_min, x_max, y_max, center_x, center_y):
    return (x_min <= center_x <= x_max) and (y_min <= center_y <= y_max)

# === MAIN LOOP ===
def main():
    print("🎯 System active! CapsLock = Toggle ON/OFF, TAB = Headshot-only mode, ESC = Exit")

    trigger_enabled = False
    toggle_pressed = False

    try:
        while True:
            # Toggle system on/off
            if keyboard.is_pressed('caps lock') and not toggle_pressed:
                trigger_enabled = not trigger_enabled
                toggle_pressed = True
                print(f"{'✅ System ON' if trigger_enabled else '⛔ System OFF'}")
            elif not keyboard.is_pressed('caps lock'):
                toggle_pressed = False

            # Toggle headshot-only mode
            global headshot_only, tab_pressed
            if keyboard.is_pressed('tab') and not tab_pressed:
                headshot_only = not headshot_only
                tab_pressed = True
                print(f"{'🎯 Headshot-only mode ENABLED' if headshot_only else '🎯 Headshot-only mode DISABLED'}")
            elif not keyboard.is_pressed('tab'):
                tab_pressed = False

            # Capture screen
            frame, center_x, center_y = capture_frame()
            if frame is None:
                continue

            resized_frame = cv2.resize(frame, (SCALED_WIDTH, SCALED_HEIGHT))
            results = model.predict(source=resized_frame, device=device, verbose=False)[0]
            detections = results.boxes

            # UI overlay
            status_text = f"System: {'ON' if trigger_enabled else 'OFF'} | Head-only: {'ON' if headshot_only else 'OFF'}"
            cv2.putText(resized_frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 255, 0) if trigger_enabled else (0, 0, 255), 2)
            cv2.circle(resized_frame, (center_x, center_y), TRIGGER_RADIUS, (255, 0, 0), 2)

            if trigger_enabled:
                for box in detections:
                    x_min, y_min, x_max, y_max = map(int, box.xyxy[0])
                    cls = int(box.cls[0])
                    label = results.names[cls]

                    cv2.rectangle(resized_frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
                    cv2.putText(resized_frame, label, (x_min, y_min - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 1)

                    # Check position and condition
                    if is_in_center(x_min, y_min, x_max, y_max, center_x, center_y):
                        if not headshot_only or ('head' in label.lower()):
                            if random.random() < 0.15:  # ~15% success rate
                                print(f"🎯 [{label}] Trigger activated!")
                                ser.write(b'1\r')
                                time.sleep(random.uniform(0.085, 0.135))  # Simulated human reaction time
                            else:
                                print(f"🤖 [{label}] Skipped (randomized fail for realism)")
                            break

            # Show preview window
            cv2.imshow("VisualTriggerAI - Live View", resized_frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

    finally:
        ser.close()
        cv2.destroyAllWindows()
        print("🛑 System terminated.")

if __name__ == "__main__":
    main()
