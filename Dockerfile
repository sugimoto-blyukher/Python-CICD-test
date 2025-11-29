FROM python:3.11-slim-bookworm

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をコピー＆インストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリ本体をコピー
COPY ./app /app

# コンテナ内で開けるポート（任意だけど書いておくと親切）
EXPOSE 8080

# 本番用CMD
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
