import os

class Mem:

    def get_file_size_readable(self, file_path):
        """
        Gibt die Dateigröße in einem lesbaren Format (KB, MB, GB) zurück.

        Args:
            file_path (str): Der Pfad zur Datei.

        Returns:
            str: Die Dateigröße in einem lesbaren Format.
        """
        file_size_bytes = os.path.getsize(file_path)
        if file_size_bytes < 1024:
            return f"{file_size_bytes} Bytes"
        elif file_size_bytes < 1024 * 1024:
            return f"{file_size_bytes / 1024:.2f} KB"
        elif file_size_bytes < 1024 * 1024 * 1024:
            return f"{file_size_bytes / (1024 * 1024):.2f} MB"
        else:
            return f"{file_size_bytes / (1024 * 1024 * 1024):.2f} GB"
        