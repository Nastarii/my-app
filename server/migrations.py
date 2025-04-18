import os
import subprocess
from alembic.config import Config
from alembic import command

def run_migrations():
    alembic_cfg_path = os.path.join(os.path.dirname(__file__), "alembic.ini")
    alembic_cfg = Config(alembic_cfg_path)
    command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    run_migrations()
