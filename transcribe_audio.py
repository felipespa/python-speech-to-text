import os
import whisper
import warnings


def remove_quotes(file_path):
    return file_path.replace('"', "")


def transcribe_audio():
    # Suppress warnings
    warnings.filterwarnings("ignore")

    # Initialize the model with the specified options
    model = whisper.load_model("medium")

    while True:
        file_path = input(
            "Cole o caminho do arquivo, ou digite 'sair' para fechar:"
        ).strip()

        if file_path.lower() == "sair":
            print("Saindo...")
            break

        try:
            # Remove quotes from the file path
            file_path = remove_quotes(file_path)

            # Get the absolute path of the file
            abs_file_path = os.path.abspath(file_path)

            print("\nTranscrevendo Leoazinha...\n")

            # Transcribe the audio
            result = model.transcribe(abs_file_path)

            print("\nTranscrição completa: \n")
            print(result["text"] + "\n")

        except FileNotFoundError:
            print("Não foi possível localizar o arquivo")
        except Exception as e:
            print(f"Erro ao localizar: {e}\nCopie o caminho novamente e tente de novo!")


if __name__ == "__main__":
    print("Só pra você lembrar que te amo... \n")
    transcribe_audio()
