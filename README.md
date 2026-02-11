<h1 align="center">
  Awesome Fabric
  <p align="center">
    <img src="https://awesome.re/badge-flat.svg" href="https://awesome.re" />
    <img src="https://flat.badgen.net/badge/license/CC0/blue" href="https://creativecommons.org/publicdomain/zero/1.0/" />
  </p>
</h1>

<p align="center"><i>A curated list of awesome Fabric resources, libraries and tools - WIP and accepting contributions!</i></p>
<p align="center"><b><a href="https://fabricmc.net/">Fabric</a> is a mod loader for the voxel game <a href="https://en.wikipedia.org/wiki/Minecraft">Minecraft</a>.</b></p>

---

<h2 align="center">Contents <code>🔠</code></h2>

<div align="center">
  <table>
    <tr>
      <th colspan=2>Category</th> <th>Description</th>
    </tr>
    <tr>
      <td>📖</td>
      <td><a href="#resource-">Resource</a></td>
      <td>Learning resources for modding in Fabric.</td>
    </tr>
    <tr>
      <td>🛠️</td>
      <td><a href="#development-️">Development</a></td>
      <td>Mods that help during the development of other mods.</td>
    </tr>
    <tr>
      <td>💾</td>
      <td><a href="#library-">Library</a></td>
      <td>Mods whose functionality is to be used inside other mods.</td>
    </tr>
    <tr>
      <td>🧰</td>
      <td><a href="#tool-">Tool</a></td>
      <td><b>External</b> programs that generally help with Fabric mod/modpack development.</td>
    </tr>
  </table>
</div>

