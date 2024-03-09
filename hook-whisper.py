from PyInstaller.utils.hooks import collect_data_files

# Include Whisper package assets
# This line collects the data files associated with the Whisper package
datas = collect_data_files("whisper")
