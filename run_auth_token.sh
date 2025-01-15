#!/bin/bash

# 仮想環境のパス
VENV_PATH="/var/www/twikit_for_authtoken/venv"

# アプリケーションのディレクトリ
APP_DIR="/var/www/twikit_for_authtoken"

# 仮想環境をアクティベート
source "$VENV_PATH/bin/activate"

# アプリケーションディレクトリに移動
cd "$APP_DIR"

# Pythonスクリプトを実行
python3 twikit/main.py

# 仮想環境を非アクティブ化
deactivate
