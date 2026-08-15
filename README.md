# Raspberry Flavoured
A Minecraft 1.20.1 modpack

## Installing with Prism Launcher

> **Note:** mods are not stored in this repository. After either method below, add the pack's 1.20.1 Forge mods to the instance's `mods` folder (right-click the instance → **Folder** → `mods`).

### Option 1 — import an instance zip (easiest)
1. Build the zip (needs Python 3 and git): run `python3 tools/build-prism-instance.py` from a clone of this repo — it writes `build/Avocachlo-Prism.zip`.
2. In Prism Launcher: **Add Instance → Import → Local file**, and select the zip.
3. The instance comes preconfigured with Minecraft **1.20.1** and Forge **47.4.10**, plus this repo's `config`, `defaultconfigs`, and `kubejs` folders.

To have GitHub build the zip automatically on every push to `main` (published on a `prism-latest` release, so users can skip step 1), move `tools/prism-instance.workflow.yml` to `.github/workflows/prism-instance.yml` and push — that file couldn't be added directly from this automated session because the GitHub App lacks the `workflows` permission.

### Option 2 — clone the repo into an instance (for pack development)
1. In Prism Launcher create a new instance: **Add Instance → Custom**, Minecraft **1.20.1**, then under Mod Loader pick Forge **47.4.10**.
2. Right-click the instance → **Folder** to open its `minecraft` folder.
3. Clone this repository directly into that folder:
   ```
   git init
   git remote add origin https://github.com/chloevinky/Avocachlo.git
   git fetch origin
   git checkout main
   ```
   (or clone it elsewhere and copy `config`, `defaultconfigs`, and `kubejs` in).

### MODPACK CREDITS:

**raspmary** - Project lead

**Baisylia** - Co-lead, programming, Discord 
& GitHub management

**cassiancc** - Creator and main 
developer of Raspberry Core, Discord 
& GitHub management

**DavigJ** - Major work on 
Raspberry Core, creator of various 
useful mods in RF

**nöelle** - Major sprite/texture 
work & music

**Nive** - Major sprite/texture work

**QinomeD** - Programming, creator 
of KubeJS Delight

**Crabbarition** - Programming, music, 
Discord management

**asof** - Major programming work,
sprite/texture work

**Derb** - Major sprite/texture work

**ProbablyEkho** - Major sprite/texture work

**Kayla_the_Bee** - Major sprite/texture work, Discord management

**ChadVAFN** - Ideas, Discord management

**Kiroto** - Public RF SMP server owner

**MehVahdJukaar** - Creator of various 
essential mods in RF (made tweaks 
upon request)

**DoltHHaven** - Mod configurations, 
creator of some useful mods in RF

**Kobber** - Sprite/texture work

**MythrilBagels** - Sprite/texture work, 
creator of some resource packs in RF

**Jamiscus** - Sprite/texture work

**CW** - Sprite/texture work

**noodleman** - Sprite/texture work

**beb** - Sprite/texture work

**Jameslice** - Sprite/texture work

**jaybees** - Ideas, sprite/texture work

**SarahIsWeird** - Programming,
Raspberry Core contributor

**Grom PE** - Programming

**WaterOre** - Ideas, programming

**AkhillLikesMinecraft** - Programming

**culling** - Programming

**Kelpiesaurus** - Ideas, mod configurations

**db3k** - Inspiration for 
built-in resource packs

**Vazkii** - Mod configurations

**Freshah** - Previously assisted 
with programming

**murao.kun** - Previous inspiration 
for inventory layout
