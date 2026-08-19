import ctypes
import win32api
import win32con


def set_volume(volume_level):
    # Ensure volume_level is between 0.0 and 1.0
    volume_level = max(0.0, min(volume_level, 1.0))

    # Convert volume level to range 0-65535
    volume = int(volume_level * 65535)

    # Set the volume
    ctypes.windll.winmm.waveOutSetVolume(0, volume)
    print(f"Volume set to {volume_level * 100}%")


if __name__ == "__main__":
    volume_level = float(input("Enter volume level (0.0 to 1.0): "))
    set_volume(volume_level)
