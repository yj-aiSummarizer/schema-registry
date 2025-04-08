import os, json, requests
from dotenv import load_dotenv

# ✅ .env 파일 로딩
load_dotenv()

SCHEMA_DIR = "./schemas"
SCHEMA_REGISTRY_URL = os.getenv("SCHEMA_REGISTRY_URL")

if not SCHEMA_REGISTRY_URL:
    raise RuntimeError("❌ SCHEMA_REGISTRY_URL 환경변수가 설정되지 않았습니다.")

for filename in os.listdir(SCHEMA_DIR):
    if filename.endswith(".avsc"):
        subject = f"{filename.replace('.avsc', '')}-value"
        with open(os.path.join(SCHEMA_DIR, filename)) as f:
            schema_str = json.dumps(json.load(f))
            payload = {"schema": schema_str}
            res = requests.post(
                f"{SCHEMA_REGISTRY_URL}/subjects/{subject}/versions",
                headers={"Content-Type": "application/vnd.schemaregistry.v1+json"},
                data=json.dumps(payload)
            )
            print(f"📦 등록 완료: {subject} → {res.status_code} {res.text}")