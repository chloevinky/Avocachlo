#!/usr/bin/env python3
"""Build a Prism Launcher-importable instance zip from this repository.

Usage (from anywhere inside the repo):
    python3 tools/build-prism-instance.py

Output: build/Avocachlo-Prism.zip
Import it in Prism Launcher via  Add Instance -> Import -> Local file.

The zip contains the instance metadata (Minecraft + Forge versions) and the
repository's game files (config/, defaultconfigs/, kubejs/) under .minecraft/.
Mods are not stored in this repository, so they must be added to the
instance's mods folder after importing.
"""
import json
import subprocess
import sys
import zipfile
from pathlib import Path

MINECRAFT_VERSION = "1.20.1"
FORGE_VERSION = "47.4.10"
INSTANCE_NAME = "Avocachlo"
ZIP_NAME = "Avocachlo-Prism.zip"

INSTANCE_CFG = f"""InstanceType=OneSix
name={INSTANCE_NAME}
iconKey=default
notes=Imported from the Avocachlo repository. Mods are not included - add the pack's {MINECRAFT_VERSION} Forge mods to the mods folder.
"""

MMC_PACK = {
    "formatVersion": 1,
    "components": [
        {"important": True, "uid": "net.minecraft", "version": MINECRAFT_VERSION},
        {"uid": "net.minecraftforge", "version": FORGE_VERSION},
    ],
}


def main() -> int:
    repo = Path(
        subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], text=True
        ).strip()
    )
    # Only ship files tracked by git so local working-directory clutter
    # (logs, generated configs, etc.) never leaks into the instance zip.
    tracked = subprocess.check_output(
        ["git", "-C", str(repo), "ls-files", "config", "defaultconfigs", "kubejs"],
        text=True,
    ).splitlines()
    if not tracked:
        print("No tracked game files found - run this from inside the repo.", file=sys.stderr)
        return 1

    out_dir = repo / "build"
    out_dir.mkdir(exist_ok=True)
    out_zip = out_dir / ZIP_NAME

    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("instance.cfg", INSTANCE_CFG)
        zf.writestr("mmc-pack.json", json.dumps(MMC_PACK, indent=4) + "\n")
        for rel in tracked:
            zf.write(repo / rel, ".minecraft/" + rel)

    print(f"Wrote {out_zip} ({len(tracked)} game files, "
          f"Minecraft {MINECRAFT_VERSION}, Forge {FORGE_VERSION})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
