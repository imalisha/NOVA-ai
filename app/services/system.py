import ctypes
import subprocess


class SystemService:

    # ========================================================
    # LOCK COMPUTER
    # ========================================================

    def lock_computer(self):

        try:

            ctypes.windll.user32.LockWorkStation()

            return "Locking your computer."

        except Exception as error:

            print(f"Lock error: {error}")

            return "I couldn't lock the computer."

    # ========================================================
    # SCREENSHOT
    # ========================================================

    def take_screenshot(self):

        try:

            # Windows shortcut: Win + Print Screen
            user32 = ctypes.windll.user32

            # Press Windows key
            user32.keybd_event(
                0x5B,
                0,
                0,
                0
            )

            # Press Print Screen
            user32.keybd_event(
                0x2C,
                0,
                0,
                0
            )

            # Release Print Screen
            user32.keybd_event(
                0x2C,
                0,
                2,
                0
            )

            # Release Windows key
            user32.keybd_event(
                0x5B,
                0,
                2,
                0
            )

            return (
                "Screenshot captured and saved "
                "to your Pictures folder."
            )

        except Exception as error:

            print(f"Screenshot error: {error}")

            return "I couldn't take a screenshot."

    # ========================================================
    # VOLUME UP
    # ========================================================

    def volume_up(self):

        try:

            self.media_key(0xAF)

            return "Volume increased."

        except Exception as error:

            print(f"Volume up error: {error}")

            return "I couldn't increase the volume."

    # ========================================================
    # VOLUME DOWN
    # ========================================================

    def volume_down(self):

        try:

            self.media_key(0xAE)

            return "Volume decreased."

        except Exception as error:

            print(f"Volume down error: {error}")

            return "I couldn't decrease the volume."

    # ========================================================
    # MUTE
    # ========================================================

    def mute(self):

        try:

            self.media_key(0xAD)

            return "Volume muted."

        except Exception as error:

            print(f"Mute error: {error}")

            return "I couldn't mute the volume."

    # ========================================================
    # PLAY / PAUSE
    # ========================================================

    def play_pause(self):

        try:

            self.media_key(0xB3)

            return "Play and pause command sent."

        except Exception as error:

            print(f"Media error: {error}")

            return "I couldn't control media playback."

    # ========================================================
    # MEDIA KEY HELPER
    # ========================================================

    def media_key(self, key):

        user32 = ctypes.windll.user32

        user32.keybd_event(
            key,
            0,
            0,
            0
        )

        user32.keybd_event(
            key,
            0,
            2,
            0
        )

    # ========================================================
    # SHUTDOWN
    # ========================================================

    def shutdown(self):

        try:

            subprocess.run(
                [
                    "shutdown",
                    "/s",
                    "/t",
                    "5"
                ],
                check=False
            )

            return (
                "Shutdown scheduled in 5 seconds."
            )

        except Exception as error:

            print(f"Shutdown error: {error}")

            return "I couldn't shut down the computer."

    # ========================================================
    # RESTART
    # ========================================================

    def restart(self):

        try:

            subprocess.run(
                [
                    "shutdown",
                    "/r",
                    "/t",
                    "5"
                ],
                check=False
            )

            return (
                "Restart scheduled in 5 seconds."
            )

        except Exception as error:

            print(f"Restart error: {error}")

            return "I couldn't restart the computer."