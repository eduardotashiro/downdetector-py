FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    xvfb \
    tini \
    build-essential \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libasound2t64 \
    libxt6 \
    libx11-xcb1 \
    libxcb-dri3-0 \
    libdrm2 \
    libgbm1 \
    libxss1 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    fonts-liberation \
    fonts-noto-color-emoji \
    && rm -rf /var/lib/apt/lists/*

ENV DISPLAY=:99
ENV PYTHONUNBUFFERED=1
ENV MOZ_DISABLE_CONTENT_SANDBOX=1
ENV MOZ_DISABLE_GPU_SANDBOX=1
ENV MOZ_DISABLE_RDD_SANDBOX=1
ENV MOZ_DISABLE_SOCKET_PROCESS_SANDBOX=1
ENV MOZ_DISABLE_UTILITY_SANDBOX=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m camoufox fetch

COPY . .

RUN chmod +x ./xvfb.sh

ENTRYPOINT ["/usr/bin/tini", "--", "/bin/bash", "/app/xvfb.sh"]

CMD ["sh", "-c", "make dockerrun"]