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

<h2 align="center">Contents <code>📑</code></h2>

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

---

<h2 align="center">Resource <code>📖</code></h2>

- [Fabric Wiki](https://fabricmc.net/wiki/doku.php) - The official Fabric wiki with a lot of tips and tutorials. `CC-BY-NC-SA-4.0`

---

<h2 align="center">Development <code>🛠️</code></h2>

### Mixins

- [MixinTrace](https://github.com/comp500/mixintrace) - Adds a list of related mixins to crash reports. `MIT`

---

<h2 align="center">Library <code>💾</code></h2>

### Agnostic (Common & Multi-Feature)

- [Fabric API](https://github.com/FabricMC/fabric) - Essential hooks and patches for modding with Fabric. ([Wiki](https://fabricmc.net/wiki)) `Apache-2.0`
- [Mesh](https://github.com/GlassPane/Mesh) - A modding library with various utilities, such as auto-registration of items and blocks, or crafting recipe generation. ([Wiki](https://github.com/GlassPane/Mesh/blob/1.18/README.md)) `LGPL-3.0-only`
- [oωo (owo-lib)](https://github.com/glisco03/owo-lib) - A general utility library for content-focused modding on Fabric. ([Wiki](https://github.com/wisp-forest/owo-lib/blob/1.18.2/README.md)) `MIT`

### Audio

- [Sound Categories](https://github.com/stashingco/sound-categories) - Allows mods to add more sound categories, and modifies the Minecraft sound settings menu to fit as many categories as required. ([Wiki](https://github.com/stashingco/sound-categories/blob/main/README.md)) `Apache-2.0`

### Chat

- [AdvancedChatCore](https://github.com/DarkKronicle/AdvancedChatCore) - The base mod of all AdvancedChat modules and features, presenting an API to achieve many different functionalities related to the Minecraft chat. ([Wiki](https://darkkronicle.github.io/AdvancedChatCore/)) `MPL-2.0`

### Configs

- [AutoConfig](https://github.com/shedaniel/AutoConfig) - A full-fledged, annotation-based configuration library. ([Wiki](https://shedaniel.gitbook.io/cloth-config/auto-config)) `Apache-2.0`
- [Cloth Config](https://github.com/shedaniel/cloth-config) - A client side API for creating configuration screens. ([Wiki](https://shedaniel.gitbook.io/cloth-config)) `Unlicense`

### Data Parsing & Loading

- [Bow Tie](https://github.com/Siphalor/bow-tie/) - Data loading interceptor that enables the use of Hjson, YAML, XML and more instead of JSON. `Apache-2.0`

### Documentation

- [Patchouli](https://github.com/VazkiiMods/Patchouli/) - A mod that aims to provide easy to implement, data-driven documentation for minecraft modders and modpack makers alike. ([Wiki]()) `BY-NC-SA 3.0`

### Entities

#### Disguising & Impersonation

- [DisguiseLib](https://github.com/NucleoidMC/DisguiseLib) - A (server-side) library for disguising entities in Minecraft. `MIT`
- [Impersonate](https://github.com/Ladysnake/Impersonate) - Allows players to take on the name and appearance of other players. ([Wiki](https://github.com/Ladysnake/Impersonate/blob/1.17/README.md)) `LGPL-3.0-only`

#### Villagers & Trading

- [SimpleJsonVillagerTrades](https://github.com/aws404/SimpleJsonVillagerTrades) - A small jar-in-jar-able or standalone library to modify/add merchant trades via datapacks. ([Wiki](https://github.com/aws404/SimpleJsonVillagerTrades/wiki/Trade-Offer-JSON-Files)) `CC0`

#### Piglins & Bartering

- [Piglib](https://github.com/Shnupbups/Piglib) - Adds item tags for various Piglin related things that Mojang were too silly to add themselves! ([Wiki](https://github.com/Shnupbups/Piglib/blob/1.18.2/README.md)) `LGPL-3.0-only`

#### Attributes

- [Air Strafing Attribute](https://github.com/CammiePone/Air-Strafing-Attribute) - Adds an attribute for the flyingSpeed variable so multiple mods can safely modify the air strafing speed of entities. ([Wiki](https://github.com/CammiePone/Air-Strafing-Attribute/blob/1.17-dev/README.md)) `MIT`

### Generation

- [Terraformers' Shapes](https://github.com/TerraformersMC/Shapes) - A context independent library for generating voxel shapes using mathematical equations. ([Wiki](https://github.com/TerraformersMC/Shapes/wiki/Using-Shapes)) `MIT`

### GUIs & Menus

- [SpruceUI](https://github.com/LambdAurora/SpruceUI) - Utilities for creating GUIs. `MIT`
- [Main Menu Credits](https://github.com/isXander/main-menu-credits) - Adds a way of adding information to the user's title screen. ([Wiki](https://github.com/isXander/main-menu-credits/wiki/Usage)) `LGPL-3.0-only`

### Input Methods & Keybinds

- [Amecs' API](https://github.com/Siphalor/amecs-api) - Allows to define modifier keys (control, shift, alt) for keybindings. `Apache-2.0`
- [No More Useless Keys - NMUK](https://github.com/Siphalor/nmuk) - Allows you to specify an arbitrary amount of alternative key combinations for key bindings. `Apache-2.0`

### Inventory & Transfer Systems

- [Trinkets](https://github.com/emilyalexandra/trinkets) - A data-driven accessory mod that adds a slot group and slot system to Minecraft. ([Wiki](https://github.com/emilyploszaj/trinkets/wiki)) `MIT`
- [LibBlockAttributes](https://github.com/AlexIIL/LibBlockAttributes) -  ([Wiki](https://github.com/AlexIIL/LibBlockAttributes/wiki)) `MPL-2.0`

### Items & Equippables

- [Fabric Shield Lib](https://github.com/CrimsonDawn45/Fabric-Shield-Lib) - Library mod for easily adding shields, and shield enchantments into the game. ([Wiki](https://fabricmc.net/wiki/tutorial:shield)) `LGPL-2.1`

### Kotlin

- [Fabrik](https://modrinth.com/mod/fabrik) - An API for using FabricMC with Kotlin. It is the bridge between Minecraft and common Kotlin language features, libraries, [DSLs](https://en.wikipedia.org/wiki/Domain-specific_language) and more. ([Wiki](https://jakobkmar.github.io/fabrikmc/)) `GPL-3.0-only`

### Low-Level Manipulation (E.g. Bytecode)

- [Fabric-ASM](https://github.com/Chocohead/Fabric-ASM) - Utilities for manipulating Java byte code and extending enums. `MPL-2.0`

### Miscellaneous & Humor

- [owo](https://github.com/MaowImpl/owo) - [Zuzak](https://github.com/zuzak)'s JS [furry-speak transformation library](https://github.com/zuzak/owo) ported to a Java library.

### Multipart

- [LibMultiPart](https://github.com/AlexIIL/LibMultiPart) - Adds support for multiple "parts" (such as pipes, facades, wires, etc) in a single block. ([Wiki]([https://github.com/AlexIIL/LibMultiPart/wiki](https://github.com/AlexIIL/LibMultiPart/wiki/Brief-overview))) `MPLv2.0`

### Networking & Packets

- [LibNetworkStack](https://github.com/AlexIIL/LibNetworkStack) - Adds a networking layer for mods to communicate data more easily. ([Wiki](https://github.com/AlexIIL/LibNetworkStack/wiki)) `MPL-2.0`

### Recipes & Crafting

- [Nbt Crafting](https://github.com/Siphalor/nbt-crafting) - JSON-driven nbt data in recipes and remainders as well as brewing recipes and a lot more. ([Wiki](https://mcwiki.siphalor.de/nbt-crafting/v2)) `Apache-2.0`
- [Push To Craft](https://github.com/Siphalor/push-to-craft) - Allows to provide alternatives for recipe ingredients in a general fashion. `MIT`
- [Smart Recipes](https://github.com/Kir-Antipov/smart-recipes) - Extends the recipe format with conditions. ([Wiki](https://github.com/Kir-Antipov/smart-recipes#readme)) `MIT`

### Visual, Models, Rendering & Animation

- [GeckoLib](https://github.com/bernie-g/geckolib) - Forward kinematic gui-based animation engine. ([Wiki](https://github.com/bernie-g/geckolib/wiki/Getting-Started)) `LGPL-3.0-only`
- [LibZoomer](https://github.com/EnnuiL/LibZoomer/issues) - A library for Minecraft 1.17+ that allows other mods to zoom easily while being able to customize it for their own needs. `MIT`
- [JsonEM](https://github.com/FoundationGames/JsonEM) - Library for modders, resource pack makers, and modpack makers to create and edit entity models with JSON. ([Wiki](https://github.com/FoundationGames/JsonEM/blob/1.18/README.md)) `MIT`
- [JSON Model Extensions](https://github.com/vram-guild/json-model-extensions) - Adds support for [FREX Rendering API](https://github.com/vram-guild/frex) features to Minecraft JSON model loading. ([Wiki](https://github.com/vram-guild/json-model-extensions/wiki)) `LGPL-3`
- [FREX](https://github.com/vram-guild/frex) - A rendering API for Minecraft mods to create content that wouldn't normally be possible. ([Wiki](https://github.com/vram-guild/frex/wiki)) `LGPL-3.0-only`
- [UltralightFabric](https://github.com/isXander/UltralightFabric) - A HTML renderer for Fabric. ([Wiki](https://github.com/isXander/UltralightFabric/wiki)) `LGPL-3.0-only`
- [Renderer](https://github.com/0x3C50/Renderer) - An easy-to-use rendering library for modern FabricMC. ([Wiki](https://github.com/0x3C50/Renderer/blob/master/README.md)) `BSD-3-Clause`

---

<h2 align="center">Tool <code>🧰</code></h2>

### Conversion

- [Entity Model Remapper](https://github.com/Draylar/entity-model-remapper) - An [online tool](https://www.draylar.dev/entity-model-remapper) to convert entity models between Yarn and MCP mappings. `MIT`

### Inspection

- [mod_jar_inspector](https://github.com/comp500/mod_jar_inspector) - Allows you to inspect mods in a directory like listing all jar-in-jars or all mixins. `GPL-3.0-only`

### Generators

- [GeneratorFabricMod](https://github.com/ExtraCrafTX/GeneratorFabricMod) - Prompts for various information and outputs a skeleton mod, ready to be modified. `Apache-2.0`

### Versioning

- [GIUP](https://github.com/Siphalor/giup) - Allows to maintain mods that are spread across branches for different MC versions. `Apache-2.0`

### IDE Plugins

- [Minecraft Development for IntelliJ](https://github.com/minecraft-dev/MinecraftDev) - Plugin for IntelliJ IDEA that helps with mixins, fabric.mod.json files and contains a lot of other small tweaks. ([Wiki](https://minecraftdev.org/docs)) `MIT`

### Mappings

- [yarn-cli](https://github.com/ByMartrixx/yarn-cli) - CLI to look up yarn/intermediary mappings. `MIT`
