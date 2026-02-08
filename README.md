# Super Resolution с RealESRGAN

Увеличение разрешения изображений в 4× с помощью предобученной модели RealESRGAN. Веб-приложение на Gradio для интерактивной работы.

Быстрый старт
=

- Установка зависимостей:

    pip install -r requirements.txt

- Запуск приложения:

    python app.py

- Открой в браузере: http://localhost:7860

Сборка образа Docker
=

- Сборка образа:

    docker build -t sr-app .

- Запуск контейнера:

    docker run -p 7860:7860 sr-app

- Открыть в браузере: http://localhost:7860

Тесты
=

    pytest tests/ -v