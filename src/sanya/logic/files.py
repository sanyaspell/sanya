from collections.abc import Generator
from pathlib import Path


def iter_po_files(folder_path: Path) -> Generator[Path, None, None]:
    """Iterate over all `.po` files in `folder_path` or the file itself."""
    path = Path(folder_path)
    if path.is_file() and path.suffix == '.po':
        yield path
        return
    yield from path.rglob('*.po')
