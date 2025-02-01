from setuptools import setup, find_packages
import os

# Read long description if README.md exists
long_description = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name="telegram_chatbot",
    version="1.0.0",
    author_email=".com",
    description="Telegram Agent Bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tgbotgit/Group-Agent-AI",  # Change if private
    packages=find_packages(),
    install_requires=[
        "pyTelegramBotAPI",
        "openai==0.28.0",
        "requests",
        "tqdm"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="<=3.8",
)
