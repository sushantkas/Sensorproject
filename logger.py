import logging
import os, sys
from datetime import datetime


log_file=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs", log_file)


os.makedirs(logs_path, exist_ok=True)


log_file_path = os.path.join(logs_path, log_file)

logging.basicConfig(
    filename=log_file_path,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

