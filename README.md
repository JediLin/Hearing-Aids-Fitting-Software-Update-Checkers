# Hearing Aids Fitting Software Update Checkers
A collection of scripts which check hearing aids fitting software directly from their own update servers.

![Total downloads](https://img.shields.io/github/downloads/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/total?label=Total%20downloads&style=for-the-badge)
![Latest release](https://img.shields.io/github/v/release/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers?label=Latest%20release&style=for-the-badge)
![Latest release downloads)](https://img.shields.io/github/downloads/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/latest/total?label=Latest%20release%20downloads&style=for-the-badge)
<br/>
![Commits since tagged version](https://img.shields.io/github/commits-since/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/latest?style=for-the-badge)
![Last commit](https://img.shields.io/github/last-commit/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers?style=for-the-badge)
![Open issues](https://img.shields.io/github/issues/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers?style=for-the-badge)

## What does it do?
This project (\"The Checker\") contains scripts which can check hearing aids fitting software (such as Phonak Target) directly from each own update servers with APIs, so that you can easily know if there is a newer version available, and check corresponding files.

## Currently supported software
This project currently supports:
- Sonova
  - Phonak [Target](https://www.phonak.com/en-int/professionals/innovations/target)
    - Phonak Target Media
    - Phonak Target Sounds
  - Phonak iPFG Successware
  - Phonak PFG
  - Phonak [Roger Upgrader](https://www.phonak.com/en-int/hearing-devices/microphones/roger-upgrader)
  - Unitron [TrueFit](https://www.unitron.com/global/en_us/professionals/truefit.html)
  - Hansaton [scout](https://www.hansaton.com/en-int/professionals/support/instr.html)
- Demant
  - Oticon [Genie 2](https://www.oticon.com/professionals/tools-and-support/fitting)
  - Oticon Genie
  - Oticon Genie Medical
  - Bernafon [OasisNXT](https://www.bernafon.com/for-professionals/fitting-software)
  - Bernafon OasisNXT Custom
  - Sonic [ExpressFit Pro](https://www.sonici.com/professional-center/professional-support/software-download)
  - Philips [HearSuite](https://www.hearingsolutions.philips.com/for-professionals/hearsuite)
- GN
  - ReSound [Smart Fit](https://pro.resound.com/en-us/products/resound/fsw-2)
  - ReSound [Aventa](https://www.gnhearing.com/en/products/support-materials/fsw-support)
  - ReSound Pro-Counsel
  - Beltone [Solus Max](https://www.gnhearing.com/en/products/beltone/fsw-2)
  - Beltone Solus Pro
  - Beltone Solus
  - Beltone SelectaFit
  - Interton [Fitting](https://www.interton.com/en/professionals/hearing-aid-fitting)
  - Interton Appraise
  - Interton CompuFit
- WS Audiology
  - Signia [Connexx](https://www.signia-pro.com/en/business-support/connexx/)
  - Rexton [Connexx](https://www.rexton.com/en/professional/connexx/)
  - Audio Service Connexx
  - A&M Connexx
  - Widex [Compass GPS](https://www.widexpro.com/en/business-support/compass/)
- Starkey
  - Starkey [Pro Fit](https://www.starkeypro.com/products/other-products/software/pro-fit)
  - Starkey [Inspire OS](https://www.starkeypro.com/products/other-products/software/inspire)
  - Starkey [PatientBase](https://patientbase.starkeyhearingtechnologies.com)
- HIMSA: [Noahlink Wireless 2 (NW2)](https://www.himsa.com/products/noahlink-wireless-2/) and [Noahlink Wireless (NW1)](https://www.himsa.com/products/noahlink-wireless/)
  - Driver
  - Firmware Upgrader
- [Hearing Aids Fitting Software Update Checkers](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/) (\"The Checker\" itself)

## Where to get it
The latest release version of The Checker is available here: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest

NOTE: You need to have the latest version of Python installed for this to work.

You can also get the latest release version via The Checker's built-in \"*Self Update Checker*\" option.

### Pre-release version
If you don't want to wait for the proper release, the fresh pre-release work-in-progress version is available here: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/archive/refs/heads/main.zip

NOTE: You can also get the pre-release version via The Checker's \"*Extra & Legacy Software Update Checkers*\" option.

## How to use it
1. [Install Python](#pre-requirement-install-python) (and reboot your computer) if you don't have it yet
2. Download The Checker from here: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest<br/>
   Click on the link and then click on the `Hearing-Aids-Fitting-Software-Update-Checkers.zip` link to download it
3. Extract the ZIP to a folder
4. Go to the extracted folder, double-click the `start-Windows.bat` file and follow the instructions on-screen

NOTE: If The Checker looks like it has frozen, then try disabling `quickEdit` by running the `fixQuickedit.reg` file before running `start-Windows.bat`

**WARNING**: The Checker always tries to upgrade `pip` and some used Python packages. If you are using Python for other reasons and need to keep particular version, be advised to make your own backup or prepare a seperate environment.

### Pro-tip & Configuration
Not all market regions get the same versions for all hearing aids fitting software. In case you see newer versions from some forums or sites yet the checkers report older ones, try changing `target market` on-the-fly to other countries to get alternative results. You can check [Versions](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/wiki/Versions) information from our Wiki.

To change checking variables such as (target) `Market` or (spoof) `Version`, simply edit `config.ini` with any plain-text editor. This file is sectioned by hearing aid brands.

This project will try to keep up changing default target market for most up-to-date results. Scripts automatically fetch this information from this project (*LiveUpdate*-ish) without needing to re-download the whole release package.

### Pre-requirement: Install Python
The following steps only need to be done **ONCE** on each system:
1. Go to: https://www.python.org/downloads/
2. Click on the yellow `Download Python` button and run the installer
3. Make sure you select `Add python.exe to PATH` in the start of the installer, and then click on `Install Now`
4. **Reboot your computer**

NOTE: If you run The Checker (on Windows OS) without Python installed yet, The Checker will refuse to run and bring you to Python download page instead.

## Credits
- [@Blue](https://forum.hearingtracker.com/u/blue/summary): Original author of this project (up to v1.8.0)
- [@pvc](https://forum.hearingtracker.com/u/pvc/summary): Assisting with testing of the script and finding software links, providing `StarkeyOtherBrands.bat` and rebranded hearing aids information
- [@tenkan](https://forum.hearingtracker.com/u/tenkan/summary): Finding the Genie (2) download page links
- [@labuwx](https://github.com/labuwx): Provide [vital information](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/3) about rebranded private label variations of Bernafon OasisNXT
- [@tux-mania](https://github.com/tux-mania): Report bugs and help testing

## Changelog

### Pre-release (work-in-progress)
- HIMSA: official site is using br encoding (need to import `brotli` for that)
- HIMSA: headers spoof

### v2025.07.22
- Skip on individual file checking error, rather than break on it
- Clean-up unused module
- Reduce requests
- Quick Scan: automatically turn off certification security verification for Starkey PatientBase (with warning) if needed
- Quick Scan: add Phonak Roger Upgrader
- Quick Scan: color adjustment
- Phonak: check Roger Upgrader directly from official Roger Upgrader site, removing 3rd-party services dependency
- Phonak: fix Roger Upgrader checker fallback version display logic
- Hansaton: properly using `config.ini`
- Signia: update configuration for Signia Connexx v9.13.5.1814
- Rexton/Audio Service/A&M: using `SupportTools` and `UpdateManager` configuration from `[Signia]` section of `config.ini`
- Starkey: tweak version number display format for PatientBase
- HIMSA: check from official Noahlink Wireless site, removing 3rd-party services dependency

### v2025.07.05
- Starkey: provide a workaround for PatientBase website certification expiration

### v2025.07.04
- Spoof User-Agent string
- HIMSA: add archived version v3.5.0.0 for Noahlink Wireless firmware upgrader
- HIMSA: workaround for error checking file data stream
- Quick Scan: add Starkey PatientBase and HIMSA Noahlink Wireless Firmware Upgrader

### v2025.06.10
- Quick Scan: skip all by default (please edit `config.ini` to enable each scan)

### v2025.06.09
- Using configuration file `config.ini`

### v2025.05.24
- Widex: fix Compass GPS checker for v4.9+ [close [issue #1](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/1)]
- Widex: add manual version support
- Phonak: add iPFG and PFG (options in Target checker)
- Quick Scan: add skip messages
- Add retry messages

### v2025.05.13
- Unitron: fix TrueFit checker for v5.8.0.29338 by changing target market
- Phonak/Unitron/Hansaton/Oticon/Bernafon/Sonic/Philips/Signia/Rexton/Audio Service/A&M/Widex: LiveUpdate-ish default target market code with local fallback (Note: From next Release version on, target market updates will no longer be logged in Changelog anymore.)

### v2025.05.10
- Starkey: fix timezone bug
- Quick Scan: add cool down warning
- Quick Scan: fix timezone bug
- Quick Scan: add `Default` market for certain software
- Menu: better handle GitHub error
- Extra Menu: show last timestamp performing Quick Scan
- Extra Menu: check if the latest Release version contains the latest commit (thus Pre-release version is identical to Release version)
- Prompt adjustment
- Fix color
- Underhood bug fix

### v2025.05.08
- Phonak: fix Roger Upgrader update title for documents
- Add `Quick Scan` option to get all major hearing aids software update across several market at once (ONLY available in Turbo Mode, Extra Menu)

### v2025.05.05
- Phonak: Roger Upgrader update checker (in Extra Menu)
- HIMSA: fix verbose log related bug
- Fix potential Akamai cache miss related bug
- Extra Menu: text adjustment
- Extra Menu: ReBrand Code Viewer
- Pre-Release Checker: change filename with latest commit date and ID
- `StarkeyOtherBrands.bat`
- Offline documents

### v2025.04.21
- Bernafon/Sonic/Philips: target market accepts manually input `default` rather than only accepts pressing Enter with default
- ReSound/Beltone/Interton: add an option to manually specify a version
- Widex: option to change target market (country)
- Clean screen before menus
- Layout adjustment

### v2025.04.14
- Unitron: fix TrueFit checker for v5.7.1 by changing default target market
- Hansaton: fix scout checker for v5.7.1 by changing default target market

### v2025.04.13
- Phonak/Unitron/Hansaton/Oticon/Bernafon/Sonic/Philips/Signia/Rexton/Audio Service/A&M: target market (country) input accepts country name, 2-letter code, or 3-letter code; input value will be checked against ISO 3166 data and converted into 2-letter code accordingly
- Extra Menu: provide last update date and corresponding commit ID of pre-release version

### v2025.04.09
- Starkey: auto-detect country name of current geolocation
- Starkey: check latest version of PatientBase from official webpage [close [issue #5](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/5)]
- HIMSA: check actual update via 3rd-party web service [close [issue #6](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/6)]

### v2025.04.07
- Phonak/Unitron/Hansaton/Oticon/Bernafon/Sonic/Philips: script tweak for easy changing target market and base version
- Phonak/Unitron/Hansaton/Oticon/Bernafon/Sonic/Philips/Signia/Rexton/Audio Service/A&M: prompt target market (country) code before checking
- Starkey: prompt current location (country name) before checking

### v2025.04.05
- Rexton: fix Connexx checker for v9.13.0.1436 by changing target market
- Audio Service: fix Connexx checker for v9.13.0.1420 by changing target market
- Signia/Rexton/Audio Service/A&M: script tweak for easy changing target market and base version

### v2025.04.04
- HIMSA: update Noahlink Wireless firmware upgrader to v3.3.0.0

### v2025.04.02
- Starkey: detailed message if no update available
- Starkey: add checker for PatientBase in the Extra Menu
- Sonic: `ExpressFit` should be `ExpressFit Pro`
- HIMSA: add checker for driver and firmware upgrader in the Extra Menu
- Documents improved

### v2025.03.04
- Starkey: move Inspire OS Checker into Extra Menu
- Oticon: add checker for Genie 2 2025+ and move previous checker (for 2024+) into Extra Menu

### v2025.01.29
- Windows: using code page 65001 (UTF-8)
- Extra Menu: option to show version changes

### v2025.01.28
- Extra Menu: option to check Custom version of Bernafon OasisNXT for private label variations such as `Delight`, `ProAkustik`, `Lisound`, `Specsavers`, `Meditrend`, `GPL`, `Maico`, `Audilab`, `RITM`, `Hoerex`, and `Sonic` [close [issue #3](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/3)]
- Audio Service: fix Connexx checker for v9.12.0.1550 [close [issue #4](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/4)]

### v2024.12.22
- Phonak: fix Target checker for v10.0.1 [close [issue #2](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/2)]
- Phonak: failsafe for Target Media checker
- Document (README) update

### v2024.12.06
- Fix display on older Windows versions (such as Windows 7 or Windows 8)
- Messages tweak

### v2024.11.27
- Extra Menu: option to download the pre-release version of \"The Checker\" (this project)
- Unlockable achievement (secret)

### v2024.11.26
- Colorful
- Phonak/Unitron/Hansaton: fix manual version re-prompting while format error
- Extra Menu: option to open GitHub page of this project with default web browser
- Self Update Checker: the pre-release version mechanism is not working, reverted

### v2024.11.20
- Turbo mode (secret)
- Checkers: layout adjustment and name alignment

### v2024.11.19
- Menu: Extra menu contains Phonak Target Media and Sounds, and legacy software of Demant brands (Oticon/Bernafon/Sonic/Philips)
- Menu: option names change and layout adjustment
- Self Update Checker: better display new version information
- Fix typo and terms
- Minor display layout adjustment

### v2024.11.18
- Signia/Rexton/Audio Service/A&M: better version info display
- Minor display layout adjustment

### v2024.11.17
- Python: always try to upgrade pip
- Self Update Checker: offer the ability to fetch the latest release version, and the pre-release work-in-progress version
- Self Update Checker: better version info display
- Starkey: better version info display

### v2024.11.16
- Self Update Checker: automatically and manually check for latest release version of this script itself from GitHub
- README: better instruction on installing Python

### v2024.11.12
- Menu: fix version number display
- Phonak: automatically query for latest version number of Target software while checking Target Media and Sounds, manually input required no more

### v2024.11.11
- Checkers: better provide the latest version information so users can skip the download process without breaking the menu loop
- Widex: better handle server responses
- Remove unused batch file
- Tweak Linux/macOS shell script

### v2024.11.07
- Display: set CMD window/buffer size to 160x30
- Display: fix menu layout for script version number
- Menu: better handle menu loop
- Menu: present Phonak Target Media and Sounds Update Checkers
- Python: check Python first and open its download page if not installed yet
- Python: Require rot-codec to store API keys
- Python: automatically install/upgrade packages
- Oticon/Bernafon/Sonici/Philips: clean-up unnecessary request content
- Oticon/Bernafon/Sonici/Philips: comments on base version required to get further (newer) updates and how to set them if needed in the future
- Widex: show update server responses
- Starkey: using geoIP, baseVer, and baseOS variables for easier updating scripts in the future if needed
- Starkey: better handle null update response
- Phonak: fix version numbering for its scheme changed since v10.0.0

### v2024.08.31
- Name changes
- Versoning scheme changes to date-based
- Add support for A&M Connexx
- Add support for Audio Services Connexx
- Add support for Bernafon OasisNXT v2024+
- Add support for Hansaton scout
- Add support for Oticon Genie 2 v2024+
- Add support for Philips HearSuite v2024+
- Add support for Phonak Target Media
- Add support for Phonak Target Sounds
- Add support for Sonic ExpressFit v2024+
- Add support for Starkey Pro Fit
- Add support for Starkey Inspire
- Fix Starkey intermediate SSL Certificate error
- Fix bugs
- Add exit script
- Pausing after requirement-checks
- Update README

### v1.8.0 / 2022.12.06
- Add native Linux and MacOS Support

### v1.7.6 / 2022.12.04
- Fix debug logging utility bug

### v1.7.5 / 2022.12.04
- Add debug logging utility

### v1.7.4 / 2022.11.24
- Fixed Widex Compass GPS Localisation Errors
- Fixed Typos

### v1.7.3
- Fix bugs

### v1.7.2
- Fix library bug

### v1.7.1
- Fix typos

### v1.7.0
- Add folder selection GUI
- Add support for GN Resound Smart Fit
- Add support for GN Resound Aventa
- Add catch for server index download errors
- Fix download location bugs in Bernafon Oasis & Oticon Genie 2 checkers

### v1.6.3 / 2022.11.20
- Fix folder path selection bug

### v1.6.2 / 2022.11.11
- Fix Unitron checker Bug

### v1.6.1 / 2022.11.02
- Fix Phonak Target checker Bug
- Fix script name mistake

### v1.6.0 / 2022.10.31
- Add support for Rexton Connexx

### v1.5.0 / 2022.10.31
- Add support for OasisNXT
- Fix bugs

### v1.4.0 / 2022.10.31
- Split up the Genie checkers into separate versions
- Update Genie 2 checker to also use updater
- Fix bugs

### v1.3.0 / 2022.10.30
- Add support for Widex Compass GPS

### v1.2.0 / 2022.10.30
- Add support for Unitron TrueFit
- Add downloading progress bar
- Reduce RAM usage when running the script

### v1.1.2 / 2022.10.30
- Fix bugs with selecting download version

### v1.1.0 / 2022.10.30
- Add support for Oticon Genie & Oticon Genie 2

### v1.0.0 / 2022.10.27
- Add support for Phonak Target & Signia Connexx
- Release it publically


## Copyright & DMCA
The Hearing Aids Fitting Software Update Checkers (\"The Checker\") checks software update from associated update servers using associated APIs. The Checker does not contain or distribute any hearing aids fitting software or associated content, nor bypass any DRM protection if there is one. If anyone presents an associated company and believes that there are violations of copyright, please open an issue describing how exactly, so there will be a chance to make all parties happy with the resolve.

## WARANTY/SUPPORT
ANYTHING CAME FROM THE HEARING FITTING SOFTWARE UPDATE CHECKERS (\"THE CHECKER\") IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

THE CHECKER IS NOT IN ANY AFFILIATED WITH THE AUTHORS OR COPYRIGHT HOLDERS OF ANY SOFTWARE ASSOCIATED WITH THE USE OF THE CHECKER. THEY HAVE NO REQUIREMENT TO PROVIDE ANY SUPPORT OR WARANTY TO ANY SOFTWARE ASSOCIATED WITH THE USE OF THE CHECKER. THE AUTHORS AND COPYRIGHT HOLDERS OF ANY SOFTWARE ASSOCIATED WITH THE USE OF THE CHECKER RESERVE THE RIGHT TO TERMINATE ANY USAGE OF SOFTWARE ASSOCIATED WITH THE CHECKER.

## DISCLAIMER
The contributors of the Hearing Aids Fitting Software Update Checkers (\"The Checker\") do not take any responsability for what you do with The Checker. All rights and credit go to their rightful owners. No copyright infringement intended.

The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by any of the companies mentioned in The Checker. Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software. The Checker is an UNOFFICIAL project and the use of associated software may be limited.

## Appendix
- Check our [Wiki](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/wiki)!
- Some less common hearing aids software can be checked via their official websites:
  - [Audina ezFIT](https://www.audina.net/en/professional/software)
  - [AUSTAR Fit](https://www.austar-hearing.net/Fitting+Software) and older software can be found [here](https://www.austar-hearing.com/soft-40.html) or [here](https://soft.austar-hearing.com:4431/software-center/#/)
  - [NewSound Fit](https://www.newsound.cn/软件下载)
  - [Persona Medical ProFit](https://personamedical.com/downloads/)
- Widex lunched a new cloud-based fitting software, [Compass Cloud](https://www.widexpro.com/en/business-support/compass-cloud/), for its new hearing aids using Allure platform. Cloud-based software usually updates only at the server (cloud) side.

Note: these software WILL NOT be included in The Checker.

Modern hearing aids fitting software which supports [Noahlink Wireless](https://www.himsa.com/products/noahlink-wireless/) and/or [Noahlink Wireless 2](https://www.himsa.com/products/noahlink-wireless-2/) programming interface should be certified *BEFORE* release. This means one can check [Certified Noahlink Wireless and Noahlink Wireless 2 Modules](https://www.himsa.com/products/noahlink-wireless-2/certified-noahlink-wireless-modules/) for upcoming version of fitting software before its release.
