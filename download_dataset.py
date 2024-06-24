import os

def download_dataset():
    os.system('kaggle datasets download -d kritanjalijain/amazon-reviews -p ./ --unzip')

if __name__ == "__main__":
    download_dataset()
