from pathlib import Path


def load_document(file_path):
    return Path(file_path).read_text(encoding="utf-8")


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent

    file_path = project_root / "data" / "backend.txt"
    
    text = load_document(file_path)

    print("\nDocument contents:")
    print(text)