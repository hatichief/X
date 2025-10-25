import os
import json

def validate_json_files(directory="."):
    print(f"📂 Memeriksa semua file JSON di: {os.path.abspath(directory)}\n")

    json_files = [f for f in os.listdir(directory) if f.endswith(".json")]
    if not json_files:
        print("⚠️ Tidak ada file JSON ditemukan.")
        return

    for filename in json_files:
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                json.load(f)
            print(f"✅ {filename} — VALID")
        except Exception as e:
            print(f"❌ {filename} — INVALID ({e})")

if __name__ == "__main__":
    validate_json_files(".")