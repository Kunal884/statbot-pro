with open('config.py', 'w', encoding='utf-8', newline='\n') as f:
    f.write("""import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

class Config:
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8001))
    WORKERS = 1
    LOG_LEVEL = "debug"
    ENVIRONMENT = "development"
    CORS_ORIGINS = ["http://localhost:3000", "http://localhost:8080"]
    ALLOWED_HOSTS = ["*"]
    MAX_FILE_SIZE = 50 * 1024 * 1024
    ALLOWED_EXTENSIONS = [".csv"]
    RATE_LIMIT_REQUESTS = 1000
    RATE_LIMIT_WINDOW = 3600
    EXECUTION_TIMEOUT = 30
    MAX_RETRIES = 3
    MAX_ROWS = 10000
    MAX_COLUMNS = 100
    MAX_CELL_SIZE = 1000
    MAX_QUERY_LENGTH = 5000
    MAX_RESPONSE_LENGTH = 10000
    CLEANUP_INTERVAL = 3600
    BASE_DIR = Path(__file__).parent
    WORKSPACE_DIR = BASE_DIR / "workspace"
    STATIC_DIR = BASE_DIR / "static"
    TEMPLATES_DIR = BASE_DIR / "templates"
    LOGS_DIR = BASE_DIR / "logs"

    @classmethod
    def setup_directories(cls):
        for d in [cls.WORKSPACE_DIR, cls.STATIC_DIR, cls.TEMPLATES_DIR, cls.LOGS_DIR]:
            d.mkdir(exist_ok=True)

    @classmethod
    def get_uvicorn_config(cls):
        return {"host": cls.HOST, "port": cls.PORT, "workers": 1, "log_level": cls.LOG_LEVEL, "access_log": True, "reload": True, "loop": "asyncio"}

    @classmethod
    def is_development(cls):
        return True

config = Config()

def get_config():
    return config
""")
print("Done!")