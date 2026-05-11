from pathlib import Path
import subprocess


DATA_DIR = Path("data")
ARCHIVE_DIR = DATA_DIR / "archives"

URLS = [
    "https://zenodo.org/records/14546832/files/HRPlanes.7z.001?download=1",
    "https://zenodo.org/records/14546832/files/HRPlanes.7z.002?download=1",
    "https://zenodo.org/records/14546832/files/HRPlanes.7z.003?download=1",
    "https://zenodo.org/records/14546832/files/HRPlanes.7z.004?download=1",
    "https://zenodo.org/records/14546832/files/HRPlanes.7z.005?download=1",
    "https://zenodo.org/records/14546832/files/HRPlanes.7z.006?download=1",
    "https://zenodo.org/records/14546832/files/HRPlanes.7z.007?download=1",
    "https://zenodo.org/records/14546832/files/HRPlanes.7z.008?download=1",
    "https://zenodo.org/records/14546832/files/HRPlanes.7z.009?download=1",
    "https://zenodo.org/records/14546832/files/HRPlanes.7z.010?download=1",
]


ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

for url in URLS:
    file_name = url.split("/")[-1].split("?")[0]
    out_path = ARCHIVE_DIR / file_name

    if out_path.exists():
        print("already downloaded:", out_path)
        continue

    print("download:", file_name)
    subprocess.run(
        ["wget", "-c", "-O", str(out_path), url],
        check=True
    )


first_part = ARCHIVE_DIR / "HRPlanes.7z.001"

print("extract:", first_part)
subprocess.run(
    ["7z", "x", str(first_part), f"-o{DATA_DIR}"],
    check=True
)

print("Path to dataset files:", DATA_DIR.resolve())
