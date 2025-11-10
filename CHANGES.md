# Hearing Aids Fitting Software Update Checkers

## Changelog

### v1.0.0 / 2022.10.27
- Add support for Phonak Target & Signia Connexx
- Release it publically

### v1.1.0 / 2022.10.30
- Add support for Oticon Genie & Oticon Genie 2

### v1.1.2 / 2022.10.30
- Fix bugs with selecting download version

### v1.2.0 / 2022.10.30
- Add support for Unitron TrueFit
- Add downloading progress bar
- Reduce RAM usage when running the script

### v1.3.0 / 2022.10.30
- Add support for Widex Compass GPS

### v1.4.0 / 2022.10.31
- Split up the Genie checkers into separate versions
- Update Genie 2 checker to also use updater
- Fix bugs

### v1.5.0 / 2022.10.31
- Add support for OasisNXT
- Fix bugs

### v1.6.0 / 2022.10.31
- Add support for Rexton Connexx

### v1.6.1 / 2022.11.02
- Fix Phonak Target checker Bug
- Fix script name mistake

### v1.6.2 / 2022.11.11
- Fix Unitron checker Bug

### v1.6.3 / 2022.11.20
- Fix folder path selection bug

### v1.7.0
- Add folder selection GUI
- Add support for GN Resound Smart Fit
- Add support for GN Resound Aventa
- Add catch for server index download errors
- Fix download location bugs in Bernafon Oasis & Oticon Genie 2 checkers

### v1.7.1
- Fix typos

### v1.7.2
- Fix library bug

### v1.7.3
- Fix bugs

### v1.7.4 / 2022.11.24
- Fixed Widex Compass GPS Localisation Errors
- Fixed Typos

### v1.7.5 / 2022.12.04
- Add debug logging utility

### v1.7.6 / 2022.12.04
- Fix debug logging utility bug

### v1.8.0 / 2022.12.06
- Add native Linux and MacOS Support

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

### v2024.11.11
- Checkers: better provide the latest version information so users can skip the download process without breaking the menu loop
- Widex: better handle server responses
- Remove unused batch file
- Tweak Linux/macOS shell script

### v2024.11.12
- Menu: fix version number display
- Phonak: automatically query for latest version number of Target software while checking Target Media and Sounds, manually input required no more

### v2024.11.16
- Self Update Checker: automatically and manually check for latest release version of this script itself from GitHub
- README: better instruction on installing Python

### v2024.11.17
- Python: always try to upgrade pip
- Self Update Checker: offer the ability to fetch the latest release version, and the pre-release work-in-progress version
- Self Update Checker: better version info display
- Starkey: better version info display

### v2024.11.18
- Signia/Rexton/Audio Service/A&M: better version info display
- Minor display layout adjustment

### v2024.11.19
- Menu: Extra menu contains Phonak Target Media and Sounds, and legacy software of Demant brands (Oticon/Bernafon/Sonic/Philips)
- Menu: option names change and layout adjustment
- Self Update Checker: better display new version information
- Fix typo and terms
- Minor display layout adjustment

### v2024.11.20
- Turbo mode (secret)
- Checkers: layout adjustment and name alignment

### v2024.11.26
- Colorful
- Phonak/Unitron/Hansaton: fix manual version re-prompting while format error
- Extra Menu: option to open GitHub page of this project with default web browser
- Self Update Checker: the pre-release version mechanism is not working, reverted

### v2024.11.27
- Extra Menu: option to download the pre-release version of \"The Checker\" (this project)
- Unlockable achievement (secret)

### v2024.12.06
- Fix display on older Windows versions (such as Windows 7 or Windows 8)
- Messages tweak

