# Hearing Aids Fitting Software Update Checkers

## Changelog

### v1.0.0
- Add support for Phonak Target & Signia Connexx
- Release it publically

### v1.1.0
- Add support for Oticon Genie & Oticon Genie 2

### v1.1.2
- Fix bugs with selecting download version

### v1.2.0
- Add support for Unitron TrueFit
- Add downloading progress bar
- Reduce RAM usage when running the script

### v1.3.0
- Add support for Widex Compass GPS

### v1.4.0
- Split up the Genie checkers into separate versions
- Update Genie 2 checker to also use updater
- Fix bugs

### v1.5.0
- Add support for OasisNXT
- Fix bugs

### v1.6.0
- Add support for Rexton Connexx

### v1.6.1
- Fix Phonak Target checker Bug
- Fix script name mistake

### v1.6.2
- Fix Unitron checker Bug

### v1.6.3
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

### v1.7.4
- Fixed Widex Compass GPS Localisation Errors
- Fixed Typos

### v1.7.5
- Add debug logging utility

### v1.7.6
- Fix debug logging utility bug

### v1.8.0
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
- Phonak: fix Target checker for v10.0.1
- Phonak: failsafe for Target Media checker
- Document (README) update

### v2025.01.28
- Extra Menu: option to check Custom version of Bernafon OasisNXT for private label variations such as `Delight`, `ProAkustik`, `Lisound`, `Specsavers`, `Meditrend`, `GPL`, `Maico`, `Audilab`, `RITM`, `Hoerex`, and `Sonic`
- Audio Service: fix Connexx checker for v9.12.0.1550

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
