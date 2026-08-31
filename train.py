import time
from datetime import datetime

for step in range(1, 100000):
    print(f"[{datetime.now():%H:%M:%S}] step {step} loss={1/step:.5f}", flush=True)
    time.sleep(1)
