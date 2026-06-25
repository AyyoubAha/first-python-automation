from pathlib import Path

from main import get_category


def test_get_category_for_image():
    assert get_category(Path("photo.jpg")) == "images"


def test_get_category_for_document():
    assert get_category(Path("notes.pdf")) == "documents"


def test_get_category_for_unknown_extension():
    assert get_category(Path("file.unknown")) == "other"
