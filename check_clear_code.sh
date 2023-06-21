# Правка измененных файлов форматировщиком кодо isort
# Что бы работало нужно поставить isort(https://pycqa.github.io/isort/)
# pip install isort
FILES=$(git diff --name-only)
isort $FILES
# Проверка "Чистоты кода". Оценка условкая, но стоит обратить внимание!
# https://habr.com/ru/articles/456150/
# Что бы работало нужно поставить radon(https://radon.readthedocs.io/en/latest/)
# pip install radon
echo "Подсчет цикломатической сложности измененных файлов(от A до F) A - хорошо,F - очень плохо"
radon cc $FILES
echo "Индекс поддерживаемости измененных файлов(от A до F) A - хорошо,F - очень плохо"
radon mi $FILES