The following symbols are used in this list:
- `🏰` - A link to the [Modrinth](https://modrinth.com/) page of the library/mod.
- `🔝` - The latest Minecraft version supported by the library/mod (as pulled from Modrinth).

---

<h2 align="center">Resource <code>📖</code></h2>

- [Fabric Wiki](https://docs.fabricmc.net/) - The official Fabric wiki with a lot of tips and tutorials. `CC-BY-NC-SA-4.0`
- [Old Fabric Wiki](https://fabricmc.net/wiki/doku.php) - Ye olde Fabric wiki. Looks a bit dated but this is where everything started. `CC-BY-NC-SA-4.0`

### Mixins

- [Official Wiki](https://github.com/SpongePowered/Mixin/wiki) - Contains some in-depth technical information, but is also missing a lot of topics.
- [MixinExtras Wiki](https://github.com/LlamaLad7/MixinExtras/wiki) - MixinExtras is nowadays included in Fabric loader, so you can use all of it out of the box.
- [Unofficial Wiki](https://mixin-wiki.readthedocs.io/) - A simpler and more beginner-friendly version of the official wiki.

---

<h2 align="center">Development <code>🛠️</code></h2>

### Mixins

- [MixinTrace](https://github.com/comp500/mixintrace) - Adds a list of related mixins to crash reports. `MIT`

---

<h2 align="center">Library <code>💾</code></h2>

### Agnostic (Common & Multi-Feature)

- [Fabric API](https://github.com/FabricMC/fabric) [`🏰`](https://modrinth.com/mod/fabric-api) `🔝 1.21.11 / 26.1-snapshot-7` - Essential hooks and patches for modding with Fabric. ([Wiki](https://docs.fabricmc.net/) · [Old Wiki](https://fabricmc.net/wiki)) `Apache-2.0`
- [oωo (owo-lib)](https://github.com/glisco03/owo-lib) [`🏰`](https://modrinth.com/mod/owo-lib) `🔝 1.21.11` - A general utility library for content-focused modding on Fabric. ([Wiki](https://github.com/wisp-forest/owo-lib/blob/1.18.2/README.md)) `MIT`

### Audio

- [Sound Categories](https://github.com/stashingco/sound-categories) [`🏰`](https://modrinth.com/mod/sound-categories) `🔝 1.19` - Allows mods to add more sound categories, and modifies the Minecraft sound settings menu to fit as many categories as required. ([Wiki](https://github.com/stashingco/sound-categories/blob/main/README.md)) `Apache-2.0`

### Chat

- [AdvancedChatCore](https://github.com/DarkKronicle/AdvancedChatCore) [`🏰`](https://modrinth.com/mod/advancedchatcore) `🔝 1.19.4` - The base mod of all AdvancedChat modules and features, presenting an API to achieve many different functionalities related to the Minecraft chat. ([Wiki](https://darkkronicle.github.io/AdvancedChatCore/)) `MPL-2.0`
- [oωo (owo-lib)](https://github.com/glisco03/owo-lib) [`🏰`](https://modrinth.com/mod/owo-lib) `🔝 1.21.11` - A general utility library for content-focused modding on Fabric. ([Wiki](https://docs.wispforest.io/owo/setup)) `MIT`

### Configs

- [Cloth Config](https://github.com/shedaniel/ClothConfig/) [`🏰`](https://modrinth.com/mod/cloth-config) `🔝 1.21.11` - A full-fledged, annotation-based configuration library. ([Wiki](https://shedaniel.gitbook.io/cloth-config/)) `Apache-2.0`
- [oωo (owo-lib)](https://github.com/glisco03/owo-lib) [`🏰`](https://modrinth.com/mod/owo-lib) `🔝 1.21.11` - Another annotation-based full config library ([Wiki](https://docs.wispforest.io/owo/config)) `MIT`

### Data Parsing, Loading & Generation

- [ARRP](https://github.com/Devan-Kerman/ARRP) [`🏰`](https://modrinth.com/mod/arrp) `🔝 1.21.11 / 26.1-snapshot-6` - **A**dvanced **R**untime **R**esource **P**acks (for Fabric). ([Wiki](https://github.com/Devan-Kerman/ARRP/wiki)) `MPL-2.0`

### Documentation

- [Patchouli](https://github.com/VazkiiMods/Patchouli/) [`🏰`](https://modrinth.com/mod/patchouli) `🔝 1.21.1` - A mod that aims to provide easy to implement, data-driven documentation for minecraft modders and modpack makers alike. ([Wiki]()) `BY-NC-SA 3.0`

### Food

- [Capsaicin](https://github.com/Siphalor/capsaicin) - Allows to dynamically modify food properties of items. `Apache-2.0`

### Entities

#### Disguising & Impersonation

- [DisguiseLib](https://github.com/NucleoidMC/DisguiseLib) [`🏰`](https://modrinth.com/mod/disguiselib) `🔝 1.19.3` - A (server-side) library for disguising entities in Minecraft. `MIT`
- [Impersonate](https://github.com/Ladysnake/Impersonate) [`🏰`](https://modrinth.com/mod/impersonate) `🔝 1.21.4` - Allows players to take on the name and appearance of other players. `LGPL-3.0-only`

### Generation

- [Terraformers' Shapes](https://github.com/TerraformersMC/Terraform) - A context independent library for generating voxel shapes using mathematical equations. ([Wiki](https://github.com/TerraformersMC/Shapes/wiki/Using-Shapes)) `MIT`

### GUIs & Menus

- [SpruceUI](https://github.com/LambdAurora/SpruceUI) - Utilities for creating GUIs. `MIT`
- [Main Menu Credits](https://github.com/isXander/main-menu-credits) [`🏰`](https://modrinth.com/mod/main-menu-credits) `🔝 1.21.8` - Adds a way of adding information to the user's title screen. ([Wiki](https://github.com/isXander/main-menu-credits/wiki/Usage)) `LGPL-3.0-only`

### Input Methods & Keybinds

- [Amecs' API](https://github.com/Siphalor/amecs-api) - Allows to define modifier keys (control, shift, alt) for keybindings. `Apache-2.0`
- [No More Useless Keys - NMUK](https://github.com/Siphalor/nmuk) [`🏰`](https://modrinth.com/mod/nmuk) `🔝 1.21.11` - Allows you to specify an arbitrary amount of alternative key combinations for key bindings. `Apache-2.0`

### Inventory & Transfer Systems

- [Trinkets](https://github.com/emilyalexandra/trinkets) [`🏰`](https://modrinth.com/mod/trinkets) `🔝 1.21.1` - A data-driven accessory mod that adds a slot group and slot system to Minecraft. ([Wiki](https://github.com/emilyploszaj/trinkets/wiki)) `MIT`
- [LibBlockAttributes](https://github.com/AlexIIL/LibBlockAttributes) -  ([Wiki](https://github.com/AlexIIL/LibBlockAttributes/wiki)) `MPL-2.0`

### Items & Equippables

- [Shield Lib](https://github.com/StellarWind22/Shield-Lib) [`🏰`](https://modrinth.com/mod/shieldlib) `🔝 1.21.8` - Library mod for easily adding shields, and shield enchantments into the game. ([Wiki](https://fabricmc.net/wiki/tutorial:shield)) `LGPL-2.1`

### Low-Level Manipulation (e.g. mixins or bytecode)

- [Fabric-ASM](https://github.com/Chocohead/Fabric-ASM) - Utilities for manipulating Java byte code and extending enums. `MPL-2.0`
- [Mixin Constraints](https://github.com/Moulberry/MixinConstraints) - Annotation-based system to conditionally enable/disable Mixins. `MIT`

### Multipart

- [LibMultiPart](https://github.com/AlexIIL/LibMultiPart) - Adds support for multiple "parts" (such as pipes, facades, wires, etc) in a single block. ([Wiki]([https://github.com/AlexIIL/LibMultiPart/wiki](https://github.com/AlexIIL/LibMultiPart/wiki/Brief-overview))) `MPLv2.0`

### Networking & Packets

- [LibNetworkStack](https://github.com/AlexIIL/LibNetworkStack) - Adds a networking layer for mods to communicate data more easily. ([Wiki](https://github.com/AlexIIL/LibNetworkStack/wiki)) `MPL-2.0`

### Recipes & Crafting

- [Nbt Crafting](https://github.com/Siphalor/nbt-crafting) [`🏰`](https://modrinth.com/mod/nbt-crafting) `🔝 1.19.2` - JSON-driven nbt data in recipes and remainders as well as brewing recipes and a lot more. ([Wiki](https://mcwiki.siphalor.de/nbt-crafting/v2)) `Apache-2.0`
- [Push To Craft](https://github.com/Siphalor/push-to-craft) [`🏰`](https://modrinth.com/mod/push-to-craft) `🔝 1.19.2` - Allows to provide alternatives for recipe ingredients in a general fashion. `MIT`
- [Smart Recipes](https://github.com/Kir-Antipov/smart-recipes) [`🏰`](https://modrinth.com/mod/smart-recipes) `🔝 1.20.4` - Extends the recipe format with conditions. ([Wiki](https://github.com/Kir-Antipov/smart-recipes#readme)) `MIT`

### Visual, Models, Rendering & Animation

- [GeckoLib](https://github.com/bernie-g/geckolib) [`🏰`](https://modrinth.com/mod/geckolib) `🔝 1.21.11` - Forward kinematic gui-based animation engine. ([Wiki](https://github.com/bernie-g/geckolib/wiki/Getting-Started)) `LGPL-3.0-only`
- [LibZoomer](https://github.com/EnnuiL/LibZoomer/issues) - A library for Minecraft 1.17+ that allows other mods to zoom easily while being able to customize it for their own needs. `MIT`
- [JsonEM](https://github.com/FoundationGames/JsonEM) [`🏰`](https://modrinth.com/mod/jsonem) `🔝 1.21.8` - Library for modders, resource pack makers, and modpack makers to create and edit entity models with JSON. ([Wiki](https://github.com/FoundationGames/JsonEM/blob/1.18/README.md)) `MIT`
- [JSON Model Extensions](https://github.com/vram-guild/json-model-extensions) [`🏰`](https://modrinth.com/mod/imx) `🔝 1.20.1` - Adds support for [FREX Rendering API](https://github.com/vram-guild/frex) features to Minecraft JSON model loading. ([Wiki](https://github.com/vram-guild/json-model-extensions/wiki)) `LGPL-3`
- [FREX](https://github.com/vram-guild/frex) [`🏰`](https://modrinth.com/mod/imx) `🔝 1.20.1` - A rendering API for Minecraft mods to create content that wouldn't normally be possible. ([Wiki](https://github.com/vram-guild/frex/wiki)) `LGPL-3.0-only`
- [UltralightFabric](https://github.com/isXander/UltralightFabric) [`🏰`](https://modrinth.com/mod/ultralightfabric) `🔝 1.18.1` - A HTML renderer for Fabric. ([Wiki](https://github.com/isXander/UltralightFabric/wiki)) `LGPL-3.0-only`
- [Renderer](https://github.com/0x3C50/Renderer) [`🏰`](https://modrinth.com/mod/renderer) `🔝 1.20.4` - An easy-to-use rendering library for modern FabricMC. ([Wiki](https://github.com/0x3C50/Renderer/blob/master/README.md)) `BSD-3-Clause`

---

<h2 align="center">Tool <code>🧰</code></h2>

### Inspection

- [mod_jar_inspector](https://github.com/comp500/mod_jar_inspector) - Allows you to inspect mods in a directory like listing all jar-in-jars or all mixins. `GPL-3.0-only`

### Generators

- [GeneratorFabricMod](https://github.com/ExtraCrafTX/GeneratorFabricMod) - Prompts for various information and outputs a skeleton mod, ready to be modified. `Apache-2.0`

### Versioning

- [GIUP](https://github.com/Siphalor/giup) - Helps to maintain mods that are spread across Git branches for different MC versions. `Apache-2.0`

### IDE Plugins

- [Minecraft Development for IntelliJ](https://github.com/minecraft-dev/MinecraftDev) - Plugin for IntelliJ IDEA that helps with mixins, fabric.mod.json files and contains a lot of other small tweaks. ([Wiki](https://minecraftdev.org/docs)) `MIT`

### Mappings

- [mappings.dev](https://mappings.dev) - A website that allows you to convert between different mappings formats, Yarn, MCP, intermediary and Mojmap.
- [yarn-cli](https://github.com/ByMartrixx/yarn-cli) - CLI to look up yarn/intermediary mappings. `MIT`
