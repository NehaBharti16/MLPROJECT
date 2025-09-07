import sys
from pathlib import Path

# Add src folder to Python path so MLPROJECT can be imported
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from MLPROJECT.logger import logging
from MLPROJECT.exception import CustomException
