from pathlib import Path
import subprocess
from pathlib import Path

THIS_DIR = Path(__file__).parent.resolve()

def run_test(cmd):
    try:
        # subprocess.run(f". .samples/bin/activate && {cmd}", shell=True, check=True)
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as ex:
        print(f"Cannot run {cmd}, {ex}")
        exit(-1)
    print("-" * 30)




THIS_DIR = Path(__file__).parent.resolve()

for fn in Path(THIS_DIR).glob("*.py"):
    if fn.stem in [ 'test_all_samples', 'input_providers' , 'eot-server' , 'portal_english_entities'] :
        continue
    print("running:",fn)
    run_test(f"""python3 {fn}""")


