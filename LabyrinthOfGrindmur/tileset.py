import tcod
import numpy as np  # type: ignore
from typing import List, Tuple


class TilesetData:

    """
    The basics of it though are, I load in the tcod CP437 tileset then reserve
    codepoints from the Unicode Private Use Area.
    I can then arbitrarily modify my font file. I keep it to 16 columns
    and just add rows as needed to keep things simple.
    """

    def __init__(self) -> None:
        self._charmap = tcod.tileset.CHARMAP_CP437
        _pua_start = 57344
        _pua_end = 57856
        self._charmap.extend([_ for _ in range(_pua_start, _pua_end)])

    @property
    def charmap(self) -> List[int]:
        """The extended CP437 charmap, extended with 512 codepoints from the
        unicode private use area (codepoints 57344:57856)
        """
        return self._charmap

    @property
    def tilemap(self) -> List[int]:
        """A list of integers starting from 0 representing the Tiled-generated
        tilemap enumeration.
        """
        return [_ for _ in range(len(self._charmap))]

    def __getitem__(
            self,
            key: Tuple[str, slice, slice]
    ) -> np.ndarray:
        """Implementation of slice indexing for both map classifications.
        To slice the `charmap`, set key to ('charmap', :, :).
        To slice the `tilemap`, set key to ('tilemap', :, :).
        """
        _charmap_array = np.array(self.charmap).reshape(80, 16)
        _tilemap_array = np.array(self.tilemap).reshape(80, 16)
        if key[0] == 'charmap':
            return _charmap_array[key[1], key[2]]
        elif key[0] == 'tilemap':
            return _tilemap_array[key[1], key[2]]


tileset = tcod.tileset.load_tilesheet(
    path="rexpaint_cp437_10x10.png",
    columns=16,
    rows=48,
    charmap=TilesetData().charmap)
