from setuptools import setup, find_packages

setup(
    name="kbaccv",  # Назва вашої бібліотеки
    version="0.1",  # Початкова версія
    author="Ваше ім'я",  # Вкажіть ваше ім'я або псевдонім
    author_email="ваш_email@example.com",  # Ваш email
    description="Бібліотека для аналізу зображень та відео з об'єктами",  # Короткий опис бібліотеки
    long_description=open("README.md", encoding="utf-8").read(),  # Опис з файлу README.md
    long_description_content_type="text/markdown",  # Тип довгого опису
    url="https://github.com/yourusername/kbaccv",  # Посилання на ваш репозиторій (якщо є)
    packages=find_packages(),  # Автоматичний пошук і включення всіх пакетів
    install_requires=[
        "Pillow",  # Бібліотека для роботи з зображеннями
        "imageio",  # Бібліотека для обробки відео
        "numpy",  # Бібліотека для роботи з масивами
    ],  # Залежності
    classifiers=[
        "Programming Language :: Python :: 3",  # Підтримка Python 3
        "License :: OSI Approved :: MIT License",  # Ліцензія
        "Operating System :: OS Independent",  # Платформа не має значення
    ],
    python_requires=">=3.6",  # Мінімальна версія Python
)