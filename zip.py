import zipfile
import sys
import os


def browse_folder(folder):
    files = []
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if not path.startswith("./."):
            if os.path.isdir(path):
                files.extend(browse_folder(path))
            else:
                files.append(path.replace("\\", "/").replace("./", ""))
    return files

def main():
    version = sys.argv[1]
    datapackname = sys.argv[2]
    with zipfile.ZipFile(f"{datapackname}-{version}.zip", "w", compresslevel=9) as zf:
        for root, dirs, files in os.walk("./"):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.startswith("./data") or file_path == "./pack.mcmeta" or file_path == "./LICENSE" or file_path == "./pack.png":
                    zf.write(file_path)


    with zipfile.ZipFile(f"{datapackname}-{version}-rp.zip", "w", compresslevel=9) as zf:
        for root, dirs, files in os.walk("./"):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.startswith("./assets") or file_path == "./pack.mcmeta" or file_path == "./LICENSE" or file_path == "./pack.png":
                    zf.write(file_path)


if __name__ == "__main__":
    main()