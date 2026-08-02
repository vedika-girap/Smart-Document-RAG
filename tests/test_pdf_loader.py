from pathlib import Path

from app.loaders.pdf_loader import PDFLoader

def test_pdf_loader():
    loader = PDFLoader()

    document = loader.load(
        Path("data/raw/sample.pdf")
    )

    assert document.metadata["filename"] == "sample.pdf"
    assert document.metadata["filetype"] == "pdf"
    assert len(document.content) > 0 