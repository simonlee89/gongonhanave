from flask import Flask, jsonify, send_from_directory
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv('config.env')

app = Flask(__name__)

@app.route('/')
def index():
    """메인 페이지"""
    return send_from_directory('.', 'index.html')

@app.route('/health')
def health():
    """헬스 체크 엔드포인트"""
    return jsonify({'status': 'ok'})

@app.route('/api/config')
def get_config():
    """API 키와 설정 정보를 클라이언트에 제공"""
    # 환경 변수 확인
    print(f"[DEBUG] NAVER_MAP_CLIENT_ID: {os.getenv('NAVER_MAP_CLIENT_ID')}")
    print(f"[DEBUG] SUPABASE_URL: {os.getenv('SUPABASE_URL')}")
    print(f"[DEBUG] SUPABASE_KEY 존재: {bool(os.getenv('SUPABASE_KEY'))}")
    
    return jsonify({
        'CLIENT_ID': os.getenv('NAVER_MAP_CLIENT_ID'),
        'CLIENT_SECRET': os.getenv('NAVER_MAP_CLIENT_SECRET'),
        'SUPABASE': {
            'URL': os.getenv('SUPABASE_URL'),
            'ANON_KEY': os.getenv('SUPABASE_KEY')
        },
        'NAVER_MAP': {
            'CENTER': {'lat': 37.5665, 'lng': 126.9780},  # 서울 중심
            'ZOOM': 12
        }
    })

if __name__ == '__main__':
    # Railway 배포 시 포트는 자동으로 할당됨
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port) 