### v2024.12.22
- Phonak: fix Target checker for v10.0.1 [close [issue #2](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/2)]
- Phonak: failsafe for Target Media checker
- Document (README) update

### v2025.01.28
- Extra Menu: option to check Custom version of Bernafon OasisNXT for private label variations such as `Delight`, `ProAkustik`, `Lisound`, `Specsavers`, `Meditrend`, `GPL`, `Maico`, `Audilab`, `RITM`, `Hoerex`, and `Sonic` [close [issue #3](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/3)]
- Audio Service: fix Connexx checker for v9.12.0.1550 [close [issue #4](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/4)]

### v2025.01.29
- Windows: using code page 65001 (UTF-8)
- Extra Menu: option to show version changes

### v2025.03.04
- Starkey: move Inspire OS Checker into Extra Menu
- Oticon: add checker for Genie 2 2025+ and move previous checker (for 2024+) into Extra Menu

### v2025.04.02
- Starkey: detailed message if no update available
- Starkey: add checker for PatientBase in the Extra Menu
- Sonic: `ExpressFit` should be `ExpressFit Pro`
- HIMSA: add checker for driver and firmware upgrader in the Extra Menu
- Documents improved

### v2025.04.04
- HIMSA: update Noahlink Wireless firmware upgrader to v3.3.0.0

### v2025.04.05
- Rexton: fix Connexx checker for v9.13.0.1436 by changing target market
- Audio Service: fix Connexx checker for v9.13.0.1420 by changing target market
- Signia/Rexton/Audio Service/A&M: script tweak for easy changing target market and base version

### v2025.04.07
- Phonak/Unitron/Hansaton/Oticon/Bernafon/Sonic/Philips: script tweak for easy changing target market and base version
- Phonak/Unitron/Hansaton/Oticon/Bernafon/Sonic/Philips/Signia/Rexton/Audio Service/A&M: prompt target market (country) code before checking
- Starkey: prompt current location (country name) before checking

### v2025.04.09
- Starkey: auto-detect country name of current geolocation
- Starkey: check latest version of PatientBase from official webpage [close [issue #5](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/5)]
- HIMSA: check actual update via 3rd-party web service [close [issue #6](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/6)]

### v2025.04.13
- Phonak/Unitron/Hansaton/Oticon/Bernafon/Sonic/Philips/Signia/Rexton/Audio Service/A&M: target market (country) input accepts country name, 2-letter code, or 3-letter code; input value will be checked against ISO 3166 data and converted into 2-letter code accordingly
- Extra Menu: provide last update date and corresponding commit ID of pre-release version

### v2025.04.14
- Unitron: fix TrueFit checker for v5.7.1 by changing default target market
- Hansaton: fix scout checker for v5.7.1 by changing default target market

### v2025.04.21
- Bernafon/Sonic/Philips: target market accepts manually input `default` rather than only accepts pressing Enter with default
- ReSound/Beltone/Interton: add an option to manually specify a version
- Widex: option to change target market (country)
- Clean screen before menus
- Layout adjustment

### v2025.05.05
- Phonak: Roger Upgrader update checker (in Extra Menu)
- HIMSA: fix verbose log related bug
- Fix potential Akamai cache miss related bug
- Extra Menu: text adjustment
- Extra Menu: ReBrand Code Viewer
- Pre-Release Checker: change filename with latest commit date and ID
- `StarkeyOtherBrands.bat`
- Offline documents

### v2025.05.08
- Phonak: fix Roger Upgrader update title for documents
- Add `Quick Scan` option to get all major hearing aids software update across several market at once (ONLY available in Turbo Mode, Extra Menu)

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

### v2025.05.13
- Unitron: fix TrueFit checker for v5.8.0.29338 by changing target market
- Phonak/Unitron/Hansaton/Oticon/Bernafon/Sonic/Philips/Signia/Rexton/Audio Service/A&M/Widex: LiveUpdate-ish default target market code with local fallback (Note: From next Release version on, target market updates will no longer be logged in Changelog anymore.)

### v2025.05.24
- Widex: fix Compass GPS checker for v4.9+ [close [issue #1](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/1)]
- Widex: add manual version support
- Phonak: add iPFG and PFG (options in Target checker)
- Quick Scan: add skip messages
- Add retry messages

### v2025.06.09
- Using configuration file `config.ini`

### v2025.06.10
- Quick Scan: skip all by default (please edit `config.ini` to enable each scan)

### v2025.07.04
- Spoof User-Agent string
- HIMSA: add archived version v3.5.0.0 for Noahlink Wireless firmware upgrader
- HIMSA: workaround for error checking file data stream
- Quick Scan: add Starkey PatientBase and HIMSA Noahlink Wireless Firmware Upgrader

### v2025.07.05
- Starkey: provide a workaround for PatientBase website certification expiration

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

### v2025.07.24
- HIMSA: import `brotli` for checking from official site with `br` content-encoding
- HIMSA: headers spoof

### v2025.07.26
- Fix configuration bug which may cause checking error

### v2025.08.12
- Using the same `OS` string from `General` section of `config.ini` for all checkers
- Quick Scan: minor display adjustment
- Phonak: fix critical bug on checking files from latest Target version
- Phonak: workaround for Target Media checker

### v2025.08.18
- Self Update Checker: prepare for portable release by showing all available release files
- Portable release: bundled with [python-3.13.7-embed-win32](https://www.python.org/ftp/python/3.13.7/python-3.13.7-embed-win32.zip) package and necessary modules

### v2025.08.29
- Add support for Miracle-Ear Harmony II
- ReSound/Beltone/Interton: display full version numbers
- Quick Scan: fix `config.ini` missing bug
- Document update
- Portable release: use [python-3.8.10-embed-win32](https://www.python.org/ftp/python/3.8.10/python-3.8.10-embed-win32.zip) package instead for Windows 7 compatibility

### v2025.09.02
- Phonak: update Roger Upgrader checker [close [issue #8](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/8)]
- Self Update Checker: correct file list order
- Fix document
- Portable release: cache clean-up
- Release filenames change to `HAFS-Update-Checkers.zip` and `HAFS-Update-Checkers_Win32-Portable.zip`

### v2025.10.30
- Python: temporary workaround for Brotli's Python 3.14.x support issue [close [issue #9](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/9)]
- Rexton: update default market
- Starkey: update self-sign certification chain file
- Miracle-Ear: fix checker banner color to match brand color (as menu did)
- Document: Update and add yet another screenshot
- Portable release: update Python modules

### v2025.11.04
- Oticon/Bernafon/Philips: update `config.ini` for checking version 2025.2
- Beltone: check against public update site (no longer support Beltone SelectaFit) [close [issue #10](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/issues/10)]

### Pre-release (work-in-progress)
- Document: update that Python 3.14 works now
- Beltone: fix archived versions
- ReSound/Interton: check against public update site
