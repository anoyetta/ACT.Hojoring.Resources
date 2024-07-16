from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlretrieve


def download():
    xivdb = Path("resources/xivdb")
    ko_url = "https://raw.githubusercontent.com/Ra-Workspace/ffxiv-datamining-ko/master/csv/{name}.csv"
    cn_url = "https://raw.githubusercontent.com/thewakingsands/ffxiv-datamining-cn/master/{name}.csv"

    sheets = ["Action", "Status", "TerritoryType"]

    with ThreadPoolExecutor() as executor:
        for sheet in sheets:
            executor.submit(
                urlretrieve,
                ko_url.format(name=sheet),
                xivdb / f"{sheet}.ko-KR.csv",
            )
            executor.submit(
                urlretrieve,
                cn_url.format(name=sheet),
                xivdb / f"{sheet}.zh-CN.csv",
            )


if __name__ == "__main__":
    download()
