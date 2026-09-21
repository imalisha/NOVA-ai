import os
import subprocess
import winreg
import time


class FileService:

    # ========================================================
    # GET WINDOWS FOLDER
    # ========================================================

    def get_windows_folder(self, name):

        try:

            key_path = (
                r"Software\Microsoft\Windows"
                r"\CurrentVersion\Explorer\User Shell Folders"
            )

            with winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                key_path
            ) as key:

                value, _ = winreg.QueryValueEx(
                    key,
                    name
                )

                return os.path.expandvars(value)

        except Exception as error:

            print(
                f"Folder lookup error: {error}"
            )

            return None

    # ========================================================
    # OPEN FOLDER
    # ========================================================

    def open_folder(self, path, folder_name):

        if not path:

            return (
                f"I couldn't find your "
                f"{folder_name} folder."
            )

        if not os.path.exists(path):

            return (
                f"Your {folder_name} folder "
                f"doesn't exist."
            )

        try:

            subprocess.Popen(
                [
                    "explorer.exe",
                    path
                ]
            )

            return (
                f"Opening {folder_name}."
            )

        except Exception as error:

            print(
                f"Open folder error: {error}"
            )

            return (
                f"I couldn't open "
                f"{folder_name}."
            )

    # ========================================================
    # CLOSE FOLDER WINDOW
    # ========================================================

    def close_folder(self, path, folder_name):

        if not path:

            return (
                f"I couldn't find your "
                f"{folder_name} folder."
            )

        try:

            # PowerShell closes only the Explorer
            # window displaying this exact folder.
            escaped_path = path.replace(
                "'",
                "''"
            )

            powershell_command = (
                "$shell = New-Object -ComObject Shell.Application; "
                f"$windows = $shell.Windows(); "
                "foreach ($window in $windows) { "
                "try { "
                "$url = $window.Document.Folder.Self.Path; "
                f"if ($url -eq '{escaped_path}') {{ "
                "$window.Quit() "
                "} "
                "} catch {} "
                "}"
            )

            result = subprocess.run(
                [
                    "powershell",
                    "-NoProfile",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-Command",
                    powershell_command
                ],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:

                return (
                    f"Closing {folder_name}."
                )

            return (
                f"I couldn't close "
                f"{folder_name}."
            )

        except Exception as error:

            print(
                f"Close folder error: {error}"
            )

            return (
                f"I couldn't close "
                f"{folder_name}."
            )

    # ========================================================
    # DESKTOP
    # ========================================================

    def open_desktop(self):

        path = self.get_windows_folder(
            "Desktop"
        )

        return self.open_folder(
            path,
            "Desktop"
        )

    def close_desktop(self):

        path = self.get_windows_folder(
            "Desktop"
        )

        return self.close_folder(
            path,
            "Desktop"
        )

    # ========================================================
    # DOCUMENTS
    # ========================================================

    def open_documents(self):

        path = self.get_windows_folder(
            "Personal"
        )

        return self.open_folder(
            path,
            "Documents"
        )

    def close_documents(self):

        path = self.get_windows_folder(
            "Personal"
        )

        return self.close_folder(
            path,
            "Documents"
        )

    # ========================================================
    # PICTURES
    # ========================================================

    def open_pictures(self):

        path = self.get_windows_folder(
            "My Pictures"
        )

        return self.open_folder(
            path,
            "Pictures"
        )

    def close_pictures(self):

        path = self.get_windows_folder(
            "My Pictures"
        )

        return self.close_folder(
            path,
            "Pictures"
        )

    # ========================================================
    # DOWNLOADS
    # ========================================================

    def open_downloads(self):

        downloads_key = (
            "{374DE290-123F-4565-9164-39C4925E467B}"
        )

        path = self.get_windows_folder(
            downloads_key
        )

        return self.open_folder(
            path,
            "Downloads"
        )

    def close_downloads(self):

        downloads_key = (
            "{374DE290-123F-4565-9164-39C4925E467B}"
        )

        path = self.get_windows_folder(
            downloads_key
        )

        return self.close_folder(
            path,
            "Downloads"
        )