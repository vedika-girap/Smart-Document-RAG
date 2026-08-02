from pathlib import Path

from app.loaders.txt_loader import TXTLoader


def test_txt_loader():
    loader = TXTLoader()

    document = loader.load(Path("data/raw/aws.txt"))

    assert document.metadata["filename"] == "aws.txt"
    assert document.metadata["filetype"]== "txt"
    assert "AWS IAM" in document.content
    