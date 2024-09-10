# kbaccv/core.py

import imageio
from PIL import Image, ImageDraw, ImageFont
import numpy as np

class KbacCV:
    def __init__(self, similarity_threshold=0.7):
        """
        Ініціалізація класу.
        similarity_threshold — це поріг схожості, за яким ми визначаємо об'єкт як знайдений.
        """
        self.dataset = []  # Спочатку датасет порожній
        self.similarity_threshold = similarity_threshold

    def set_dataset(self, dataset_paths):
        """
        Функція для встановлення датасету.
        Приймає список шляхів до зображень, які будуть використані для порівняння.
        """
        self.dataset = [self._load_image(path) for path in dataset_paths]

    def _load_image(self, path):
        """
        Допоміжна функція для завантаження зображення та перетворення його в масив.
        """
        img = Image.open(path)
        img_array = np.asarray(img)  # Перетворюємо зображення на масив
        return img_array

    def load_source(self, src):
        """
        Завантажує джерело для аналізу. Це може бути або фото, або відео.
        """
        if src.endswith(('.png', '.jpg', '.jpeg')):
            # Якщо це фото, завантажуємо зображення
            image = self._load_image(src)
            return image
        elif src.endswith(('.mp4', '.avi')):
            # Якщо це відео, використовуємо imageio для читання кадрів
            reader = imageio.get_reader(src)
            return reader
        else:
            raise ValueError("Невідомий формат файлу.")

    def compare_objects(self, frame, obj):
        """
        Функція порівняння об'єкта з кадром.
        Повертає схожість від 0.0 до 1.0 на основі середньої різниці пікселів.
        """
        if frame.shape != obj.shape:
            # Якщо розміри кадру і об'єкта різні, схожість 0
            return 0.0

        # Обчислюємо середню різницю пікселів між кадром і об'єктом
        difference = np.abs(frame - obj).mean()
        similarity = 1 - (difference / 255.0)  # Нормалізуємо значення до [0.0, 1.0]
        return similarity

    def draw_objects(self, frame, detected_object_name, location):
        """
        Малює на кадрі рамку і додає підпис для знайденого об'єкта.
        """
        img = Image.fromarray(frame)
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()

        # Обведення рамки навколо знайденого об'єкта
        x, y, w, h = location
        draw.rectangle([x, y, x + w, y + h], outline="red", width=2)

        # Додаємо текст із назвою об'єкта над рамкою
        draw.text((x, y - 10), detected_object_name, fill="red", font=font)

        return np.array(img)

    def process(self, src):
        """
        Основна функція обробки файлу (відео чи фото).
        Повертає оброблені кадри з підписаними об'єктами.
        """
        if not self.dataset:
            raise ValueError("Датасет не встановлений. Використовуйте set_dataset(), щоб встановити шлях до датасету.")

        source = self.load_source(src)

        # Якщо це фото
        if isinstance(source, np.ndarray):
            return self._process_frame(source)

        # Якщо це відео
        elif isinstance(source, imageio.core.format.Reader):
            processed_frames = []
            for i, frame in enumerate(source):
                frame_array = np.array(frame)
                processed_frame = self._process_frame(frame_array)
                processed_frames.append(processed_frame)

                # Логічне обмеження для тестування — лише перші 100 кадрів
                if i > 100:
                    break
            return processed_frames

    def _process_frame(self, frame):
        """
        Функція для обробки окремого кадру: перевіряє збіги з об'єктами з dataset.
        Якщо знаходить збіг, обводить об'єкт рамкою.
        """
        for obj in self.dataset:
            similarity = self.compare_objects(frame, obj)
            if similarity >= self.similarity_threshold:
                # Якщо схожість достатня, малюємо рамку та підписуємо об'єкт
                detected_object_name = "Object"  # Тестова назва знайденого об'єкта
                location = (50, 50, obj.shape[1], obj.shape[0])  # Пример координат
                frame = self.draw_objects(frame, detected_object_name, location)

        return frame