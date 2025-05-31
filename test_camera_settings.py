import cv2
import time

def test_camera_settings():
    # Try to open the camera with default settings first
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    
    # Get default settings
    default_fps = cap.get(cv2.CAP_PROP_FPS)
    default_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    default_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    print(f"Default settings:")
    print(f"FPS: {default_fps}")
    print(f"Width: {default_width}")
    print(f"Height: {default_height}")
    
    # Try to read a frame with default settings
    ret, frame = cap.read()
    if ret:
        print(f"Successfully read frame with default settings")
        print(f"Frame shape: {frame.shape}")
    else:
        print("Failed to read frame with default settings")
    
    # Release the camera
    cap.release()
    
    # Now try with our desired settings
    print("\nTrying with desired settings (1280x720, 30fps):")
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, 30)
    
    # Get actual settings
    actual_fps = cap.get(cv2.CAP_PROP_FPS)
    actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    print(f"Actual settings:")
    print(f"FPS: {actual_fps}")
    print(f"Width: {actual_width}")
    print(f"Height: {actual_height}")
    
    # Try to read a frame
    ret, frame = cap.read()
    if ret:
        print(f"Successfully read frame with desired settings")
        print(f"Frame shape: {frame.shape}")
    else:
        print("Failed to read frame with desired settings")
    
    # Release the camera
    cap.release()

if __name__ == "__main__":
    test_camera_settings() 