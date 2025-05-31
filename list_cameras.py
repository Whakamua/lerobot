import cv2

def list_cameras():
    # Try to open cameras with different indices
    available_cameras = []
    
    for i in range(10):  # Check first 10 indices
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print(f"Camera {i} is available")
                print(f"Frame shape: {frame.shape}")
                available_cameras.append(i)
            cap.release()
    
    if not available_cameras:
        print("No cameras found!")
    else:
        print(f"\nFound {len(available_cameras)} cameras with indices: {available_cameras}")

if __name__ == "__main__":
    list_cameras() 