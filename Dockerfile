FROM python:3.10-slim


RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*


RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


RUN playwright install chromium
RUN playwright install-deps


COPY . .


RUN mkdir -p allure-results screenshots


CMD ["pytest", "tests/", "-v", "--alluredir=allure-results"]