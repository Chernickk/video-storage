FROM node:12.21.0

WORKDIR /app
# Копируем package.json и package-lock.json и делаем npm install, чтобы зависимости закешировались.
COPY ./ ./
RUN npm install

# Финальный слой содержит билд нашего приложения.
RUN npm run build

